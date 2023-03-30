import pygame
#导入屏幕的数据信息
height = 675
width = 1200

#设置背景信息
background = pygame.image.load("images/background.bmp")

#退出键(q)
end = pygame.image.load("images/paimeng.bmp")
end_rect = end.get_rect(top = 100 ,left = 300)

#菜单键(w)
menu = pygame.image.load("images/menu_temp.png")
menu_rect = menu.get_rect(top = 100,left = 300)

#血量
life = pygame.image.load("images/life.bmp")
life_width = 30


"""哈哈哈哈背景就这么多了代码量，说实话第一次开发游戏还真是的不是很容易
再接再厉吧"""