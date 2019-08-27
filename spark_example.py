#!/home/zkfr/.local/share/virtualenvs/xf-5EfV3Nly/bin/python
#-*- coding:utf-8 -*-
# @author : MaLei 
# @datetime : 2019-08-13 14:33
# @file : spark_example.py
# @software : PyCharm

# from pyspark import SparkContext
# sc = SparkContext( 'local', 'test')
# logFile = "file:///usr/local/spark/README.md"
# logData = sc.textFile(logFile, 2).cache()
# numAs = logData.filter(lambda line: 'a' in line).count()
# numBs = logData.filter(lambda line: 'b' in line).count()
# print('Lines with a: %s, Lines with b: %s' % (numAs, numBs))

# from pyspark import SparkContext
# sc = SparkContext( 'local', 'test')
# textFile = sc.textFile("file:///usr/local/spark/README.md")
# wordCount = textFile.flatMap(lambda line: line.split(" ")).map(lambda word: (word,1)).reduceByKey(lambda a, b : a + b)
# wordCount.foreach(print)

from pyspark import SparkContext,SparkConf
from pyspark.sql import SparkSession,Row
from pyspark.sql.functions import concat,date_format,lead,lag
from pyspark.sql.types import DataType,DateType,FloatType,IntegerType,DoubleType,DecimalType,TimestampType
import os
# from pyspark.ml.classification import DecisionTreeClassifier



file_paths=os.path.dirname(os.path.realpath(__file__))+'/tn_electric_history_all.csv'

# client=Client("http://server2:50070",root="/",session=False)
# client.upload("/tmp/test/",file_paths,cleanup=True)

# 读取文件
# sc=SparkContext('local','test')
# print(paths)
# files=sc.textFile('file://'+file_paths)
# files = sc.textFile("hdfs://192.168.1.108:9000/user/hadoop/tn_electric_history_all.csv")
# 从hdfs读取文件
files=SparkSession.builder.getOrCreate()
# files=files.read.csv("hdfs://192.168.1.108:9000/user/hadoop/tn_electric_history_all.csv",header=True)
files=files.read.csv("hdfs://192.168.1.108:9000/user/hadoop/tn_electric_history.csv",header=True)

# print(files.columns)

#节电控制
# new_df=files['dev_id','unit_id','dept_id','current','factor','current_power','leakage_value','electric_quantity','alarm_time']
# # new_df.show()
# new_df_2=new_df.withColumn('alarm_time',date_format(new_df.alarm_time, 'yyyy-MM-dd HH:00:00').cast(TimestampType()))\
#     .withColumn("electric_quantity", new_df["electric_quantity"].cast(FloatType()))\
#     .withColumn("leakage_value", new_df["leakage_value"].cast(IntegerType()))\
#     .withColumn("current_power", new_df["current_power"].cast(DoubleType()))\
#     .withColumn("factor", new_df["factor"].cast(DoubleType()))\
#     .withColumn("current", new_df["current"].cast(DoubleType()))\
#     .withColumn("dept_id", new_df["dept_id"].cast(IntegerType()))\
#     .withColumn("unit_id", new_df["unit_id"].cast(IntegerType()))
# new_df_2.show()
#
# # 按电量统计
# # 设备用电统计
# new_df_3=new_df_2.groupby('dev_id','dept_id','unit_id')
# dev_electric_quantity=new_df_3.max('electric_quantity')\
#     .withColumnRenamed("max(electric_quantity)","electric_quantity")\
#     .sort('electric_quantity',ascending=False)
# dev_electric_quantity.show()
#
# # 单位用电统计
# unit_electric_quantity=dev_electric_quantity.groupby('unit_id','dept_id')\
#     .sum('electric_quantity')\
#     .withColumnRenamed("sum(electric_quantity)","electric_quantity")
# unit_electric_quantity=unit_electric_quantity.withColumn("electric_quantity",
#                                                          unit_electric_quantity["electric_quantity"]
#                                                          .cast(DecimalType(20,2))).sort('electric_quantity',ascending=False)
# unit_electric_quantity.show()
#
# # 部门用电统计
# dept_electric_quantity=unit_electric_quantity.groupby('dept_id')\
#     .sum('electric_quantity')\
#     .withColumnRenamed("sum(electric_quantity)","electric_quantity")\
#     .sort('electric_quantity',ascending=False)
# dept_electric_quantity.show()
#
# # 按时间做分类
# new_df_4=new_df_2.groupby('dev_id','unit_id','dept_id','alarm_time')
#
# # 每小时设备最高消耗电量
# dev_hour_electric_quantity=new_df_4.max('electric_quantity')\
#     .withColumnRenamed("max(electric_quantity)","electric_quantity")\
#     .sort('alarm_time',ascending=False)
# dev_hour_electric_quantity.show()
#
# # 一个单位每小时消耗的电量
# unit_hour_electric_quantity=dev_hour_electric_quantity.groupby('unit_id','dept_id','alarm_time')\
#     .sum('electric_quantity')\
#     .withColumnRenamed("sum(electric_quantity)","electric_quantity")\
#     .sort('alarm_time',ascending=False)
# unit_hour_electric_quantity=unit_hour_electric_quantity.withColumn("electric_quantity",
#                                                          unit_hour_electric_quantity["electric_quantity"]
#                                                          .cast(DecimalType(20,2)))
# unit_hour_electric_quantity.show()
#
# #一个部门每小时耗电量
# dept_hour_electric_quantity=unit_hour_electric_quantity.groupby('dept_id','alarm_time')\
#     .sum('electric_quantity')\
#     .withColumnRenamed("sum(electric_quantity)","electric_quantity")\
#     .sort('alarm_time',ascending=False)
# dept_hour_electric_quantity.show()




# 用电安全
# 创建新的dataframe
new_df=files['dev_id','unit_id','dept_id','afci_information','line_overvoltage','line_undervoltage','line_overload','line_temperature','line_leakage','alarm_time']
# new_df.show()
new_df_2=new_df.withColumn('alarm_time',date_format(new_df.alarm_time, 'yyyy-MM-dd HH:00:00').cast(TimestampType()))
alarm_data=new_df_2.filter((new_df_2.afci_information==1)
                           |(new_df_2.line_overvoltage==1)
                           |(new_df_2.line_undervoltage==1)
                           |(new_df_2.line_overload==1)
                           |(new_df_2.line_temperature==1)
                           |(new_df_2.line_leakage==1))
alarm_data.show()
alarm_data.groupby('dev_id','unit_id','dept_id','afci_information','line_overvoltage',
                   'line_undervoltage','line_overload','line_temperature','line_leakage','alarm_time').count()\
    .sort('alarm_time')\
    .show()