import turtle as t

t.screensize(400, 300, 'red')
t.tracer(False)
t.color("yellow", "blue")


def blood_eye():
    t.up()
    t.goto(0, -20)
    t.down()
    t.circle(20)
    t.up()
    t.goto(0, -200)
    t.down()
    t.circle(200)
    t.up()
    t.home()
    t.down()
    for i in range(6):
        t.right(90 + 60 * i)
        t.up()
        t.forward(200)
        t.down()
        t.right(135)
        t.circle(-200 * (2 ** 0.5), 90)
        t.up()
        t.home()


def a(d=0):
    # 偏转
    # 画一个风车
    start = 0 + d
    start += d
    for i in range(4):
        t.left(start + i * 90)
        t.forward(200)
        t.left(210)
        t.circle(-200, 60)
        t.home()


def g():
    n = 1
    while True:
        if n <= 360:
            a(n * 1)
            t.update()
            t.clear()
            n += 1
        else:
            n = 1


while True:
    blood_eye()
    t.update()
    t.clear()
# if __name__ == '__main__':
#     print(timeit.timeit('a()', setup="from __main__ import a", number=100))
