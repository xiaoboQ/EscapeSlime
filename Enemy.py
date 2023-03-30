"""对Enemy对象的定义"""

import pygame
import random

#记录玩家的分数
SCORE = 0

#导入屏幕数据
width = 1200
height = 676

#设置敌人速度
speed = 3


class Enemy_1(pygame.sprite.Sprite):
    def __init__(self):
        #调用父类的初始化方法
        super().__init__()

        #制作随机初始化位置
        self.x = random.randint(0,width - 100)
        self.image = pygame.image.load("images/silme.bmp")
        self.rect = self.image.get_rect(top = 0 , left = self.x)

    def move(self):
        self.rect.move_ip(0,speed)

        #为玩家赋分
        if self.rect.top >= 675:
            global SCORE
            SCORE += 1

        #重新返回原位置
        if self.rect.top >= 675:
            self.x = random.randint(0, width - 100)
            self.rect.y = 0
            self.rect.x = self.x



class Enemy_2(pygame.sprite.Sprite):
    def __init__(self):
        #调用父类的初始化方法
        super().__init__()

        #制作随机初始化位置
        self.y = random.randint(0,height - 97)
        self.image = pygame.image.load("images/silme_two.bmp")
        self.rect = self.image.get_rect(top = self.y , left = 0)

    def move(self):
        self.rect.move_ip(speed,0)

        #为玩家赋分
        if self.rect.left >= 1200:
            global SCORE
            SCORE += 1

        #重新返回原位置
        if self.rect.x >= 1200:
            self.y = random.randint(0, height - 97)
            self.rect.x = 0
            self.rect.y = self.y
