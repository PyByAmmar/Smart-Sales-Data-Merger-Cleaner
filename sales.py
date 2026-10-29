from glob import glob
import pandas as pd

all_files = glob("sale_*.csv")


if not all_files:
    print("No matching files found for merging!")
else:

    df_list = [pd.read_csv(file, encoding="cp1256", on_bad_lines="skip") for file in all_files]
    cobined_df = pd.concat(df_list, ignore_index=True)


    cobined_df["date"] = pd.to_datetime(
        cobined_df["date"], format="%Y.%m.%d", errors="coerce"
    )

    combined_df = cobined_df.dropna(subset=["date", "amount"])

    cobined_df["Month"] = cobined_df["date"].dt.to_period("M")
    final_report = (
        cobined_df.groupby("Month")["amount"].sum().reset_index()
    )



    final_report.to_excel("safe_sales_report.xlsx", index=False)
    print("The date has been processed and report generated successfully without any errors!")