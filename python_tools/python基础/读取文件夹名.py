import pandas as pd
import os


path = 'C:/Users/Administrator/Desktop/待办/0730谭韵琦汽车吊检查'
f = open('C:/Users/Administrator/Desktop/车牌号.txt', 'a')
for i in os.listdir(path):
    print(i, file=f)
