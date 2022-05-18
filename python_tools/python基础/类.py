class 月饼():
    def __init__(self):
        self.时间 = 0
        self.状态 = '生的'
        self.调料 = []

    def 烘焙时间(self, 时间):
        self.时间 += 时间
        if 0 <= self.时间 < 3:
            self.状态 = '生的'
        elif 3 <= self.状态 < 5:
            self.状态 = '半生不熟'
        elif 5 <= self.状态 < 8:
            self.状态 = '熟了'
        else:
            self.状态 = '糊了'

    def 添加调料(self, 调料):
        self.调料.extend(调料)

    def __str__(self):
        return f'这批月饼的烘烤时间是{self.时间}，状态是{self.状态}，调料有{self.调料}。'


model = 月饼()
model.烘焙时间(2)
model.添加调料(['红豆沙', '蔓越莓'])
print(model)
