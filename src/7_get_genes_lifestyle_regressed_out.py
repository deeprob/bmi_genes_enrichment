import os
import pandas as pd


def save_lifestyle_regressed_genes(combo2_file, combo3_file, save_dir):
    # read the combo file
    combinations2_df = pd.read_csv(combo2_file, low_memory=False)
    combinations3_df = pd.read_csv(combo3_file, low_memory=False)
    # filter for "high" phenotype and "joint" sex (both male and female)
    combinations2_df = combinations2_df.loc[(combinations2_df.Phenotype=="high")&(combinations2_df.Sex=="joint")]
    combinations3_df = combinations3_df.loc[(combinations3_df.Phenotype=="high")&(combinations3_df.Sex=="joint")]
    # get genes from combos
    combo2_genes = set([g for gc in zip(*[combinations2_df[f"Item_{i}"] for i in range(1, 2 + 1)]) for g in gc])
    combo3_genes = set([g for gc in zip(*[combinations3_df[f"Item_{i}"] for i in range(1, 3 + 1)]) for g in gc])
    combo_genes = combo2_genes.union(combo3_genes)
    save_file = os.path.join(save_dir, "high_bmi.txt")
    with open(save_file, "w") as f:
        for g in combo_genes:
            f.write(f"{g}\n")
    return 


if __name__ == "__main__":
    combo2_file = "/data5/UK_Biobank/bmi_project/combinations/white_british_regress_out_lifestyle/statistics/6_add_info/combos_length_2.csv"
    combo3_file = "/data5/UK_Biobank/bmi_project/combinations/white_british_regress_out_lifestyle/statistics/6_add_info/combos_length_3.csv"
    save_dir = "/data5/deepro/ukbiobank/analysis/bmi_project/bmi_genes_enrichment/data/bmi_genes_lifestyle_regressed_out"
    save_lifestyle_regressed_genes(combo2_file, combo3_file, save_dir)
