import sys
from time import sleep
import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard
"""
规划项目：(开发大型项目时，制定好规划后再动手编写代码很重要。规划可确保我们不会偏离轨道，从而提高项目成功的可能性。)
    玩家控制一艘最初出现在屏幕底部中央的飞船。玩家可以使用箭头键左右移动飞船，可使用空格键射击。
    游戏开始时，一群外星人出现在天空中，并向屏幕下方移动。玩家的任务就是射杀这些外星人。
    玩家将所有外星人都消灭干净后，将出现一群新的外星人，其移动速度更快。
    只要有外星人撞到玩家的飞船或者到达屏幕的底部，玩家就损失一艘飞船，损失3艘后，游戏判定结束。

安装Pygame:
    python -m pip install --user pygame
    这条命令可以让Python运行pip模块，将pygame包添加到当前用户的python安装中。
    或者pip install pygame, 亦或是用Anaconda管理。

"""

class AlienInvasion:
    """管理游戏资源和行为的类"""
    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption('Alien Invasion')
        # 计分
        self.stats = GameStats(self)
        self.board = Scoreboard(self)
        # 飞船
        self.ship = Ship(self)
        # 子弹存储到编组中
        self.bullets = pygame.sprite.Group()
        # 外星人存储到编组中
        self.aliens = pygame.sprite.Group()
        self._handle_create_fleet()
        #开始游戏
        self.play_button = Button(self, "Play")

    def _handle_create_fleet(self):
        """创建外星人群"""
        # 创建一行外星人并计算一行可以容纳多少个外星人(外星人之间的间距为外星人宽度)
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        avaiable_space_x = self.settings.screen_with - (2 * alien_width)
        number_aliens_x = avaiable_space_x // (2 * alien_width)
        # 计算屏幕可容纳多少行外星人
        ship_height = self.ship.rect.height
        avaiable_space_y = (self.settings.screen_height - (3*alien_height) - ship_height)
        number_rows = avaiable_space_y // (2*alien_height)
        for row_number in range(number_rows):
            for alien_number in range(number_aliens_x):
                self._handle_create_alien(alien_number, row_number)

    def _handle_create_alien(self, alien_number, row_number):
        """创建一个外星人并将其放在当前行"""
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien.rect.height + 2*alien.rect.height*row_number
        self.aliens.add(alien)

    def _handle_update_bullets(self):
        """更新子弹的位置并删除消失的子弹"""
        # 对编组调用update, 编组自动对其中的每个精灵Sprite调用update()
        self.bullets.update()
        # 删除消失的子弹(因为不能从for循环遍历的列表或编组中删除元素，所以必须遍历编组的副本)
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

        self._handle_check_bullet_alien_collisions()

    def _handle_check_bullet_alien_collisions(self):
        """检查子弹与外星人的碰撞"""
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)
        if collisions:
            for aliens in collisions.values():
                self.stats.score += self.settings.alien_points*len(aliens)
            self.board.prep_score()
            self.board.check_high_score()
        if not self.aliens:
            self.bullets.empty()
            self._handle_create_fleet()
            # 加快游戏节奏(升级)
            self.settings.increase_speed()
            # 提高等级
            self.stats.level += 1
            self.board.prep_level()

    def _handle_fire_bullet(self):
        """创建一颗子弹，并将其加入编组bullets中"""
        # 限制子弹数量
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _handle_check_keydown_events(self, event):
        """响应键盘按下"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._handle_fire_bullet()

    def _handle_check_keyup_events(self, event):
        """响应键盘抬起"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _handle_check_play_button(self, mouse_pos):
        """点击play按钮开始游戏"""
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.stats.game_active:
            self.settings.initialize_dynamic_settings()
            self.stats.reset_stats()
            self.stats.game_active = True
            self.board.prep_score()
            self.board.prep_level()
            self.board.prep_ships()
            self.aliens.empty()
            self.bullets.empty()
            self._handle_create_fleet()
            self.ship.center_ship()
            # 隐藏光标
            pygame.mouse.set_visible(False)

    def _handle_check_events(self):
        """事件循环"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._handle_check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._handle_check_keyup_events(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._handle_check_play_button(mouse_pos)

    def _hanlde_change_fleet_direction(self):
        """将整群外星人下移，并改变他们的方向"""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    def _handle_check_fleet_edges(self):
        """有外星人到达边缘时采取相应的措施"""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._hanlde_change_fleet_direction()
                break

    def _hanlde_check_aliens_bottom(self):
        """检查是否有外星人到达了屏幕底端"""
        screen_rect = self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                self._handle_ship_hit()
                break

    def _handle_update_aliens(self):
        """检查是否有外星人位于屏幕边缘并更新外星人群中所有外星人的位置"""
        self._handle_check_fleet_edges()
        self.aliens.update()
        # 检查外星人与飞船的碰撞
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            # 删除余下的外星人和子弹，让飞船重新居中，创建一群新的外星人
            self._handle_ship_hit()
        # 检查外星人是否到了屏幕底端
        self._hanlde_check_aliens_bottom()

    def _handle_ship_hit(self):
        """响应飞船被外星人撞到"""
        if self.stats.ships_left > 0:
            self.stats.ships_left -= 1
            self.board.prep_ships()
            self.aliens.empty()
            self.bullets.empty()
            self._handle_create_fleet()
            self.ship.center_ship()
            sleep(1)
        else:
            self.stats.game_active = False
            # 重新显示光标
            pygame.mouse.set_visible(True)

    def _handle_update_screen(self):
        """刷新屏幕"""
        # 设置背景色
        self.screen.fill(self.settings.bg_color)
        # 添加飞船
        self.ship.blitme()
        # 绘制子弹
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        # 绘制外星人
        self.aliens.draw(self.screen)
        # 显示得分
        self.board.show_score()
        if not self.stats.game_active:
            self.play_button.draw_button()
        # 屏幕更新：让最近绘制的屏幕可见
        pygame.display.flip()

    def run_game(self):
        """游戏主循环"""
        while True:
            self._handle_check_events()
            if self.stats.game_active:
                self.ship.update()
                self._handle_update_bullets()
                self._handle_update_aliens()
            self._handle_update_screen()

if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()