from printall import printer_loading
import os,  time


os.chdir(r'D:\Documents\Tencent Files\277038938\FileRecv')
for file in os.listdir():
    if file.endswith('.docx'):
        if "模板" not in file:
            for i in range(2):
                printer_loading(file)
                time.sleep(5)

