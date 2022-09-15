import collections
import os
import pandas as pd


DESC = """get partner genes of the genes the genes present in both high and low bmi pheno"""

def save_partner_genes(combo2f, combo3f, save_dir):
    # read the combo file
    combinations2_df = pd.read_csv(combo2f, low_memory=False)
    combinations3_df = pd.read_csv(combo3f, low_memory=False)
    # add gene combo information
    combinations2_df["gene_combos"] = list(map(lambda x: ":".join(x), zip(*[combinations2_df[f"Item_{i}"] for i in range(1, 2 + 1)])))
    combinations3_df["gene_combos"] = list(map(lambda x: ":".join(x), zip(*[combinations3_df[f"Item_{i}"] for i in range(1, 3 + 1)])))
    # concat and create a dataframe with relevant columns only
    relevant_columns = ["gene_combos", "Phenotype", "Group"]
    parsed_df = pd.concat((combinations2_df.loc[:, relevant_columns], combinations3_df.loc[:, relevant_columns]))
    # take only white british group
    parsed_df = parsed_df.loc[parsed_df.Group=="white_british"]
    # map genes to their phenotype
    gene_2_pheno_dict = collections.defaultdict(set)
    for gc, p in zip(parsed_df.gene_combos, parsed_df.Phenotype):
        for g in gc.split(":"):
            gene_2_pheno_dict[g].add(p)
    # get genes involved in both phenotype
    both_pheno_genes = [g for g,p in gene_2_pheno_dict.items() if len(p)==2]
    # get their high and low partners
    partner_gene_dict = {g:{"high":set(), "low": set()} for g in both_pheno_genes}
    for bpg in both_pheno_genes:
        bpg_df = parsed_df.loc[parsed_df.gene_combos.str.contains(bpg)]
        low_bmi_partners = [g for gc in bpg_df.loc[bpg_df.Phenotype=="low_bmi"].gene_combos for g in gc.split(":") if g!=bpg]
        partner_gene_dict[bpg]["low"].update(low_bmi_partners)
        high_bmi_partners = [g for gc in bpg_df.loc[bpg_df.Phenotype=="high_bmi"].gene_combos for g in gc.split(":") if g!=bpg]
        partner_gene_dict[bpg]["high"].update(high_bmi_partners)
    partner_genes_high_bmi = sorted(set(sum([list(partner_gene_dict[g]["high"]) for g in partner_gene_dict.keys()], [])))
    partner_genes_low_bmi = sorted(set(sum([list(partner_gene_dict[g]["low"]) for g in partner_gene_dict.keys()], [])))
    both_pheno_genes_file = os.path.join(save_dir, "both_pheno.txt")
    with open(both_pheno_genes_file, "w") as f:
        for g in both_pheno_genes:
            f.write(f"{g}\n")
    pg_high_bmi_file = os.path.join(save_dir, "high_bmi.txt")
    with open(pg_high_bmi_file, "w") as f:
        for pg in partner_genes_high_bmi:
            f.write(f"{pg}\n")
    pg_low_bmi_file = os.path.join(save_dir, "low_bmi.txt")
    with open(pg_low_bmi_file, "w") as f:
        for pg in partner_genes_low_bmi:
            f.write(f"{pg}\n")
    return


if __name__ == "__main__":
    combinations2_file = "/data5/UK_Biobank/bmi_project/combinations/all_combinations/for_manuscript/combos_of_length_2.csv"
    combinations3_file = "/data5/UK_Biobank/bmi_project/combinations/all_combinations/for_manuscript/combos_of_length_3.csv"
    save_dir = "/data5/deepro/ukbiobank/analysis/bmi_project/bmi_genes_enrichment/data/partner_genes"
    save_partner_genes(combinations2_file, combinations3_file, save_dir)
