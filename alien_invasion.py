import sys

import pygame

from setting import Settings
from ship import Ship

import game_functions as gf



def run_game():
    # 初始化游戏并创建一个屏幕对象
    pygame.init()
    ai_settings = Settings()
    # 创建显示窗口及标题
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption(ai_settings.title)

    ship = Ship(screen)

    # 设置背景色
    # bg_color = (230, 230, 230)

    # 开始游戏的主循环 每次动画都会重绘

    while True:
        # 监视键盘和鼠标事件
        # for event in pygame.event.get():
        #     if event.type == pygame.QUIT:
        #         sys.exit()
        gf.check_events(ship)
        ship.update()
        gf.update_screen(ai_settings,screen,ship)
        #填充颜色，只接受一个参数
        # screen.fill(ai_settings.bg_color)
        # ship.blitme()
        # #         让最近绘制的屏幕可见
        # pygame.display.flip()


run_game()

