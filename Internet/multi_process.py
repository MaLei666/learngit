# -*- coding: utf-8 -*-
from multiprocessing import Process
import os
from time import sleep

#子进程要执行的代码
def proc(name,age,**kwargs):
    for i in range(10):
        print('子进程：name=%s,age=%s,pid=%s'%(name,age,os.getpid()))
        print(kwargs)
        sleep(0.5)

if __name__=='__main__':  #如果模块是被直接运行的，则代码块被运行，如果模块是被导入的，则代码块不被运行。
    print('父进程：%s'%os.getpid())
    p=Process(target=proc,args=('test',18),kwargs={'m':20})
    print('子进程将要执行...')
    p.start()
    sleep(1)
    p.terminate()
    p.join()
    print('子进程结束')
