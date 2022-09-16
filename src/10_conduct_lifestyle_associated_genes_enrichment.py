import os
import utils as ut


def main(proj_dir, lofs, store_dir):
    for lof in lofs:
        gene_in = os.path.join(proj_dir, f"{lof}", "genelist.txt")
        results_dir = os.path.join(store_dir, lof)
        os.makedirs(results_dir,  exist_ok=True)
        kegg_results_out = os.path.join(results_dir, f"kegg_enrich.csv")
        gsea_results_out = os.path.join(results_dir, f"gsea_enrich.csv")
        ut.run_kegg_enrichment(gene_in, kegg_results_out)
        ut.run_gsea_enrichment(gene_in, gsea_results_out)
    return


if __name__ == "__main__":
    lofs = ["diet", "physical_activity", "mental_health"]
    proj_dir = "/data5/deepro/ukbiobank/analysis/bmi_project/bmi_genes_enrichment/data/bmi_genes_with_lifestyle"
    store_dir = "/data5/deepro/ukbiobank/analysis/bmi_project/bmi_genes_enrichment/data/bmi_genes_with_lifestyle"
    main(proj_dir, lofs, store_dir)
