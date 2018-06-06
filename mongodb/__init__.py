# -*- coding: utf-8 -*-
import pymongo
import pytesseract
from bson.objectid import ObjectId

client=pymongo.MongoClient(host='localhost',port=27017)
# client = MongoClient('mongodb://localhost:27017/')
db = client.python
collection=db.python

# 插入数据
# python = {
#     'id': '20170101',
#     'name': 'Jordan',
#     'age': 20,
#     'gender': 'male'
# }
# result=collection.insert_one(python)
# print(result)
# print(result.inserted_id)

# 查询单条数据
# result=collection.find_one({'_id': ObjectId('5b177a5df728ae9074b49a67')})
# print(type(result))
# print(result)

# 查询多条数据
# results=collection.find({'age':20})
# print(results)
# for result in results:
#     print(result)

# 计数
# count1=collection.find().count()
# count2=collection.find({'age':20}).count()
# print(count1)
# print(count2)

# 排序
# results=collection.find().sort('name',pymongo.DESCENDING)
# for result in results:
#     print(result['name'])

# 偏移
# results=collection.find().sort('name',pymongo.DESCENDING).skip(2).limit(1)
# for result in results:
#     print(result['name'])

# 更新#
# condition={'python':'malei'}
# newdata=collection.find_one(condition)
# newdata['id']= '20170112'
# # result=collection.update(condition,newdata)
# # result=collection.update(condition,{'$set':newdata})
# result=collection.update_one(condition,{'$set':newdata})
# print(result.matched_count, result.modified_count)
# print(result)

# condition={'age': {'$gte': 20}}
# result=collection.update_many(condition,{'$inc': {'age': 21}})
# print(result.matched_count, result.modified_count)
# print(result)

# 删除
# collection.remove({'python': 'malei'})
# result=collection.delete_one({'name':'Jordan'})
# print(result)
# print(result.deleted_count)
result=collection.delete_many({'name':'Jordan'})
print(result)
print(result.deleted_count)
