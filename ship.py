import pygame


class Ship():

    def __init__(self, screen):
        """"初始化飞船并设置起始位置"""
        self.screen = screen

        # 加载飞船图像并获取起外接矩形
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # 按住键盘不放标志
        self.moving_right = False

        self.moving_left = False

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def update(self):
        """根据移动标志调整飞船位置"""
        if self.moving_right:
            self.rect.centerx += 1
        if self.moving_left:
            self.rect.centerx -= 1
