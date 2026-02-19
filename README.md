# Israeli Transportation Data Lakehouse

## Project Overview

This project implements an end-to-end data engineering pipeline in Databricks using public transportation datasets from data.gov.il.

The system follows a Medallion Architecture (Bronze → Silver → Gold) to ingest, clean, and model the data into analytics-ready tables.

---

## Architecture

### Data Flow

<!-- Data Flow Diagram will be inserted here -->

---

## Data Modeling

### Star Schema Overview

<!-- Star Schema Diagram will be inserted here -->

---

## Data Quality & Validation

- Grain validation (COUNT vs DISTINCT checks)
- Fan-out join detection and resolution
- Natural key uniqueness enforcement
- Foreign key match rate validation

---

## Technologies Used

- Databricks
- PySpark
- SQL
- Delta Lake
- REST API
