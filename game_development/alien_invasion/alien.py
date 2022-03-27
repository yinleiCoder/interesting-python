import pygame
from pygame.sprite import Sprite
"""
Alien类——外星人来了：
    首先在屏幕上边缘附近添加一个外星人，再生成一群外星人。然后让这群外星人向两边和下面移动，并删除被子弹击中的外星人。最后显示玩家拥有的飞船数量，并
    在玩家的飞船用完后结束游戏。
    
    开发计划：
        1. 研究既有代码，确定实现新功能前是否要重构。
           在项目中添加新功能前，还应审核既有代码。每进入一个新阶段，项目通常会更复杂，因此最好对混乱或低效的代码进行清理。
        2. 在屏幕左上角添加一个外星人，并指定合适的边距。
        3. 根据第一个外星人的边距和屏幕尺寸计算屏幕上可容纳多少个外星人，使其填满屏幕的上半部分。
        3. 让外星人群向两边和下方移动，直到外星人被全部击落、有外星人撞到飞船或外星人抵达屏幕底端。如果整群外星人都被击落，将再创建一群外星人。如果
           有外星人撞到了飞船或抵达屏幕底端，将销毁飞船并再创建一群外星人。
        4. 限制玩家可用的飞船数量。当配给的飞船用完之后，游戏结束。
"""
class Alien(Sprite):
    """表示单个外星人的类。"""

    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.image = pygame.image.load('images/alien.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (85, 100)).convert_alpha()
        self.rect = self.image.get_rect()
        # 每个外星人最初都在屏幕左上角附近
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)

    def check_edges(self):
        """检查外星人是否撞到了屏幕边缘"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True

    def update(self):
        """向左边或右移动外星人群"""
        self.x += (self.settings.alien_speed * self.settings.fleet_direction)
        self.rect.x = self.x
