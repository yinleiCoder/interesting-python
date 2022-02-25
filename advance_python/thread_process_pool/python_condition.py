"""
线程同步——condition：
    条件变量，用于复杂的线程间同步。
"""
import threading
from threading import Lock, Condition

class Siri(threading.Thread):
    def __init__(self, cond):
        super().__init__(name='siri')
        self.cond = cond

    def run(self):
        with self.cond:
            self.cond.wait()
            print(f"{self.name}: 小爱同学!")
            self.cond.notify()
            self.cond.wait()
            print(f"{self.name}: 暂时没有，心里放不下其他人了!")

class MiTalk(threading.Thread):
    def __init__(self, cond):
        super().__init__(name='小爱')
        self.cond = cond

    def run(self):
        with self.cond:
            print(f"{self.name}: 嗨, siri!")
            self.cond.notify()
            self.cond.wait()
            print(f"{self.name}: 你现在身边有称心如意的女孩子吗？")
            self.cond.notify()

if __name__ == '__main__':
    cond = threading.Condition()
    xiaoai = MiTalk(cond)
    siri = Siri(cond)
    siri.start()
    xiaoai.start()
