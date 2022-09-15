import os
import utils as ut


def main(proj_dir, external_dir, phenos, groups, external_types, store_dir):
    for pheno in phenos:
        for group in groups:
            for ext_type in external_types:
                gene_in = os.path.join(proj_dir, pheno, group, "genelist.txt")
                control_genes_file = os.path.join(proj_dir, pheno, group, "controls.txt")
                external_genes_file = os.path.join(external_dir, ext_type, "all_externals.txt")
                contingency_file = os.path.join(store_dir, ext_type, pheno, group, "external_contingency.csv")
                enrichment_file = os.path.join(store_dir, ext_type, pheno, group, "external_enrich.csv")
                results_dir = os.path.join(store_dir, ext_type, pheno, group)
                os.makedirs(results_dir,  exist_ok=True)
                ut.create_contingency_table(gene_in, control_genes_file, external_genes_file, contingency_file)
                ut.run_fishers_enrichment(contingency_file, enrichment_file)
    return


if __name__ == "__main__":
    groups = ["white_british", "white_british_male", "white_british_female", "post_menopause", "pre_menopause"]
    phenos = ["high_bmi", "low_bmi"]
    external_data_types = ["lipid", "bmi"]
    proj_dir = "/data5/deepro/ukbiobank/analysis/bmi_genes_enrichment/data/bmi_genes/"
    external_dir = "/data5/deepro/ukbiobank/analysis/bmi_genes_enrichment/data/external_genes/"
    store_dir = "/data5/deepro/ukbiobank/analysis/bmi_genes_enrichment/data/external_enrich_results"
    main(proj_dir, external_dir, phenos, groups, external_data_types, store_dir)
