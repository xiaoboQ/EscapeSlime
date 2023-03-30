"""设计Player类"""
import pygame
import data

#设置屏幕数据
width = 1200
height = 676



class Player(pygame.sprite.Sprite):

    #对自己进行初始化
    def __init__(self):
        # 调用父类方法进行初始化
        super().__init__()
        #加载自身图片并且得到矩形边框
        self.image = pygame.image.load("images/test.png")
        self.rect = self.image.get_rect(top = height/2 , left = width/2)

    #设计移动函数
    def move(self):

        #从键盘上获取所按下的键的列表
        pressed_keys = pygame.key.get_pressed()

        #进行边缘检测
        if self.rect.top <= 0 or self.rect.top >= height - self.rect.height or \
            self.rect.left <= 0 or self.rect.left >= width - self.rect.width:
            #如果处于屏幕边缘则将Player拉回屏幕
            if self.rect.top <= 0 :
                self.rect.move_ip(0,data.speed)

            if self.rect.top >= height - self.rect.height:
                self.rect.move_ip(0,-data.speed)

            if self.rect.left <= 0:
                self.rect.move_ip(data.speed,0)

            if self.rect.left >= width - self.rect.width:
                self.rect.move_ip(-data.speed,0)

        else:
            #根据按键控制Player移动
            if pressed_keys[pygame.K_UP]:
                self.rect.move_ip(0,-data.speed)

            if pressed_keys[pygame.K_DOWN]:
                self.rect.move_ip(0,data.speed)

            if pressed_keys[pygame.K_LEFT]:
                self.rect.move_ip(-data.speed,0)

            if pressed_keys[pygame.K_RIGHT]:
                self.rect.move_ip(data.speed,0)





