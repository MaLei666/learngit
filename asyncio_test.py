#!/home/zkfr/.local/share/virtualenvs/xf-5EfV3Nly/bin/python
#-*- coding:utf-8 -*-
# @author : MaLei 
# @datetime : 2018-10-30 11:24
# @file : asyncio_test.py
# @software : PyCharm

import asyncio,time

# now=lambda: time.time()
# async def work(x):
#     print('waiting...',x)
#
# start=now()
# # 定义一个协程
# # 这里是一个协程对象，这个时候work函数并没有执行
# coroutine=work(2)
# print(coroutine)
# #  创建一个事件loop
# loop=asyncio.get_event_loop()
# # 使用run_until_complete将协程注册到事件循环，并启动事件循环
# # loop.run_until_complete(coroutine)

# 定义一个task
# 创建task后，在task加入事件循环之前为pending状态，当完成后，状态为finished
# 通过loop.create_task(coroutine)创建task,同样的可以通过 asyncio.ensure_future(coroutine)创建task
# task=loop.create_task(coroutine)
# print(task)
# loop.run_until_complete(task)
# print(task)

# 绑定回调
# task执行完成的时候可以获取执行的结果，回调的最后一个参数是future对象，通过该对象可以获取协程返回值。
# async def cb_work(x):
#     print('waiting...',x)
#     return 'Done after{}s'.format(x)
#
# def callback(future):
#     print('callback:',future.result())
#
# coroutine = cb_work(2)
# loop = asyncio.get_event_loop()
# task = asyncio.ensure_future(coroutine)
# print(task)
# # add_done_callback方法给task任务添加回调函数
# # 当task（也可以说是coroutine）执行完成的时候,就会调用回调函数
# # 并通过参数future获取协程执行的结果
# task.add_done_callback(callback)
# print(task)
# loop.run_until_complete(task)


# 阻塞和await
# 协程遇到await，事件循环将会挂起该协程，执行别的协程，直到其他的协程也挂起或者执行完毕，再进行下一个协程的执行
# async def do_some_work(x):
#     print("waiting:",x)
#     # await 后面就是调用耗时的操作
#     await asyncio.sleep(x)
#     return "Done after {}s".format(x)
#
# coroutine = do_some_work(2)
# loop = asyncio.get_event_loop()
# task = asyncio.ensure_future(coroutine)
# loop.run_until_complete(task
# print("Task ret:", task.result())



# 不是异步的
# import time
#
#
# def job(t):
#     print('Start job ', t)
#     time.sleep(t)               # wait for "t" seconds
#     print('Job ', t, ' takes ', t, ' s')
#
#
# def main():
#     [job(t) for t in range(1, 3)]
#
#
# t1 = time.time()
# main()
# print("NO async total time : ", time.time() - t1)


import asyncio


async def job(t):                   # async 形式的功能
    print('Start job ', t)
    await asyncio.sleep(t)          # 等待 "t" 秒, 期间切换其他任务
    print('Job ', t, ' takes ', t, ' s')


async def main(loop):                       # async 形式的功能
    tasks = [
    loop.create_task(job(t)) for t in range(1, 3)
    ]                                       # 创建任务, 但是不执行
    await asyncio.wait(tasks)               # 执行并等待所有任务完成

t1 = time.time()
loop = asyncio.get_event_loop()             # 建立 loop
loop.run_until_complete(main(loop))         # 执行 loop
loop.close()                                # 关闭 loop
print("Async total time : ", time.time() - t1)








