from printall import printer_loading
import os,  time


os.chdir(r'F:\测厚')
for i in range(2):
    for file in os.listdir():
        if file.endswith('.docx'):
            if "模板" not in file:
                printer_loading(file)
                time.sleep(5)

