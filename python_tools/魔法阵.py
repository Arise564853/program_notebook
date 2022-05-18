import turtle as t
import math

t.screensize(400, 300, 'black')
t.tracer(False)
t.color("yellow")


def a(d=0):
    t.up()
    t.speed(1)
    t.goto(0, -200)
    t.down()
    t.circle(200)
    t.up()

    t.home()

    t.goto(0, -300)
    t.down()
    t.circle(300)
    t.up()

    t.home()

    t.right(90)

    t.left(90)

    n = 0
    while n < 12:
        # print(30*n+d)
        t.right(30 * n + d)
        t.forward(200)
        t.down()
        t.forward(100)

        t.up()
        t.home()
        n += 1

    t.home()
    t.left(90)
    t.left(d)
    t.forward(200)

    # 六边形
    t.down()
    t.left(180)
    t.left(30)  # -------------
    t.forward(345)

    t.right(30)
    t.right(90)
    t.forward(345)

    t.right(90)
    t.right(30)  # -------------
    t.forward(345)

    t.up()
    t.home()
    t.right(90)  # -------------
    t.forward(200)

    t.home()
    t.left(90)
    t.left(d)
    t.left(180)
    t.forward(200)

    t.right(180)

    t.down()
    t.left(30)  # -------------
    t.forward(345)

    t.right(30)
    t.right(90)  # -------------
    t.forward(345)

    t.right(90)
    t.right(30)  # -------------
    t.forward(345)
    t.up()

    t.home()
    t.left(90)
    t.left(d)
    t.left(90)
    t.forward(200)

    t.right(180)
    t.down()
    t.left(30)
    t.forward(345)
    t.right(30)
    t.right(90)
    t.forward(345)
    t.right(30)
    t.right(90)
    t.forward(345)
    t.up()

    t.home()
    t.left(90)
    t.left(d)
    t.left(180 + 90)
    t.forward(200)
    t.right(180)
    t.down()
    t.left(30)
    t.forward(345)
    t.right(30)
    t.right(90)
    t.forward(345)
    t.right(30)
    t.right(90)
    t.forward(345)
    t.up()

    t.home()

    t.backward(30)
    t.down()
    t.write("奥利给！", font=("Microsoft JhengHei", 24))
    t.up()


def g():
    n = 0
    while 1:
        if n == 361:
            n = 0
        a(n)
        n += 1
        t.clear()


g()
