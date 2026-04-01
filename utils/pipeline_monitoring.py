from pyspark.sql.types import (
    StructType, StructField, StringType, TimestampType,
    IntegerType, DoubleType
)
from datetime import datetime
import uuid

def log_pipeline_run(
    spark,
    dataset_name,
    layer,
    run_start_time,
    run_end_time,
    status,
    rows_ingested = 0,
    error_message=None
):
    processing_time_sec = float((run_end_time - run_start_time).total_seconds())

    schema = StructType([
        StructField("run_id", StringType(), False),
        StructField("dataset_name", StringType(), False),
        StructField("layer", StringType(), False),
        StructField("run_start_time", TimestampType(), False),
        StructField("run_end_time", TimestampType(), False),
        StructField("status", StringType(), False),
        StructField("rows_ingested", IntegerType(), False),
        StructField("error_message", StringType(), True),
        StructField("created_at", TimestampType(), False)
    ])

    data = [(
        str(uuid.uuid4()),
        dataset_name,
        layer,
        run_start_time,
        run_end_time,
        status,
        rows_ingested,
        error_message,
        datetime.now()
    )]

    spark.createDataFrame(data, schema=schema) \
        .write.format("delta") \
        .mode("append") \
        .saveAsTable("transport_lakehouse.gold.pipeline_monitoring")