import logging

def export_cleaned_data(df, path: str):
    logging.info("Exporting cleaned dataset...")
    df.to_csv(path, index=False)

def export_summary(metrics: dict, quality_report: dict, path: str):
    logging.info("Exporting summary report...")

    with open(path, "w") as f:
        f.write("=== DATA QUALITY REPORT ===\n")
        for key, value in quality_report.items():
            f.write(f"{key}: {value}\n")

        f.write("\n=== BUSINESS METRICS ===\n")
        for key, value in metrics.items():
            f.write(f"{key}: {value}\n")