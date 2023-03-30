# 导入所需要的库
import pygame
import sys
import time
import random
# 导入背景
import Enemy
import background
# 导入Player模块
from Player import Player
# 导入Enemy模块
from Enemy import Enemy_1, Enemy_2
import data
import Food

# 玩家的游玩次数
times = 3

# 颜色的设置
BLACK = (0, 0, 0)
RED = (238, 44, 44)
GREY = (190, 190, 190)

# 设置游戏的FPS
FPS = 60
clock = pygame.time.Clock()

# 初始化游戏
pygame.init()

# 字体的设置
font_big = pygame.font.SysFont("微软雅黑", 40)
font_small = pygame.font.SysFont("隶书 常规", 40)
game_over = font_big.render("GAME_OVER", True, RED)
END = font_big.render("Tanks for playing my game", True, BLACK)
score = font_small.render(f"{Enemy.SCORE}", True, RED)

# 设置屏幕的数据
width = 1200
height = 675
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("刻晴大战史莱姆")

# 实例化玩家对象
player = Player()

# 实例化Enemy对象
enemy_1_1 = Enemy_1()
enemy_1_2 = Enemy_1()
enemy_1_3 = Enemy_1()
enemy_1_4 = Enemy_1()
enemy_2_1 = Enemy_2()
enemy_2_2 = Enemy_2()
enemy_2_3 = Enemy_2()

# 存放所有敌人的精灵列表，便于遍历检查
list_sprite_1 = [enemy_1_1, enemy_1_2, enemy_1_3, enemy_1_4]
list_sprite_2 = [enemy_2_1, enemy_2_2, enemy_2_3]
# 构造精灵组存放敌人精灵
all_sprite_1 = pygame.sprite.Group()
all_sprite_1.add(enemy_1_1)
all_sprite_1.add(enemy_1_2)
all_sprite_1.add(enemy_1_3)
all_sprite_1.add(enemy_1_4)

all_sprite_2 = pygame.sprite.Group()
all_sprite_2.add(enemy_2_1)
all_sprite_2.add(enemy_2_2)
all_sprite_2.add(enemy_2_3)

# 设置食物组
food_1 = Food.food_1()
food_2 = Food.food_2()
food_1_Group = pygame.sprite.Group()
food_2_Group = pygame.sprite.Group()
food_1_Group.add(food_1)
food_2_Group.add(food_2)

# 食物打印的旗帜
food_1_flag = False
food_2_flag = False
# 初始化计时器
count = 0

# 初始化计数器
Count = 0

# 游戏前置提醒
start_image = pygame.image.load("images/start.png")
screen.fill(GREY)
screen.blit(start_image, (300, 100))
pygame.display.update()
pygame.mixer.Sound("music/start.mp3").play()
time.sleep(16)
pygame.mixer.Sound("music/start.mp3").stop()

pygame.mixer.Sound("music/bg_music.flac").play((-1))
# 游戏的主循环
while True:

    # 设置游戏的背景
    screen.blit(background.background, (0, 0))

    # 绘制血量
    life_temp = 0
    for lifes in range(times):
        screen.blit(background.life, (life_temp, 0))
        life_temp = life_temp + background.life_width

    # 绘制分数
    screen.blit(score, (1150, 0))
    score = font_small.render(f"{Enemy.SCORE}", True, RED)

    # 绘制玩家
    screen.blit(player.image, player.rect)
    player.move()

    # 控制精灵组中精灵的移动与绘制
    if Enemy.SCORE <= 30:
        for sprites in all_sprite_1:
            screen.blit(sprites.image, sprites.rect)
            sprites.move()
    else:
        for sprites in all_sprite_1:
            screen.blit(sprites.image, sprites.rect)
            sprites.move()

        for sprites in all_sprite_2:
            screen.blit(sprites.image, sprites.rect)
            sprites.move()

    pressed_keys = pygame.key.get_pressed()

    # 快捷键(w)调出菜单
    if pressed_keys[pygame.K_w]:
        screen.fill(GREY)
        screen.blit(background.menu, background.menu_rect)
        # 刷新屏幕
        pygame.display.update()
        time.sleep(1)

    if pygame.sprite.spritecollide(player, all_sprite_1, True):
        times -= 1
        Enemy.speed += 1
        pygame.mixer.Sound("music/hurt_1.mp3").play()

    if pygame.sprite.spritecollide(player, all_sprite_2, True):
        times -= 2
        Enemy.speed += 1
        pygame.mixer.Sound("music/hurt_2.mp3").play()

    # 增加游戏(趣味性)
    count += 1

    # 打印道具food_1
    if (count % 4000 == 0):
        food_x = random.randint(0, 1100)
        food_y = random.randint(0, 650)
        food_1_flag = True
    if (food_1_flag):
        food_1.rect.x = food_x
        food_1.rect.y = food_y
        screen.blit(food_1.image, food_1.rect)

    # 对于事件的判断
    if pygame.sprite.spritecollide(player, food_1_Group, True):
        if (food_1_flag):
            data.speed += 1
            # 音乐
            pygame.mixer.Sound("music/food_1.wav").play()
        # 取消食物显示旗帜
        food_1_flag = False
        # 将食物加回食物组
        food_1_Group.add(food_1)

    if (count % 6000 == 0):
        food_x = random.randint(0, 1100)
        food_y = random.randint(0, 650)
        food_2_flag = True

    if (food_2_flag):
        food_2.rect.x = food_x
        food_2.rect.y = food_y
        screen.blit(food_2.image, food_2.rect)

    if pygame.sprite.spritecollide(player, food_2_Group, True):
        if (food_2_flag):
            times += 1
            Enemy.speed -= 1
            pygame.mixer.Sound("music/food_2.wav").play()

        food_2_flag = False
        food_2_Group.add(food_2)

    # 调整敌人速度
    Enemy.speed = 3 + int(count / 3600)

    if times <= 0:
        # 打印结束语
        score_temp = font_big.render(f"SCORE : {Enemy.SCORE}", True, BLACK)
        screen.fill(GREY)
        screen.blit(END, (430, 620))
        screen.blit(background.end, background.end_rect)
        screen.blit(score_temp, (500, 50))
        # 刷新屏幕
        pygame.display.update()
        # 事件停止2秒
        time.sleep(4)
        pygame.quit()
        sys.exit()

    # 快捷键(q)控制退出
    if pressed_keys[pygame.K_q]:
        # 打印结束语
        score_temp = font_big.render(f"SCORE : {Enemy.SCORE}", True, BLACK)
        screen.fill(GREY)
        screen.blit(END, (430, 620))
        screen.blit(background.end, background.end_rect)
        screen.blit(score_temp, (500, 50))
        # 刷新屏幕
        pygame.display.update()
        # 事件停止2秒
        time.sleep(4)
        pygame.quit()
        sys.exit()

    # 在点击右上角叉号的时候选择退出
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # 更新屏幕
    pygame.display.update()

    # 根据FPS调整屏幕的更新数据
    clock.tick(FPS)
