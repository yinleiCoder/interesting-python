import pygame
from pygame.sprite import Sprite
"""
Ship类：
    负责管理飞船的大部分行为
"""

class Ship(Sprite):
    """管理飞船"""

    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.settings = ai_game.settings
        # 加载飞船图像并获取其外接矩形
        self.image = pygame.image.load('images/superman.png').convert_alpha()
        self.image_rotate = pygame.transform.rotate(self.image, 90).convert_alpha()
        self.image = pygame.transform.scale(self.image_rotate, (50, 65)).convert_alpha()
        self.rect = self.image.get_rect()
        # 每艘新飞船，都将其放在屏幕底部的中央
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
        # 移动标志
        self.moving_right = False
        self.moving_left = False


    def update(self):
        """根据移动标志调整飞船的位置"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
        self.rect.x = self.x

    def center_ship(self):
        """让飞船在屏幕底端居中"""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)

    def blitme(self):
        """在指定位置绘制飞船"""
        self.screen.blit(self.image, self.rect)
