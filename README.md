# Israeli Transportation Data Lakehouse

## Project Overview

This project implements an end-to-end data engineering pipeline in Databricks using public transportation datasets from data.gov.il.

The system follows a Medallion Architecture (Bronze → Silver → Gold) to ingest, clean, and model the data into analytics-ready tables.

---

## Architecture

### Data Flow

The pipeline is structured into three layers:

### Bronze
- Raw ingestion from Ministry of Transport APIs (REST / CSV format)
- Data stored as-is in Delta tables

### Silver
- Data cleaning and normalization
- Type casting and schema standardization
- Deduplication and validation
- Business key consistency checks

### Gold
- Dimensional modeling using Star Schema
- Fact and Dimension tables
- Referential integrity validation
- Foreign key match rate validation (100%)


![Data Flow Diagram](docs/diagrams/DATA%20FLOW%20DIAGRAM1.drawio.png)

---

## Data Modeling

### Star Schema Overview

### Private Vehicles

![Private Vehicles Star Schema](docs/diagrams/NAME1.png)

### Public Vehicles

![Public Vehicles Star Schema](docs/diagrams/NAME2.png)

### Motorcycles

![Motorcycles Star Schema](docs/diagrams/NAME3.png)

### EV Aggregation

![EV Star Schema](docs/diagrams/NAME4.png)


### Fact Tables
- `fact_private_vehicles`
- `fact_public_vehicles`
- `fact_motorcycles`
- `fact_ev_counts_by_area`

### Dimension Tables
- `dim_manufacturer`
- `dim_vehicle_type`
- `dim_fuel_type`
- `dim_color`
- `dim_ownership`

Each fact table enforces a defined grain and was validated using:
- Row count vs distinct business key checks
- Foreign key match rate validation
- Duplicate detection and fan-out join resolution


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

## Orchestration

The pipeline is orchestrated using Databricks Jobs with task dependencies between Bronze, Silver, and Gold layers.

---

## Future Improvements

- Implement Slowly Changing Dimensions (SCD)
- Add automated data quality monitoring
- Build BI dashboard (Power BI / Tableau)
