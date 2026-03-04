import pandas as pd
import logging

def clean_data(file_path: str):
    logging.info("Reading CSV file...")
    df = pd.read_csv(file_path)

    original_rows = len(df)

    # Remove duplicates
    df = df.drop_duplicates(subset="order_id")

    # Drop rows with null quantity or unit_price
    df = df.dropna(subset=["quantity", "unit_price"])

    # Replace null countries
    df["country"] = df["country"].fillna("Unknown")

    # Standardize country names
    df["country"] = df["country"].replace({
        "USA": "United States",
        "U.S.": "United States"
    })

    # Remove invalid values
    df = df[(df["quantity"] > 0) & (df["unit_price"] > 0)]

    # Create total_amount column
    df["total_amount"] = df["quantity"] * df["unit_price"]

    cleaned_rows = len(df)

    quality_report = {
        "original_rows": original_rows,
        "cleaned_rows": cleaned_rows,
        "removed_rows": original_rows - cleaned_rows,
        "removal_percentage": round(
            ((original_rows - cleaned_rows) / original_rows) * 100, 2
        ) if original_rows > 0 else 0
    }

    logging.info("Data cleaning completed.")

    return df, quality_report