import os
from win32com.client import Dispatch
import shutil


app = Dispatch('Word.Application')

xlApp = Dispatch("Excel.Application")

xlBook = xlApp.Workbooks.Open('G:/2021原始记录/2021年原始记录领号.xlsm')
sheets = ["电梯", "塔机", "井架"]
for sheet_name in sheets:
    i = 2
    while i <= 200:
        program = xlBook.Worksheets(sheet_name).Cells(i, 4).Value
        if sheet_name == "电梯":
            test_date = xlBook.Worksheets(sheet_name).Cells(i, 15).Value[:2] + xlBook.Worksheets(sheet_name).Cells(i, 15).Value[3:5]
        elif sheet_name == "塔机":
            test_date = xlBook.Worksheets(sheet_name).Cells(i, 18).Value + xlBook.Worksheets(sheet_name).Cells(i, 18).Value[3:5]
        elif sheet_name == "井架":
            test_date = xlBook.Worksheets(sheet_name).Cells(i, 15).Value + xlBook.Worksheets(sheet_name).Cells(i, 15).Value[3:5]
        for root, dirs, files in os.walk("E:/2021年起重工地"):
            for dir_name in dirs:
                if program in dir_name and dir_name.startswith(test_date) and sheet_name in dir_name:
                    position = dir_name.rfind('-')
                    print(root + '\\' + dir_name)
                    shutil.copytree(root + '\\' + dir_name, f'G:/2021原始记录/{sheet_name}/{dir_name[:position + 1]}{i-1}')
        i += 1
app.Quit()
xlBook.Close()
xlApp.Quit()
