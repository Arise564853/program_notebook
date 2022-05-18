def 迭代(n):
    n1 = 1
    n2 = 1
    n3 = 1
    if n < 1:
        print("输入有误！")
        return -1
    while n-2 > 0:
        n3 = n2 + n1
        n1 = n2
        n2 = n3
        n -= 1
    return n3


def 递归法(months):
    if months < 3:
        return 1
    else:
        return 递归法(months - 1)+递归法(months - 2)