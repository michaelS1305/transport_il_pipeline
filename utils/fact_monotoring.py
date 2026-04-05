from pyspark.sql.types import (
    StructType, StructField, StringType, TimestampType,
    IntegerType, DoubleType
)
from datetime import datetime
import uuid

def pipeline_run(
    spark,
    dataset_name,
    layer,
    missing_keys,
    duplication_check,
    key_null_ratio,
):

    schema = StructType([
        StructField("run_id", StringType(), False),
        StructField("dataset_name", StringType(), False),
        StructField("layer", StringType(), False),
        StructField("missing_keys", StringType(), False),
        StructField("duplication_check", StringType(), False),
        StructField("key_null_ratio", StringType(), False)
    ])

    data = [(
        str(uuid.uuid4()),
        dataset_name,
        layer,
        missing_keys,
        duplication_check,
        key_null_ratio,
    )]

    spark.createDataFrame(data, schema=schema) \
        .write.format("delta") \
        .mode("append") \
        .saveAsTable("transport_lakehouse.gold.pipeline_fact_monitoring")