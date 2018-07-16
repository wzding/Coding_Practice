# put raw file into destination folder
# 3 typs of raw files : part, idpd, and demand
from pyspark.sql import SparkSession
import argparse
import time

parser = argparse.ArgumentParser()
parser.add_argument("--parent_path",
                    default="hdfs://int-ambari01.escm.co:8020",
                    help="hdfs parent path")
parser.add_argument("--hdfs_path",
                    default="/data/datalake/flex/feed/TRIGGER/",
                    help="hdfs path")
parser.add_argument("--file_dir",
                    default="Part_Elem_20180509.csv",
                    help="PART file path")
parser.add_argument("--file_type",
                    default="part",
                    help="file type, can be part, idpd, or demand")

args = parser.parse_args()
__parent_path__ = args.parent_path
hdfs_path = __parent_path__ + args.hdfs_path
file_dir = args.file_dir
file_type = args.file_type


def main():
    if file_type == "part":
        dst_path = "PART/SNAPSHOT/"
    elif file_type == "idpd":
        dst_path = "INDEPENDENT_DEMAND/SNAPSHOT/"
    elif file_type == "demand":
        dst_path = "DEMAND/SNAPSHOT/"
    else:
        raise ValueError("error with file type")

    spark = SparkSession.builder.appName("process_raw_files").getOrCreate()
    filename = file_dir.split('_')[-1].split('.')[0]
    df = spark.read.csv(hdfs_path + file_dir, header=True)
    df.write.mode('overwrite').csv(hdfs_path + dst_path + filename, header=True)
    return

if __name__ == "__main__":
    main()
