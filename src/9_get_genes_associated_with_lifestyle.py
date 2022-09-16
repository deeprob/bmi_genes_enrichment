import os
import pandas as pd


def save_genes_associated_with_lifestyle(combo2_file, combo3_file, save_dir, lofs=["diet", "physical_activity", "mental_health"]):
    # read the combo file
    combinations2_df = pd.read_csv(combo2_file, low_memory=False)
    combinations3_df = pd.read_csv(combo3_file, low_memory=False)
    # filter for the lifestyle of interest
    for lof in lofs:
        lof2_df = combinations2_df.loc[(combinations2_df.Item_1.str.contains(lof))|(combinations2_df.Item_2.str.contains(lof))]
        lof3_df = combinations3_df.loc[(combinations3_df.Item_1.str.contains(lof))|(combinations3_df.Item_2.str.contains(lof))|(combinations3_df.Item_3.str.contains(lof))]
        enriched_combos2 = set(lof2_df.loc[:, [f"Item_{c}" for c in range(1, 2+1)]].values.flatten())
        enriched_combos3 = set(lof3_df.loc[:, [f"Item_{c}" for c in range(1, 3+1)]].values.flatten())
        enriched_combos = enriched_combos2.union(enriched_combos3)
        enriched_genes = [c.replace("Input_", "") for c in enriched_combos if "_ENSG" in c]
        save_file = os.path.join(save_dir, lof, "genelist.txt")
        with open(save_file, "w") as f:
            for g in enriched_genes:
                f.write(f"{g}\n")
    return


if __name__ == "__main__":
    combo2_file = "/data5/deepro/ukbiobank/analysis/bmi_project/lifestyle_factors/data/results/tables/combo2_lf_gene.csv"
    combo3_file = "/data5/deepro/ukbiobank/analysis/bmi_project/lifestyle_factors/data/results/tables/combo3.csv"
    save_dir = "/data5/deepro/ukbiobank/analysis/bmi_project/bmi_genes_enrichment/data/bmi_genes_with_lifestyle"
    save_genes_associated_with_lifestyle(combo2_file, combo3_file, save_dir)
