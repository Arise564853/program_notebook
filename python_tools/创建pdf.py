from PIL import Image
import os
from fpdf import FPDF
import tkinter as tk
from tkinter import filedialog


def makepdf(pdffilename, listpages):
    cover = Image.open(listpages[0])
    width, height = cover.size
    pdf = FPDF(unit="pt", format=[width, height])
    for page in listpages:
        pdf.add_page()
        pdf.image(page, 0, 0)
    pdf.output(pdffilename, "F")


if __name__ == '__main__':
    root = tk.Tk()
    root.withdraw()
    folderpath = filedialog.askdirectory()
    listpages = []
    if folderpath != "":
        os.chdir(folderpath)
        for picture in os.listdir():
            if picture.endswith('.jpg'):
                listpages.append(picture)
        makepdf(f'{folderpath[folderpath.rfind("/") + 1:]}.pdf', listpages)
        print(f'创建完成！')
