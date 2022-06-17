from printall import printer_loading
import os
import time
import tkinter as tk
from tkinter import filedialog


try:
    printNum = int(input("输入打印份数："))
except Exception as errorMessage:
    print(f'出现错误,{errorMessage}')
else:
    root = tk.Tk()
    root.withdraw()
    folderPath = filedialog.askdirectory()
    if folderPath != "":
        os.chdir(folderPath)
        for i in range(printNum):
            for file in os.listdir():
                if file.endswith(('合格证.docx', '合格证.doc')):
                    printer_loading(file)
                    time.sleep(5)

