"""
Pygame 2D游戏

1. 规划项目
规划可确保我们不偏离轨道，从而提高项目成功的可能性

Usage:

"""
import sys, pygame
from settings import Settings
from ship import Ship


class AlientInvasion:
    """管理游戏资源和行为"""

    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("打怪兽")
        self.ship = Ship(self)

    def run_game(self):
        """"开始游戏主循环"""
        while True:
            # 监视键盘和鼠标事件
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            self.screen.fill(self.settings.bg_color)
            self.ship.blitme()
            # 让最近绘制的屏幕可见
            pygame.display.flip()


if __name__ == '__main__':
    ai = AlientInvasion()
    ai.run_game()
