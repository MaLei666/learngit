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
from pyspark.sql.functions import concat,date_format,lead,lag,add_months,hour
from pyspark.sql.types import DataType,DateType,FloatType,IntegerType,DoubleType,DecimalType,TimestampType,StringType
import os
# from pyspark.ml.classification import DecisionTreeClassifier



# file_paths=os.path.dirname(os.path.realpath(__file__))+'/tn_electric_history_all.csv'

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

# #节电控制
# new_df=files['dev_id','unit_id','dept_id','current','factor','current_power','leakage_value','electric_quantity','alarm_time']
# # new_df.show()
# new_df_2=new_df.withColumn('alarm_time',date_format(new_df.alarm_time, 'yyyy-MM-dd HH').cast(TimestampType()))\
#     .withColumn("electric_quantity", new_df["electric_quantity"].cast(FloatType()))\
#     .withColumn("leakage_value", new_df["leakage_value"].cast(IntegerType()))\
#     .withColumn("current_power", new_df["current_power"].cast(DoubleType()))\
#     .withColumn("factor", new_df["factor"].cast(DoubleType()))\
#     .withColumn("current", new_df["current"].cast(DoubleType()))\
#     .withColumn("dept_id", new_df["dept_id"].cast(IntegerType()))\
#     .withColumn("unit_id", new_df["unit_id"].cast(IntegerType()))
# new_df_2.show()
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
# # 增量
# # 每个设备每日电量增量
# new_df_3=new_df_2.withColumn('alarm_time',date_format(new_df_2.alarm_time, 'yyyy-MM-dd').cast(TimestampType()))\
#     .groupby('dev_id','unit_id','dept_id','alarm_time')
# mindata=new_df_3.min('electric_quantity')\
#     .withColumnRenamed('alarm_time','now_alarm_time')\
#     .withColumnRenamed('dev_id','dev_id2')
# maxdata=new_df_3.max('electric_quantity')
# new_df_4=maxdata.join(mindata['dev_id2','now_alarm_time','min(electric_quantity)'],
#                       (maxdata.dev_id==mindata.dev_id2)&(maxdata.alarm_time==mindata.now_alarm_time)
#                       ,'left_outer').drop('dev_id2','now_alarm_time')
# dev_day_elec_incre=new_df_4.withColumn('increment',(new_df_4['max(electric_quantity)']-new_df_4['min(electric_quantity)']).cast(DecimalType(20,2)))
# # print(new_df_5.dtypes)
# dev_day_elec_incre.show()
# # 单位每日耗电增量
# # unit_day_elec_incre=dev_day_elec_incre.groupby('unit_id','dept_id','alarm_time')\
# #     .sum('increment')\
# #     .withColumnRenamed('sum(increment)','increment')\
# #     .sort('increment',ascending=False)
# # unit_day_elec_incre.show()
#
# # 部门每日耗电增量
# # dept_day_elec_incre=unit_day_elec_incre.groupby('dept_id','alarm_time')\
# #     .sum('increment')\
# #     .withColumnRenamed('sum(increment)','increment')\
# #     .sort('increment',ascending=False)
# # dept_day_elec_incre.show()
#
# # 设备对比上个月的耗电量
# pre_dev_day_elec_incre=dev_day_elec_incre['increment','unit_id','alarm_time']\
#     .withColumn('alarm_time',add_months(dev_day_elec_incre.alarm_time,-1).cast(TimestampType()))\
#     .withColumnRenamed('unit_id','unit_id1')\
#     .withColumnRenamed('alarm_time','pre_alarm_time')\
#     .withColumnRenamed('increment','pre_increment')\
#
# comp_dev_day_elec_incre=dev_day_elec_incre.join(pre_dev_day_elec_incre['pre_increment','unit_id1','pre_alarm_time'],
#          (pre_dev_day_elec_incre.unit_id1 == dev_day_elec_incre.unit_id) & (pre_dev_day_elec_incre.pre_alarm_time == dev_day_elec_incre.alarm_time)
#          , 'left_outer')\
#     .drop('unit_id1','pre_alarm_time')\
#     .fillna(0,subset=['pre_increment'])
#
# comp_dev_day_elec_incre=comp_dev_day_elec_incre.withColumn('diff_increment',
#                                                              (comp_dev_day_elec_incre['increment']-comp_dev_day_elec_incre['pre_increment']))
# comp_dev_day_elec_incre.show()

# 用电安全
# 创建新的dataframe
new_df=files['dev_id','unit_id','dept_id','afci_information','line_overvoltage','line_undervoltage','line_overload','line_temperature','line_leakage','alarm_time']
# new_df.show()
new_df_2=new_df.withColumn('alarm_time',date_format(new_df.alarm_time, 'yyyy-MM-dd HH').cast(TimestampType()))\
    .withColumn("afci_information", new_df["afci_information"].cast(IntegerType()))\
    .withColumn("line_overvoltage", new_df["line_overvoltage"].cast(IntegerType()))\
    .withColumn("line_undervoltage", new_df["line_undervoltage"].cast(IntegerType()))\
    .withColumn("line_overload", new_df["line_overload"].cast(IntegerType()))\
    .withColumn("line_temperature", new_df["line_temperature"].cast(IntegerType())) \
    .withColumn("line_leakage", new_df["line_leakage"].cast(IntegerType())) \
    .withColumn("dept_id", new_df["dept_id"].cast(IntegerType()))\
    .withColumn("unit_id", new_df["unit_id"].cast(IntegerType()))

alarm_data=new_df_2
#     .filter((new_df_2.afci_information==1)
#                            |(new_df_2.line_overvoltage==1)
#                            |(new_df_2.line_undervoltage==1)
#                            |(new_df_2.line_overload==1)
#                            |(new_df_2.line_temperature==1)
#                            |(new_df_2.line_leakage==1))
# alarm_data.show()

# group_alarm_data=alarm_data.groupby('dev_id','unit_id','dept_id','afci_information','line_overvoltage',
#                                     'line_undervoltage','line_overload','line_temperature','line_leakage','alarm_time').count()
alarm_data_count=alarm_data.groupby('dev_id','unit_id','dept_id','alarm_time')\
    .agg({'afci_information':'sum','line_overvoltage':'sum','line_undervoltage':'sum','line_overload':'sum','line_temperature':'sum','line_leakage':'sum'})\
    .withColumnRenamed('sum(line_temperature)','temperature_count')\
    .withColumnRenamed('sum(line_overload)','overload_count')\
    .withColumnRenamed('sum(line_undervoltage)','undervoltage_count')\
    .withColumnRenamed('sum(line_leakage)','leakage_count')\
    .withColumnRenamed('sum(line_overvoltage)','overvoltage_count')\
    .withColumnRenamed('sum(afci_information)','afci_info_count')
alarm_data_count=alarm_data_count.withColumn('all_alarm_count',alarm_data_count['temperature_count']
                                             +alarm_data_count['overload_count']
                                             +alarm_data_count['undervoltage_count']
                                             +alarm_data_count['leakage_count']
                                             +alarm_data_count['overvoltage_count']
                                             +alarm_data_count['afci_info_count'])
# alarm_data_count.show()
alarm_data_count=alarm_data_count.withColumn('alarm_hour_time',hour(alarm_data_count.alarm_time))
alarm_data_count.show()


from pyspark.ml.classification import NaiveBayes
from pyspark.ml import Pipeline
from pyspark.ml.feature import OneHotEncoder, StringIndexer, VectorAssembler
alarm_data_count=alarm_data_count.drop('alarm_time')
old_columns_names = alarm_data_count.columns
new_columns_names = [name+'-new' for name in old_columns_names]
for i in range(len(old_columns_names)):
    indexer = StringIndexer(inputCol=old_columns_names[i], outputCol=new_columns_names[i])
    alarm_data_count = indexer.fit(alarm_data_count).transform(alarm_data_count)
vecAss = VectorAssembler(inputCols=new_columns_names[1:], outputCol='features')
alarm_data_count = vecAss.transform(alarm_data_count)
# 更换label列名
alarm_data_count = alarm_data_count.withColumnRenamed(new_columns_names[0], 'label')
alarm_data_count.show()

label_features = alarm_data_count.select(['label', 'features'])

# nb=NaiveBayes(smoothing=1.0)
# model=nb.fit(alarm_data_count)
# pre=model.transform(alarm_data_count)
# pre.filter(pre['prediction'] == 0) \
#     .select("dev_id","alarm_hour_time","probability","prediction") \
#     .orderBy("probability", ascending=False) \
#     .show(n = 10, truncate = 30)
# # 每小时设备报警数量
# dev_hour_alarm_count=alarm_data.groupby('dev_id','unit_id','dept_id','alarm_time')\
#     .count()\
#     .sort('count',ascending=False)
# # dev_hour_alarm_count.ca
# dev_hour_alarm_count.show()
#
# # 一个单位每小时报警数量
# unit_hour_alarm_count=dev_hour_alarm_count.groupby('unit_id','dept_id','alarm_time')\
#     .sum('count')\
#     .withColumnRenamed("sum(count)","count")\
#     .sort('count',ascending=False)
# unit_hour_alarm_count.show()
#
#
# #一个部门每小时报警数量
# dept_hour_alarm_count=unit_hour_alarm_count.groupby('dept_id','alarm_time')\
#     .sum('count')\
#     .withColumnRenamed("sum(count)","count")\
#     .sort('count',ascending=False)
# dept_hour_alarm_count.show()
#
# #一个单位每天报警数量
# unit_day_alarm_count=unit_hour_alarm_count.withColumn('alarm_time',date_format(unit_hour_alarm_count.alarm_time, 'yyyy-MM-dd'))\
#     .groupby('unit_id','dept_id','alarm_time')\
#     .sum('count')\
#     .withColumnRenamed("sum(count)","count")\
#     .sort('count',ascending=False)
# unit_day_alarm_count.show()


# 用电采集
# new_df=files['dev_id','unit_id','dept_id','voltage','current','current_power','frequency', 'factor', 'current_power',
#              'max_power', 'reactive_power', 'apparent_power', 'temperature_value', 'leakage_value','alarm_time']
# new_df.sort('apparent_power',ascending=False).show()





















