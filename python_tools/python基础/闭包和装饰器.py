def a1(x):
    def a2(*args, **kwargs):
        print('开始')
        x(*args, **kwargs)
        print('结束')
    return a2


@a1
def a3(name1, name2, **kwargs):
    print(f'{name1},{name2}开始吃饭！')
    print(kwargs)


a3('孙兴华', '叶问', a=1, b=2, c=3)
