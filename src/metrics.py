import pandas as pd
import logging

def generate_metrics(df: pd.DataFrame):
    logging.info("Generating business metrics...")

    total_revenue = df["total_amount"].sum()

    revenue_by_country = (
        df.groupby("country")["total_amount"]
        .sum()
        .sort_values(ascending=False)
        .to_dict()
    )

    top_products = (
        df.groupby("product")["total_amount"]
        .sum()
        .sort_values(ascending=False)
        .head(5)
        .to_dict()
    )

    metrics = {
        "total_revenue": round(total_revenue, 2),
        "revenue_by_country": revenue_by_country,
        "top_5_products": top_products,
        "valid_transactions": len(df)
    }

    logging.info("Metrics generation completed.")

    return metrics