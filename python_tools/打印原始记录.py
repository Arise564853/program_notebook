import os
import shutil


os.chdir('G:/2021原始记录')
for a in os.listdir():
    if os.path.isdir(os.getcwd() + '/' + a):
        for b in os.listdir(os.getcwd() + '/' + a):
            if b.endswith('.doc'):
                for c in os.listdir(os.getcwd() + '/' + a):
                    if not c.endswith('.doc'):
                        position = c.rfind('-')
                        if str(int(b[7:11])) in c[position + 1:].split(','):
                            shutil.move(os.getcwd() + '/' + a + '/' + b, os.getcwd() + '/' + a + '/' + c)
