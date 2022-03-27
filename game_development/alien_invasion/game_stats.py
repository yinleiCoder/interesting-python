"""
跟踪游戏统计信息来记录飞船被撞了多少次
"""

class GameStats:
    """跟踪游戏的统计信息"""

    def __init__(self, ai_game):
        self.settings = ai_game.settings
        self.reset_stats()
        self.game_active = False
        # 最高得分
        self.high_score = 0

    def reset_stats(self):
        """初始化在游戏运行期间可能变化的统计信息"""
        self.ships_left = self.settings.ship_limit
        self.game_active = True
        self.score = 0
        self.level= 1
