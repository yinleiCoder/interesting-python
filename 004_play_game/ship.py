"""
负责管理飞船的大部分行为

Usage:
"""
import pygame

class Ship:

    def __init__(self, ai_game):
        """初始化飞船并设置其初始位置"""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # 加载飞船图像并获取其外接矩形
        self.image = pygame.image.load("images/ship.bmp")
        self.rect = self.image.get_rect()

        # 将新飞船放置到屏幕底部
        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        """指定位置绘制飞船"""
        self.screen.blit(self.image, self.rect)

