from printall import printer_loading
import os,  time


os.chdir(r'C:\Users\Administrator\Desktop\2021年自动模板')
for file in os.listdir():
    if file.endswith('.doc'):
        if "模板" not in file and "合格证" not in file:
            for i in range(2):
                printer_loading(file)
                time.sleep(5)

