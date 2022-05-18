#!/usr/bin/env python
# -*- coding: utf-8 -*-
_author_ = '吴晓南'
import os


os.chdir('E:/2021年起重工地')
file = []
for a, b, c in os.walk('E:/2021年起重工地'):
    for i in b:
        if '桑水初' in i:
            print(i)
            file.append(i)
print(len(file))
