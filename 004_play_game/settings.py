"""
设置类
封装所有设置，项目增大时，只需要使用一个设置对象

Usage:
"""
class Settings:
    """存储游戏中所有的设置"""
    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
