#!/home/zkfr/.local/share/virtualenvs/xf-5EfV3Nly/bin/python
#-*- coding:utf-8 -*-
# @author : MaLei 
# @datetime : 2019-03-20 17:05
# @file : celery_set.py
# @software : PyCharm

# from __future__ import absolute_import
from __future__ import absolute_import, unicode_literals
from celery import Celery

app = Celery('CeleryPro',
             broker='amqp://guest@localhost//',
             backend='redis://:zkyr1006@192.168.1.137:6379/3',
             include=['CeleryPro.tasks'])

# Optional configuration, see the application user guide.
app.conf.update(
    result_expires=3600,
)

if __name__ == '__main__':
    app.start()