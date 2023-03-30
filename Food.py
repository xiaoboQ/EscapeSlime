#定义食物类
import pygame.sprite
class food_1(pygame.sprite.Sprite):
    def __init__(self):
        super(food_1, self).__init__()
        self.image = pygame.image.load("images/food.bmp")
        self.rect = self.image.get_rect()


class food_2(pygame.sprite.Sprite):
    def __init__(self):
        super(food_2, self).__init__()
        self.image = pygame.image.load("images/nz.bmp")
        self.rect = self.image.get_rect()