# -*- coding: utf-8 -*-
import threading,time
def loop1():
    #print('thread1 %s is running...'%threading.current_thread().name)  #显示子线程实例名字
    n=0
    while n<3:
        n=n+1
        print('thread1 %s >>> %s'%(threading.current_thread().name,n))   #current_thread()函数返回当前线程实例
        time.sleep(0.5)
    #print('thread %s ended...'%threading.current_thread().name)

def loop2():
    #print('thread2 %s is running...'%threading.current_thread().name)
    n=0
    while n<2:
        n+=1
        print('thread2 %s >>> %s' %(threading.current_thread().name,n))
        time.sleep(0.5)
    #print('thread2 %s ended...' % threading.current_thread().name)

if __name__ == '__main__':
    print('---开始---:%s'%time.ctime())
    print('thread %s is running'%threading.current_thread().name)    #显示主线程实例名字
    t=threading.Thread(target=loop1)  #创建子线程，loopthread为子线程的名字
    p=threading.Thread(target=loop2)
    t.start()
    p.start()
    t.join()
    p.join()
    while True:
        length=len(threading.enumerate())
        print('当前运行线程数量：%d'%length)
        if length<=1:
            break
    print('thread %s ended'%threading.current_thread().name)

