import os
import pandas as pd
import subprocess
from functools import reduce
import pyensembl

CURRENT_DIR_PATH = os.path.dirname(os.path.abspath("__file__"))

#############
# bmi genes #
#############

def get_genes_from_combinations(combinations_file, ncomb, group, pheno):
    combinations_df = pd.read_csv(combinations_file, low_memory=False)
    # keep only relevant columns
    gene_cols =  [f'Item_{i}' for i in range(1, ncomb + 1)]
    parsed_df = combinations_df.loc[(combinations_df.Group==group)&(combinations_df.Phenotype==pheno)].loc[:, gene_cols]
    return set(parsed_df.values.flatten())

def create_control_gene_set(gtf_file, bmi_genes, store_file):
    gtf_df = pd.read_csv(gtf_file)
    protein_coding_genes = set(gtf_df.loc[gtf_df.gene_type=="protein_coding"].gene_id_stripped)
    control_geneset = protein_coding_genes - bmi_genes 
    with open(store_file, "w") as f:
        for gene in control_geneset:
            f.write(f"{gene}\n")   
    return

###################
# kegg enrichment #
###################

def run_kegg_enrichment(gene_in, table_out):
    cmd = [
        "bash", f"{CURRENT_DIR_PATH}/scripts/kegg_enrich.sh", 
        gene_in, table_out
        ]
    subprocess.run(cmd)
    return

###################
# gsea enrichment #
###################

def run_gsea_enrichment(gene_in, table_out):
    cmd = [
        "bash", f"{CURRENT_DIR_PATH}/scripts/gsea_enrich.sh", 
        gene_in, table_out
        ]
    subprocess.run(cmd)
    return

#####################
# external datasets #
#####################

def map_genenames_to_ids(gtf_file, gene_list):
    data = pyensembl.Genome(
        reference_name = 'GRCh38',
        annotation_name = 'my_genome_features',
        gtf_path_or_url = gtf_file
        )
    data.index(overwrite=False)
    gene_ids = []
    for gn in gene_list:
        try:
            gene_id = data.gene_ids_of_gene_name(gn)[0]
            gene_ids.append(gene_id)
        except ValueError:
            print(f"{gn} not found in GTF file")
    gene_ids = [gi.split(".")[0] for gi in gene_ids if gi]
    return gene_ids

def parse_rarev_genes(rarev_file, store_file, gtf_file):
    f = open(rarev_file, "r")
    gene_list = [i.strip() for i in f.readlines()]
    f.close()
    gene_ids = map_genenames_to_ids(gtf_file, gene_list)
    with open(store_file, "w") as f:
        for gene in gene_ids:
            f.write(f"{gene}\n")    
    return set(gene_ids)

def parse_mgi_genes(mgi_file, store_file, gtf_file):
    f = open(mgi_file, "r")
    gene_list = [i.strip() for i in f.readlines()]
    f.close()
    gene_ids = map_genenames_to_ids(gtf_file, gene_list)
    with open(store_file, "w") as f:
        for gene in gene_ids:
            f.write(f"{gene}\n")    
    return set(gene_ids)

def parse_twas_genes(twas_supp_file, store_file):
    df = pd.read_excel(twas_supp_file, sheet_name="S4")
    gene_ids = df.Gene.unique()
    with open(store_file, "w") as f:
        for gene in gene_ids:
            f.write(f"{gene}\n")
    return set(gene_ids)

def add_set(a,b):
    return a.union(b)

def create_external_geneset(genesets, store_file):
    all_externals = set(reduce(add_set, genesets))
    with open(store_file, "w") as f:
        for gene in all_externals:
            f.write(f"{gene}\n")    
    return

#######################
# external enrichment #
#######################

def get_set_from_file(file):
    f = open(file, "r")
    l = f.readlines()
    l = set([i.strip() for i in l])
    f.close()
    return l

def create_contingency_table(bmi_genes_file, control_gene_file, external_gene_file, save_file):
    bmi_gene_set = get_set_from_file(bmi_genes_file)
    control_gene_set = get_set_from_file(control_gene_file)
    external_gene_set = get_set_from_file(external_gene_file)
    bmi_overlap = bmi_gene_set.intersection(external_gene_set)
    control_gene_set_overlap = control_gene_set.intersection(external_gene_set)
    data_dict = {
        "data_type": ["bmi", "control_geneset"],
        "overlap": [len(bmi_overlap), len(control_gene_set_overlap)],
        "non_overlap": [len(bmi_gene_set) - len(bmi_overlap), len(control_gene_set) - len(control_gene_set_overlap)],
    }
    data_df = pd.DataFrame(data_dict).set_index("data_type")
    data_df.to_csv(save_file, index=True, header=True)
    return data_df

def run_fishers_enrichment(contingency, table_out):
    cmd = [
        "bash", f"{CURRENT_DIR_PATH}/scripts/fishers_exact.sh", 
        contingency, table_out
        ]
    subprocess.run(cmd)
    return
