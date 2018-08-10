# -*- coding: utf-8 -*-
import pymongo
import pytesseract
from bson.objectid import ObjectId

client=pymongo.MongoClient(host='localhost',port=27017)
# client = MongoClient('mongodb://localhost:27017/')
db = client.python
collection=db.python

# 插入数据
python = {'content': '对于经济学、商科的学生来说，使用数理统计的方法做文章的套路可能理所当然：观察到一个现象，提出因果关系假说， 收集大量合适的数据跑回归，得出结论，再对结论做robust检验，基本上这篇文章就能立住了。但是遗憾的是，很多时候，这个套路在历史研究当中是…',
 'name': '赫连镜繇',
 'num': '190',
 'que_url': 'https://www.zhihu.com/question/281446079/answer/422900276',
 'question': '历史学专业是如何分析数据的呢？'}

result=collection.insert_one(python)
print(result)
print(result.inserted_id)

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
# result=collection.delete_many({'name':'Jordan'})
print(result)
# print(result.deleted_count)
