class Settings():
    """"存储《外星人入侵》的所有设置类"""

    def __init__(self):
        """"初始化游戏设置"""
        # 屏幕设置
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        self.title = 'Alien Invasion'

        self.ship_speed_factor = 10

        #添加子弹
        self.bullet_speed_factor = 10
        self.bullet_width = 10
        self.bullet_height = 15
        self.bullet_color = (60,60,60)
        self.bullet_allowed = 10

        # 外星设置
        self.alien_speed_factor = 5
        self.fleet_drop_speed = 10

        # fleet_direction 为1 表示向右移，为-1表示向左移
        self.fleet_direction = 1

        self.ship_limit = 3