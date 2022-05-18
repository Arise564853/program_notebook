import PyPDF2


pdfFiles = ['09月20日富政储出【2020】36号地块项目.pdf', '09月20日富政储出【2020】36号地块项目合格证.pdf']
pdfWrite = PyPDF2.PdfFileWriter()
for file in pdfFiles:
    pdfobj = open(file, 'rb')
    pdfreader = PyPDF2.PdfFileReader(pdfobj, strict=False)
    for page in range(pdfreader.numPages):
        pageobj = pdfreader.getPage(page)
        pdfWrite.addPage(pageobj)

pdfoutput = open('合并.pdf', 'wb')
pdfWrite.write(pdfoutput)
pdfoutput.close()
