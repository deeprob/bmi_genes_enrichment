import utils as ut


def main(
    mgi_raw,
    mgi_store,
    gtf_file,
    store_file
    ):
    # mgi
    mgi_genes = ut.parse_mgi_genes(mgi_raw, mgi_store, gtf_file)
    # external intersect all
    ut.create_external_geneset([mgi_genes], store_file)
    return


if __name__ == "__main__":
    mgi_raw_file = "/data5/deepro/ukbiobank/analysis/bmi_genes_enrichment/data/external_genes/bmi/raw_data/mgi_bmi_obesity_genes.txt"
    mgi_store_file = "/data5/deepro/ukbiobank/analysis/bmi_genes_enrichment/data/external_genes/bmi/mgi_285.txt"
    gtf_file = "/data5/deepro/ukbiobank/analysis/bmi_genes_enrichment/data/gencode.v39.annotation.gtf.gz"
    store_file = "/data5/deepro/ukbiobank/analysis/bmi_genes_enrichment/data/external_genes/bmi/all_externals.txt"

    main(
        mgi_raw_file,
        mgi_store_file,
        gtf_file,
        store_file
        )
