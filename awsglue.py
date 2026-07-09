import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from pyspark.sql.functions import col, when, round, to_date, year, month

args = getResolvedOptions(sys.argv, ["JOB_NAME", "OUTPUT_PATH"])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args["JOB_NAME"], args)

# Read from Glue Catalog tables created by crawler or Athena DDL.
loans = spark.table("mortgage_lending_raw_db.loan_applications")
applicants = spark.table("mortgage_lending_raw_db.applicants")
properties = spark.table("mortgage_lending_raw_db.properties")

# Join mortgage application data.
df = (
    loans
    .join(applicants, "applicant_id", "left")
    .join(properties, "property_id", "left")
)

# Transform and add business fields.
df_clean = (
    df
    .withColumn("application_dt", to_date(col("application_date")))
    .withColumn("application_year", year(col("application_dt")))
    .withColumn("application_month", month(col("application_dt")))
    .withColumn("loan_to_value_ratio", round(col("loan_amount") / col("property_value"), 2))
    .withColumn(
        "credit_risk_bucket",
        when(col("credit_score") >= 740, "Low Risk")
        .when(col("credit_score") >= 660, "Medium Risk")
        .otherwise("High Risk")
    )
    .withColumn(
        "income_bucket",
        when(col("annual_income") >= 100000, "High Income")
        .when(col("annual_income") >= 65000, "Medium Income")
        .otherwise("Low Income")
    )
)

# Write curated data as Parquet partitioned by year/month.
(
    df_clean
    .write
    .mode("overwrite")
    .partitionBy("application_year", "application_month")
    .parquet(args["OUTPUT_PATH"])
)

job.commit()