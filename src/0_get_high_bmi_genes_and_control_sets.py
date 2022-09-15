import os
import utils as ut


def main(gtf_file, files, combos, groups, phenos, proj_dir):
    for pheno in phenos:
        for group in groups:
            gene_set = set()
            for file, combo in zip(files, combos):
                genes = ut.get_genes_from_combinations(file, combo, group, pheno)
                gene_set.update(genes)
            save_dir = os.path.join(proj_dir, pheno, group)
            os.makedirs(save_dir, exist_ok=True)
            with open(os.path.join(save_dir, "genelist.txt"), "w") as f:
                for g in gene_set:
                    f.write(f"{g}\n")
            control_store_file = os.path.join(save_dir, "controls.txt")
            ut.create_control_gene_set(gtf_file, gene_set, control_store_file)
    return


if  __name__ == "__main__":
    gtf_file = "/data5/UK_Biobank/bmi_project/annotations/gencode_genes/gencode.v39.parsed.genes.csv"
    combinations2_file = "/data5/UK_Biobank/bmi_project/combinations/all_combinations/for_manuscript/combos_of_length_2.csv"
    combinations3_file = "/data5/UK_Biobank/bmi_project/combinations/all_combinations/for_manuscript/combos_of_length_3.csv"
    proj_dir = "/data5/deepro/ukbiobank/analysis/bmi_genes_enrichment/data/bmi_genes/"
    combo_files = [combinations2_file, combinations3_file]
    combos = [2, 3]
    groups = ["white_british", "white_british_male", "white_british_female", "post_menopause", "pre_menopause"]
    phenos = ["high_bmi", "low_bmi"]
    main(gtf_file, combo_files, combos, groups, phenos, proj_dir)
