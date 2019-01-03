import pygame

class Ship():

    def __init__(self,ai_settings, screen):
        """"初始化飞船并设置起始位置"""
        self.screen = screen
        self.ai_settings = ai_settings

        # 加载飞船图像并获取起外接矩形
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # 只用于存储浮点值，最终还要反映到rect对象上
        self.center = float(self.rect.centerx)

        # 按住键盘不放标志
        self.moving_right = False

        self.moving_left = False

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def update(self):
        """根据移动标志调整飞船位置"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor

        # 根据self.center更新rect对象
        self.rect.centerx = self.center
