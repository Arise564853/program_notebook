class Yewen(object):
    def __init__(self):
        self.kongfu = '咏春'

    def way(self):
        print(f'使用功夫{self.kongfu}')


class Brucelee(Yewen):
    def __init__(self):
        self.kongfu = '截拳道'

    def way(self):
        print(f'使用功夫{self.kongfu}')


class Sunxhua(Brucelee):
    pass


model = Sunxhua()
model.way()
print(Sunxhua.__mro__)