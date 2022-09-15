library("biomaRt")
library("clusterProfiler")

gene_file = "/data5/deepro/ukbiobank/analysis/bmi_genes_enrichment/data/bmi_genes/high_bmi/white_british/genelist.txt"
out_file = "/data5/deepro/ukbiobank/analysis/bmi_genes_enrichment/data/kegg_results/high_bmi/white_british/pathway_figure.pdf"

# get the genes and store as a vector
genes = read.table(gene_file, header=FALSE)

# convert ensemble id to entrez id :: link: https://support.bioconductor.org/p/114325/
mart <- useMart("ensembl","hsapiens_gene_ensembl")
entrez_genes <- getBM(c("ensembl_gene_id", "entrezgene_id"), "ensembl_gene_id", genes, mart)

# use kegg for go term analysis :: link: http://yulab-smu.top/biomedical-knowledge-mining-book/clusterprofiler-kegg.html
kenrich = enrichKEGG(
    gene=entrez_genes[, 2],
    organism="hsa",
    pvalueCutoff=0.05,
    pAdjustMethod="BH"
)

browseKEGG(kenrich, 'hsa02010')
