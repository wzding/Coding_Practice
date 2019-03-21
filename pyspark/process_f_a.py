# 1. merge demand and actual
# 2. add data from master data
# 3. save to FORECAST_ACTUAL
from pyspark.sql import SparkSession
from pyspark.sql.functions import to_date, broadcast, col, when
from datetime import datetime
import argparse
import time

parser = argparse.ArgumentParser()
parser.add_argument("--parent_path",
                    default="hdfs://int-ambari01.escm.co:8020",
                    help="hdfs parent path")
parser.add_argument("--hdfs_path",
                    default="/data/datalake/flex/feed/TRIGGER/",
                    help="hdfs path")
parser.add_argument("--idpd_dir",
                    default="INDEPENDENT_DEMAND/SNAPSHOT/",
                    help="idpd file path")
parser.add_argument("--actual_data_dir",
                    default="SALES_ORDER_SHIPMENT/HISTORICAL/",
                    help="actual data file path")
parser.add_argument("--demand_dir",
                    default="DEMAND/SNAPSHOT/",
                    help="demand file path")
parser.add_argument("--master_data_dir",
                    default="PART/SNAPSHOT/",
                    help="master data path")
parser.add_argument("--f_a_data_dir",
                    default="FORECAST_ACTUAL/SNAPSHOT/",
                    help="forecast actual file path")
parser.add_argument("--timestamp",
                    default="20180511",
                    help="timestamp")

args = parser.parse_args()
__parent_path__ = args.parent_path
hdfs_path = __parent_path__ + args.hdfs_path
file_day = args.timestamp
# idpd data dir
idpd_dir = hdfs_path + args.idpd_dir + file_day
actual_data_dir = hdfs_path + args.actual_data_dir
demand_dir = hdfs_path + args.demand_dir + file_day
master_data_dir = hdfs_path + args.master_data_dir + file_day
f_a_data_dir = hdfs_path + args.f_a_data_dir + file_day


spark = SparkSession.builder.appName("process_forecast_actual").getOrCreate()
hc = spark.sparkContext._jsc.hadoopConfiguration()
URI = spark.sparkContext._gateway.jvm.java.net.URI
Path = spark.sparkContext._gateway.jvm.org.apache.hadoop.fs.Path
FileSystem = spark.sparkContext._gateway.jvm.org.apache.hadoop.fs.FileSystem
log4jLogger = spark.sparkContext._jvm.org.apache.log4j
logger = log4jLogger.LogManager.getLogger("process_forecast_actual")
fs = FileSystem.get(URI(__parent_path__), hc)


quarter = {"01": 1, "02": 1, "03": 1,
           "04": 2, "05": 2, "06": 2,
           "07": 3, "08": 3, "09": 3,
           "10": 4, "11": 4, "12": 4}
quarter_range = {1: "01-02-0331",
                 2: "04-05-0630",
                 3: "07-08-0930",
                 4: "10-11-1231" }

def read_csv(dirs):
    return spark.read.csv(dirs, header=True)


def get_string_value(year, month):
    [month1, month2, month3] = month
    return year + month1 + "-" + year + month2 + "-" + year + month3


def get_quarters(current_day):
    year = current_day[:4]
    month = current_day[4:6]
    qrt = quarter[month]

    last_year = year
    next_year = year

    lq = qrt - 1
    nq = qrt + 1
    if qrt == 1:
        lq = 4
        last_year = str(int(year) - 1)
    elif qrt == 4:
        nq = 1
        next_year = str(int(year) + 1)

    last_q = get_string_value(last_year, quarter_range[lq].split("-"))
    crrt_q = get_string_value(year, quarter_range[qrt].split("-"))
    next_q = get_string_value(next_year, quarter_range[nq].split("-"))
    return last_q, crrt_q, next_q


def convert_timestamp(df):
    df = df.withColumn("Due Date", to_date(df['Due Date'], 'yyyy-MM-dd'))
    return df


def fix_col_name(df):
    # fix columns with dot
    for column in df.columns:
        df = df.withColumnRenamed(column, column.replace(".", " "))
    return df


def get_crrt_month_path(crrt_q):
    path = []
    for i in crrt_q.split("-"):
        if file_day[:6] in i: # 201805
            break
        path.append(i)
    return path #['201804', '201805']


def get_df_from_dir_list(paths):
    # logger.info("Trying to read actuals from: ", paths)
    exist_path = []
    for p in paths:
        if fs.exists(Path(p)):
            exist_path.append(p)
    # logger.info("Reading actuals from: ", exist_path)
    df = spark.read.format("csv").option("header", "true").\
         option('mode', 'DROPMALFORMED').\
         load(exist_path)
    return df


def select_cols(df, type):
    if type == "master":
        df = df.select(col("Name").alias("Part Name"),
                       col("Site").alias("Part Site")
                       col('Leadtime Date'),
                       col('Description'),
                       col('Primary Supply Type Source'),
                       col('Std Unit Cost'),
                       col('Item Group Desc'),
                       col('Product Line'),
                       col('Product Line Description'),
                       col('ABC Code'),
                       col('Inventory Unit'),
                       col('Dep Demand forecast consumption'))
    if type == "idpd":
        df = df.select(col("Order Type"),
                       col("Order Site").alias("Part Site"),
                       col("Part Name"),
                       col("Due Date"),
                       col("Q_new").alias('Quantity'),
                       col("Global Cust Name"))
    if type == "demand":
        df = df.select(col("Type").alias("Order Type"),
                       col("Part Site"),
                       col("Part").alias("Part Name"),
                       col("Due Date"),
                       col("Remaining Quantity").alias('Quantity'),
                       col("Global Cust Name"))
    if type == "actual":
        df = df.select(col("Category").alias("Order Type"),
                       col("Part Site"),
                       col("Part Name"),
                       col("Date").alias("Due Date"),
                       col("Quantity"),
                       col("Global Cust Name"))
    return df


def main():
    t = time.time()
    current_day = datetime.strptime(file_day, '%Y%m%d')
    # get quarters
    last_q, crrt_q, next_q = get_quarters(file_day)
    # ------------------------FORCAST------------------------
    # read demand data - last week to end of next quarter
    df = read_csv(idpd_dir)
    # convert data type
    df = convert_timestamp(df)
    # filter data after end day
    end_day = next_q.split('-')[-1]  # "20180930"
    df = df.filter(df['Due Date'] <= datetime.strptime(end_day, '%Y%m%d'))
    # actual --> use Shipped Qty ; forcast --> use Effective Demand
    df = df.withColumn('Q_new',
                        when(df["Due Date"] <= current_day,
                        df["Shipped Qty"]).otherwise(df["Effective Demand"]))\
           .drop(df.Quantity)
    df = select_cols(df, "idpd")
    # ------------------------ACTUAL------------------------
    # read actual data - last and current quarter
    last_q_path = [actual_data_dir + 'year=' + i[:4] + '/month=' + i[4:6]
                   for i in last_q.split("-")]
    crrt_q_path = [actual_data_dir + 'year=' + i[:4] + '/month=' + i[4:6]
                   for i in get_crrt_month_path(crrt_q)]
    # logger.info("Actual data paths: ", last_q_path + crrt_q_path)
    actual_df = get_df_from_dir_list(last_q_path + crrt_q_path)
    actual_df.persist()
    actual_df = fix_col_name(actual_df)
    actual_df = select_cols(actual_df, "actual")
    # filter data after min date, typically last week - make sure no overlap data
    min_date = df.agg({"Due Date": "min"}).collect()[0]["min(Due Date)"]
    actual_df = convert_timestamp(actual_df)
    actual_df = actual_df.filter(actual_df['Due Date'] < min_date)
    # merge actual with demand
    merged_df = df.union(actual_df)
    # ------------------------MASTER DATA------------------------
    # Dep Demand forecast consumption == Yes
    master_df = read_csv(master_data_dir)
    # column W
    master_4_demand = master_df.filter(master_df['Dep Demand forecast consumption'] == 'Yes')
    master_4_demand = select_cols(master_4_demand, "master")
    master_df = select_cols(master_df, "master")
    # ------------------------DEMAND DATA------------------------
    ### selet master data with "Yes" Dep Demand forecast consumption
    demand_df = read_csv(demand_dir)
    demand_df = select_cols(demand_df, "demand")
    demand_master = master_4_demand.join(broadcast(demand_df), ["Part Name", "Part Site"], 'inner')
    # ------------------------MERGING------------------------
    final = merged_df.join(broadcast(master_df), ["Part Name", "Part Site"], "left_outer")
    final = final.union(demand_master)
    # write file
    final.write.format('com.databricks.spark.csv') \
               .mode('overwrite') \
               .option("header", 'true') \
               .option("delimiter", "|") \
               .option("mode", "DROPMALFORMED") \
               .save(f_a_data_dir)
    # final.write.csv(demand_data_dir, header=True)
    t2 = time.time()
    # logger.info(round((t2-t)/60, 2), ' minutes to create demand')
    return


if __name__ == "__main__":
    main()
