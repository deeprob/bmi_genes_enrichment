import os
import utils as ut


def main(proj_dir, phenos, store_dir):
    for pheno in phenos:
        gene_in = os.path.join(proj_dir, f"{pheno}.txt")
        results_dir = os.path.join(store_dir, pheno)
        os.makedirs(results_dir,  exist_ok=True)
        kegg_results_out = os.path.join(results_dir, f"kegg_enrich_{pheno}.csv")
        gsea_results_out = os.path.join(results_dir, f"gsea_enrich_{pheno}.csv")
        ut.run_kegg_enrichment(gene_in, kegg_results_out)
        ut.run_gsea_enrichment(gene_in, gsea_results_out)
    return


if __name__ == "__main__":
    phenos = ["high_bmi", "low_bmi", "both_pheno"]
    proj_dir = "/data5/deepro/ukbiobank/analysis/bmi_project/bmi_genes_enrichment/data/partner_genes"
    store_dir = "/data5/deepro/ukbiobank/analysis/bmi_project/bmi_genes_enrichment/data/partner_enrich_results"
    main(proj_dir, phenos, store_dir)
