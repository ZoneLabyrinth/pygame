class GameStats():
    '''跟踪统计信息'''
    def __init__(self,ai_settings):
        '''初始化'''
        self.ai_settings = ai_settings
        self.reset_stats()
        self.game_active = True

    def reset_stats(self):
        """初始化游戏运行期间变化的信息"""
        self.ships_left = self.ai_settings.ship_limit

