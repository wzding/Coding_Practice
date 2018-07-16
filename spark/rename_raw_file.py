# rename files in  folder
# 3 typs of raw files : part, idpd, and demand
from pyspark.sql import SparkSession
import argparse
import subprocess

parser = argparse.ArgumentParser()
parser.add_argument("--parent_path",
                    default="hdfs://int-ambari01.escm.co:8020",
                    help="hdfs parent path")
parser.add_argument("--hdfs_path",
                    default="/data/datalake/flex/feed/TRIGGER/",
                    help="hdfs path")
parser.add_argument("--file_timestamp",
                    default="20180509",
                    help="timestamp of file")
parser.add_argument("--file_type",
                    default="part",
                    help="file type, can be part, idpd, or demand")

args = parser.parse_args()
__parent_path__ = args.parent_path
hdfs_path = __parent_path__ + args.hdfs_path

spark = SparkSession.builder.appName("rename_PART_file").getOrCreate()
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
    file_type = args.file_type
    if file_type == "part":
        src_path = "PART/SNAPSHOT/"
        dst_path = "_TRIGGER_PART_SNAPSHOT_"
    elif file_type == "idpd":
        src_path = "INDEPENDENT_DEMAND/SNAPSHOT/"
        dst_path = "_TRIGGER_INDEPENDENT_DEMAND_SNAPSHOT_"
    elif file_type == "demand":
        src_path = "DEMAND/SNAPSHOT/"
        dst_path = "_TRIGGER_DEMAND_SNAPSHOT_"
    else:
        raise ValueError("error with file type")
    file_timestamp = hdfs_path + src_path + args.file_timestamp

    dirs = get_files_in_dir(file_timestamp)
    print("src dirs: ", dirs)
    #['hdfs://int-ambari01.escm.co:8020/data/datalake/flex/feed/TRIGGER/PART/SNAPSHOT/20180509/part-00007-ea606ea8-cb4a-42d9-a7fa-d5c438f36a0c-c000.csv',
 #'hdfs://int-ambari01.escm.co:8020/data/datalake/flex/feed/TRIGGER/PART/SNAPSHOT/20180509/part-00008-ea606ea8-cb4a-42d9-a7fa-d5c438f36a0c-c000.csv']
    for src_dir in dirs:
        if ".csv" in src_dir:
            splits = src_dir.split("/")
            customer = splits[-7]
            day = splits[-2]
            part_num = splits[-1].split("-")[1]
            dst_dir = file_timestamp + "/" + customer + dst_path + day + "_" + part_num + ".csv"
            print("renaming destination dir", dst_dir)
            fs.rename(Path(src_dir), Path(dst_dir))
            print("renamed %s to %s" %(src_dir, dst_dir))
    return

if __name__ == "__main__":
    main()
