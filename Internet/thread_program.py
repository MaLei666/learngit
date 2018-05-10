# -*- coding: utf-8 -*-
import threading,time
# def loop1():
#     print('线程 %s 运行...'%threading.current_thread().name)  #显示子线程实例名字
#     n=0
#     while n<3:
#         n=n+1
#         print('%s >>> %s'%(threading.current_thread().name,n))   #current_thread()函数返回当前线程实例
#         time.sleep(0.5)
#     print('线程 %s 结束...'%threading.current_thread().name)
#
# def loop2():
#     print('线程 %s 运行...'%threading.current_thread().name)
#     n=0
#     while n<2:
#         n+=1
#         print('%s >>> %s' %(threading.current_thread().name,n))
#         time.sleep(0.5)
#     print('线程 %s 结束...' % threading.current_thread().name)


def change_it(n):
    # 先存后取，结果应该为0:
    global balance
    balance = balance + n
    balance = balance - n

def thread(n):
    for i in range(1000):
        #获取锁
        lock.acquire()
        try:
            change_it(n)
        finally:
            #改完释放锁
            lock.release()

if __name__ == '__main__':
    balance=0
    lock=threading.Lock()
    t1 = threading.Thread(target=thread, args=(5,))
    t2 = threading.Thread(target=thread, args=(8,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print(balance)

    # 创建全局ThreadLocal对象
    local_data = threading.local()

    # print('---开始---:%s'%time.ctime(),'\n')
    # # 显示当前线程，即主线程实例名字
    # print('%s 运行'%threading.current_thread().name)
    # # 创建子线程，子线程名字在创建时指定，loopthread为子线程的名字，不指定为默认名
    # t=threading.Thread(target=loop1,name='子线程1')
    # p=threading.Thread(target=loop2,name='子线程2')
    # #子线程可以全部start之后再join，即为交替运行，分开执行，为运行完子线程1，再运行子线程2
    # #
    # t.start()
    # p.start()
    # t.join()
    # p.join()
    #
    # while True:
    #     length=len(threading.enumerate())
    #     print('当前运行线程数量：%d'%length)
    #     if length<=1:
    #         break
    # print('thread %s ended'%threading.current_thread().name)

