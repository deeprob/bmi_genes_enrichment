import utils as ut


def main(
    clinvar_raw,
    rarev_raw,
    mgi_raw,
    twas_raw,
    clinvar_store,
    rarev_store,
    mgi_store,
    twas_store,
    gtf_file,
    store_file
    ):
    # rarev
    rarev_genes = ut.parse_rarev_genes(rarev_raw, rarev_store, gtf_file)
    # mgi
    mgi_genes = ut.parse_mgi_genes(mgi_raw, mgi_store, gtf_file)
    # twas
    twas_genes = ut.parse_twas_genes(twas_raw, twas_store)
    # external intersect all
    ut.create_external_geneset([rarev_genes, mgi_genes, twas_genes], store_file)
    return


if __name__ == "__main__":
    clinvar_raw_file = "/data5/deepro/ukbiobank/analysis/bmi_genes_enrichment/data/external_genes/lipid/raw_data/mmc2.xlsx"
    clinvar_store_file = "/data5/deepro/ukbiobank/analysis/bmi_genes_enrichment/data/external_genes/lipid/clinvar_35.txt"
    rarev_raw_file = "/data5/deepro/ukbiobank/analysis/bmi_genes_enrichment/data/external_genes/lipid/raw_data/hindy_et_al_ajhg_2022.txt"
    rarev_store_file = "/data5/deepro/ukbiobank/analysis/bmi_genes_enrichment/data/external_genes/lipid/rare_35.txt"
    mgi_raw_file = "/data5/deepro/ukbiobank/analysis/bmi_genes_enrichment/data/external_genes/lipid/raw_data/cholesterol_and_lipidemia_genes.txt"
    mgi_store_file = "/data5/deepro/ukbiobank/analysis/bmi_genes_enrichment/data/external_genes/lipid/mgi_1115.txt"
    twas_raw_file = "/data5/deepro/ukbiobank/analysis/bmi_genes_enrichment/data/external_genes/lipid/raw_data/mmc2.xlsx"
    twas_store_file = "/data5/deepro/ukbiobank/analysis/bmi_genes_enrichment/data/external_genes/lipid/twas_4008.txt"
    gtf_file = "/data5/deepro/ukbiobank/analysis/bmi_genes_enrichment/data/gencode.v39.annotation.gtf.gz"
    store_file = "/data5/deepro/ukbiobank/analysis/bmi_genes_enrichment/data/external_genes/lipid/all_externals.txt"

    main(
        clinvar_raw_file,
        rarev_raw_file,
        mgi_raw_file,
        twas_raw_file,
        clinvar_store_file,
        rarev_store_file,
        mgi_store_file,
        twas_store_file,
        gtf_file,
        store_file
        )
