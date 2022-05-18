import time


class Clock:
    def __init__(self, start_time=0, stop_time=0):
        self.start_time = start_time
        self.stop_time = stop_time
        self.t = 0

    def start(self):
        print("计时开始...")
        self.start_time = time.time()

    def stop(self):
        if self.start_time == 0:
            print('提示：请先调用start()开始计时')
        else:
            print("计时结束!")
            self.stop_time = time.time()
            self.t = int(self.stop_time-self.start_time)

    def __repr__(self):
        if self.t == 0:
            return '未开始计时'
        else:
            return f'总共运行了{self.t}秒！'

    def clear(self):
        self.start_time = 0
        self.stop_time = 0
        self.t = 0
