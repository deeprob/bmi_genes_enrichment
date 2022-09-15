import os
import utils as ut


def main(gene_file, save_dir):
    kegg_results_out = os.path.join(save_dir, "kegg_enrich_high_bmi.csv")
    gsea_results_out = os.path.join(save_dir, "gsea_enrich_high_bmi.csv")
    ut.run_kegg_enrichment(gene_file, kegg_results_out)
    ut.run_gsea_enrichment(gene_file, gsea_results_out)
    return


if __name__ == "__main__":
    gene_file = "/data5/deepro/ukbiobank/analysis/bmi_project/bmi_genes_enrichment/data/bmi_genes_lifestyle_regressed_out/high_bmi.txt"
    save_dir = "/data5/deepro/ukbiobank/analysis/bmi_project/bmi_genes_enrichment/data/bmi_genes_lifestyle_regressed_out"
    main(gene_file, save_dir)
