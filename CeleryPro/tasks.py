#!/home/zkfr/.local/share/virtualenvs/xf-5EfV3Nly/bin/python
#-*- coding:utf-8 -*-
# @author : MaLei 
# @datetime : 2019-03-19 16:59
# @file : celery.py
# @software : PyCharm
from __future__ import absolute_import
from .celery import app
from kombu import Exchange,Queue

#增加两个task,test_queue_1与test_queue_2
# 此时调用main.py中的test_queue_1和test_queue_2，会发现task被分发到各个对应的celery worker服务。
#  对于没有被队列接收的sayhi函数，通过sayhi.apply_async(queue='queue_1’)可以将任务分发到queue_1

@app.task
def test_queue_1():
    return 'queue1'

@app.task
def test_queue_2():
    return 'queue2'

# queue_1与queue_2为消息队列名称
#  Exchange:为交换机实例，具有不同的类型。
#  routing_key:用来告知exchange将task message传送至相对应的queue

queue = (
    Queue('queue_1', Exchange('Exchange1', type='direct'), routing_key='queue_1_key'),
    Queue('queue_2', Exchange('Exchange2', type='direct'), routing_key='queue_2_key') )

route = { 'main.test_queue_1': {'queue': 'queue_1', 'routing_key': 'queue_1_key'},
          'main.test_queue_2': {'queue': 'queue_2', 'routing_key': 'queue_2_key'} }

app.conf.update(CELERY_QUEUES=queue, CELERY_ROUTES=route)

# celery的广播模式
# 同时在两个终端启动celery服务，通过broadcast.delay()调用task时，会发现两个celery实例均有执行broadcast函数。
from kombu.common import Broadcast

@app.task
def broadcast():
    return 'broadcast'

queue_bor = (
    Broadcast('broadcast_tasks'), #此处设置消息队列broadcast为广播模式，及该队列上的消息会发送至所有监听它的worker
    Queue('broadcast_tasks'),
)
queue_route = {
    'main.broadcast': {'queue': 'broadcast_tasks'},
}

app.conf.update(CELERY_QUEUES=queue_bor, CELERY_ROUTES=queue_route)