import logging
from cleaner import clean_data
from metrics import generate_metrics
from exporter import export_cleaned_data, export_summary

def setup_logging():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s"
    )

def main():
    setup_logging()
    logging.info("Starting Data Quality Automation Pipeline")

    input_path = "data/sales_data.csv"
    output_cleaned_path = "output/cleaned_data.csv"
    output_summary_path = "output/summary_report.txt"

    df_cleaned, quality_report = clean_data(input_path)

    metrics = generate_metrics(df_cleaned)

    export_cleaned_data(df_cleaned, output_cleaned_path)
    export_summary(metrics, quality_report, output_summary_path)

    logging.info("Pipeline completed successfully.")

if __name__ == "__main__":
    main()