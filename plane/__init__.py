#-*-coding:utf-8-*-
import pygame
import time
import random
from pygame.locals import *

class Base():
    def __init__(self,screen,name):
        self.name=name
        self.screen=screen     #设置要显示内容的窗口

class Plane(Base):
    def __init__(self,screen,name):
        super(Plane, self).__init__(screen,name)   #调用父类init方法
        self.image=pygame.image.load(self.imageName).convert()      #利用pygame.image.load（）来加载位图
        self.bulletList=[]            # 用来存储英雄飞机发射的所有子弹

    def display(self):
        self.screen.blit(self.image,(self.x,self.y))   #更新飞机位置，blit函数绘制位图，self.image为加载完成的位图，(self.x,self.y)为起始坐标
        needDelList=[]                  #存放需要删除的对象信息
        for i in self.bulletList:       #保存需要删除的对象
            if i.judge():
                needDelList.append(i)
        for i in needDelList:            #删除需要删除的对象
            self.bulletList.remove(i)
        for bullet in self.bulletList:   #更新发出的子弹位置
            bullet.display()
            bullet.move()
        # for bullet in bulletList:    #修改子弹位置
        #     bullet.y-=2

    def Bulletbiu(self):
        newBullet = PublicBullen(self.x, self.y, self.screen,self.name)
        self.bulletList.append(newBullet)

class heroplane(Plane):
    def __init__(self,screen,name):
        self.x=230          #设置飞机默认位置
        self.y=600
        # self.screen=screen        #设置要显示内容的窗口
        #保存飞机图片名字
        self.imageName='E:/资料整理/工作相关扩展/python/01课件和资料/1. Python基础/截图和代码/飞机大战-下/feiji/hero.gif'
        super(heroplane, self).__init__(screen,name)
        # self.image=pygame.image.load(self.imageName).convert()        #根据飞机名字生成飞机图片
        # self.bulletList=[]        #保存发射的子弹
    def moveLeft(self):
        self.x-=30
    def moveRight(self):
        self.x+=30

# class Bullet():
#     def __init__(self,x,y,screen):
#         self.x=x+40
#         self.y=y-20
#         self.screen=screen
#         self.image=pygame.image.load('E:/资料整理/工作相关扩展/python/01课件和资料/1. Python基础/截图和代码/飞机大战-下/feiji/bullet.png').convert()
#     def move(self):
#         self.y-=2
#     def display(self):
#         self.screen.blit(self.image,(self.x,self.y))
#     def judge(self):
#         if self.y<0:
#             return true
#         else:
#             return false

class Enemyplane(Plane):
    def __init__(self,screen,name):
        self.x=0        #设置飞机默认位置
        self.y=0
        # self.screen=screen
        self.imageName='E:/资料整理/工作相关扩展/python/01课件和资料/1. Python基础/截图和代码/飞机大战-下/feiji/enemy-1.gif'
        super(Enemyplane, self).__init__(screen,name)
        # self.image=pygame.image.load(self.imageName).convert()
        # self.bulletList=[]
        self.direction='right'
    # def display(self):
    #     self.screen.blit(self.image, (self.x, self.y))
    #     # 存放需要删除的对象信息
    #     needDelList = []
    #     # 保存需要删除的对象
    #     for i in bulletList:
    #         if i.judge():
    #             needDelList.append(i)
    #     # 删除需要删除的对象
    #     for i in needDelList:
    #         self.bulletList.remove(i)
    #     # 更新发出的子弹位置
    #     for bullet in self.bulletList:
    #         bullet.display()
    #         bullet.move()
    def move(self):
        if self.direction=='right':
            self.x+=1
        elif self.direction=='left':
            self.x-=1
        if self.x>400-50:
            self.direction='left'
        if self.x<0:
            self.direction='right'

    def Bulletbiu(self):
        num=random.randint(1,100)
        if num==88:
            # newBullet = EnemyBullet(self.x, self.y, self.screen)
            # self.bulletList.append(newBullet)
            super(Enemyplane, self).Bulletbiu()

# class EnemyBullet():
#     def __init__(self, x, y, screen):
#         self.x = x + 30
#         self.y = y + 30
#         self.screen = screen
#         self.image = pygame.image.load("E:/资料整理/工作相关扩展/python/01课件和资料/1. Python基础/截图和代码/飞机大战-下/feiji/bullet-1.gif").convert()

#     def move(self):
#         self.y+=2
#
#     def display(self):
#         self.screen.blit(self.image,(self.x,self.y))
#
#     def judge(self):
#         if self.y>730:
#             return true
#         else:
#             return false

class PublicBullen(Base):
    def __init__(self,x,y,screen,planeName):
        super(PublicBullen, self).__init__(screen,planeName)
        if self.name=='hero':
            self.x = x + 40
            self.y = y - 20
            imageName=('E:/资料整理/工作相关扩展/python/01课件和资料/1. Python基础/截图和代码/飞机大战-下/feiji/bullet-3.gif')
        elif self.name=='enemy':
            self.x = x + 30
            self.y = y + 30
            imageName=("E:/资料整理/工作相关扩展/python/01课件和资料/1. Python基础/截图和代码/飞机大战-下/feiji/bullet-1.gif")
        self.image=pygame.image.load(imageName).convert()

    def move(self):
        if self.name=='hero':
            self.y -= 3
        if self.name=='enemy':
            self.y += 2

    def display(self):
        self.screen.blit(self.image, (self.x, self.y))

    def judge(self):
        if self.y < 0 or self.y>730:
             return True
        else:
            return False


if __name__=='__main__':
    screen=pygame.display.set_mode((400,730),0,32)      # 创建窗口
    # 创建图片充当背景
    background=pygame.image.load("E:/资料整理/工作相关扩展/python/01课件和资料/1. Python基础/截图和代码/飞机大战-下/feiji/background.png").convert()
    #面向过程方式显示飞机
    # #创建玩家飞机图片
    # hero=pygame.image.load("E:/资料整理/工作相关扩展/python/01课件和资料/1. Python基础/截图和代码/飞机大战-下/feiji/hero.gif").convert()
    # #保存飞机坐标
    # x=0
    # y=600
    #背景放到窗口显示
    HeroPlane=heroplane(screen,'hero')      #面向对象方式显示飞机，对类进行实例化，之后才能应用
    EnemyPlane=Enemyplane(screen,'enemy')   #创建敌人飞机

    while True:

        screen.blit(background,(0,0))       #设定选定的背景图
        #screen.blit(hero,(x,y))
        HeroPlane.display()                 #设定显示的飞机图片
        EnemyPlane.move()
        EnemyPlane.Bulletbiu()
        EnemyPlane.display()
        for event in pygame.event.get():     #获取事件
            if event.type==QUIT:        #判断是否按下退出
                print ('quit')
                exit()
            elif event.type==KEYDOWN:       #判断是否按下键
                if event.key==K_a or event.key==K_LEFT:
                    print ('left')
                    #x-=10
                    HeroPlane.moveLeft()
                elif event.key==K_d or event.key==K_RIGHT:
                    print ('right')
                    #x+=10
                    HeroPlane.moveRight()
                elif event.key==K_SPACE:
                    print ('space')
                    HeroPlane.Bulletbiu()

        time.sleep(0.01)
        pygame.display.update()  #更新需要显示的内容


