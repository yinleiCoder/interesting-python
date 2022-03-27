"""
设置类：
    每次给游戏添加新功能时，通常也将引入一些新设置。
    设置类，用于将所有设置都存储在一个地方，以免在代码中导出添加设置。
    每当需要访问这些设置时，只需使用一个设置对象，而无须查找散步在项目中的各种设置。
"""
class Settings:
    """存储游戏中所有设置"""

    def __init__(self):
        """初始化游戏的静态设置"""
        self.screen_with = 1200
        self.screen_height = 800
        self.bg_color = (0, 0, 0)
        # 飞船设置
        self.ship_speed = 1.0
        self.ship_limit = 3
        # 子弹设置
        self.bullet_speed = 1.5
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (255, 0, 0)
        self.bullets_allowed = 3
        # 外星人设置(fleet_direction=1表示向右移，-1表示向左移)
        self.alien_speed = 0.5
        self.fleet_drop_speed = 10
        self.fleet_direction = 1

        # 加快游戏节奏
        self.speedup_scale = 1.1
        self.score_scale = 1.5
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """初始化随游戏进行而变化的设置"""
        self.ship_speed = 1.0
        self.bullet_speed = 1.5
        self.alien_speed = 0.5
        self.fleet_direction = 1
        # 计分
        self.alien_points = 10

    def increase_speed(self):
        """提高速度设置"""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)
