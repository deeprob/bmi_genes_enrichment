import os
import utils as ut


def main(proj_dir, phenos, groups, store_dir):
    for pheno in phenos:
        for group in groups:
            gene_in = os.path.join(proj_dir, pheno, group, "genelist.txt")
            results_dir = os.path.join(store_dir, pheno, group)
            os.makedirs(results_dir,  exist_ok=True)
            kegg_results_out = os.path.join(results_dir, "kegg_enrich.csv")
            gsea_results_out = os.path.join(results_dir, "gsea_enrich.csv")
            ut.run_kegg_enrichment(gene_in, kegg_results_out)
            ut.run_gsea_enrichment(gene_in, gsea_results_out)
    return


if __name__ == "__main__":
    groups = ["white_british", "white_british_male", "white_british_female", "post_menopause", "pre_menopause"]
    phenos = ["high_bmi", "low_bmi"]
    proj_dir = "/data5/deepro/ukbiobank/analysis/bmi_project/bmi_genes_enrichment/data/bmi_genes/"
    store_dir = "/data5/deepro/ukbiobank/analysis/bmi_project/bmi_genes_enrichment/data/kegg_results/"
    main(proj_dir, phenos, groups, store_dir)
