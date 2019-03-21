# rename dirs, run after process_f_a.py
# do not need to provide timestamp
from pyspark.sql import SparkSession
import argparse
import subprocess

parser = argparse.ArgumentParser()
parser.add_argument("--parent_path",
                    default="hdfs://int-ambari01.escm.co:8020",
                    help="hdfs parent path")
parser.add_argument("--hdfs_path",
                    default="/data/datalake/flex/feed/TRIGGER/FORECAST_ACTUAL/SNAPSHOT/",
                    help="hdfs path")
parser.add_argument("--file_timestamp",
                    default="20180509",
                    help="timestamp of file")

args = parser.parse_args()
__parent_path__ = args.parent_path
hdfs_path = __parent_path__ + args.hdfs_path
file_timestamp = hdfs_path + args.file_timestamp

spark = SparkSession.builder.appName("rename_FORECAST_ACTUAL_file").getOrCreate()
hc = spark.sparkContext._jsc.hadoopConfiguration()
URI = spark.sparkContext._gateway.jvm.java.net.URI
Path = spark.sparkContext._gateway.jvm.org.apache.hadoop.fs.Path
FileSystem = spark.sparkContext._gateway.jvm.org.apache.hadoop.fs.FileSystem
fs = FileSystem.get(URI(__parent_path__), hc)


def get_files_in_dir(dir_in):
    """
    run linux commands
    """
    args = "hdfs dfs -ls " + dir_in + " | awk '{print $8}'"
    proc = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    s_output, s_err = proc.communicate()
    res = s_output.split()
    return [s.decode("utf-8") for s in res]


def main():
    dirs = get_files_in_dir(file_timestamp)
    print("src dirs: ", dirs)
    for src_dir in dirs:
        if ".csv" in src_dir:
            splits = src_dir.split("/")
            customer = splits[-7]
            day = splits[-2]
            part_num = splits[-1].split("-")[1]
            dst_dir = file_timestamp + "/" + customer + "_TRIGGER_FORECAST_ACTUAL_SNAPSHOT_" + day + "_" + part_num + ".csv"
            print("renaming destination dir", dst_dir)
            fs.rename(Path(src_dir), Path(dst_dir))
            print("renamed %s to %s" %(src_dir, dst_dir))
    return

if __name__ == "__main__":
    main()
