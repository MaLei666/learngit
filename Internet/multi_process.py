# -*- coding: utf-8 -*-
from multiprocessing import Process,Pool
import os,random,subprocess
from time import sleep,time

# #子进程要执行的代码
# def proc(name,age,**kwargs):
#     for i in range(10):
#         print('子进程：name=%s,age=%s,pid=%s'%(name,age,os.getpid()))
#         print(kwargs)
#         sleep(0.5)
#
# if __name__=='__main__':  #如果模块是被直接运行的，则代码块被运行，如果模块是被导入的，则代码块不被运行。
#     print('父进程：%s'%os.getpid())
#     p=Process(target=proc,args=('test',18),kwargs={'m':20})
#     print('子进程将要执行...')
#     p.start()
#     sleep(1)
#     p.terminate()
#     p.join()
#     print('子进程结束')

# #pool
# def task(name):
#     print('运行子进程%s(%s)'%(name,os.getpid()))
#     start=time()
#     sleep(random.random()*3)
#     end=time()
#     print('子进程%s运行 %.2f 秒'%(name,(end-start)))   #子进程01213是同时进行的，某个进程运行完毕后再运行子进程4
#
# if __name__ == '__main__':
#     print('父进程%s'%os.getpid())
#     p=Pool(4)  #创建4个子进程
#     for i in range(5):
#         p.apply_async(task,args=(i,))
#     p.close()    #调用close之后不能添加新的进程了
#     p.join()
#     print('所有进程完毕')
#

print('$ nslookup www.python.org')
r = subprocess.call(['nslookup', 'www.python.org'])
print('Exit code:', r)