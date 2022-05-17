import PyPDF2, os
"""
从多个pdf中合并选择:
    需要将几十个pdf文档合并为一个pdf文档，每个文档都有一个封面作为第一页，但是不希望合并后的文档中重复出现这些封面。
    1. 找到当前工作目录中的所有pdf文档
    2.按文档名排序，这样就能有序的添加这些pdf
    3. 除开第一页之外，将每个pdf的所有页面写入输出的文档
PyPDF2: pip install PyPDF2
"""
pdfFiles = []
for filename in os.listdir('.'):
    if filename.endswith('.pdf'):
        pdfFiles.append(filename)
pdfFiles.sort(key=str.lower)
pdfWriter = PyPDF2.PdfFileWriter()

for filename in pdfFiles:
    with open(filename, 'rb') as pdfFileObj:
        pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
        if pdfReader.isEncrypted:
            pdfReader.decrypt('yinlei')
        for pageNum in range(0, pdfReader.numPages):
            pageObj = pdfReader.getPage(pageNum)
            # print(pageObj.extractText())
            pdfWriter.addPage(pageObj)

with open('all_combine_pdf.pdf', 'wb') as resultPdf:
    pdfWriter.write(resultPdf)



# 旋转pdf页面
# with open('油票.pdf', 'rb') as oilFile:
#     pdfReader = PyPDF2.PdfFileReader(oilFile)
#     page = pdfReader.getPage(0)
#     page.rotateClockwise(90)
#     pdfWriter = PyPDF2.PdfFileWriter()
#     pdfWriter.addPage(page)
#     with open('rotatedPage.pdf', 'wb') as resultFile:
#         pdfWriter.write(resultFile)

# 叠加页面(适合添加水印)
# with open('油票.pdf', 'rb') as oilFile:
#     pdfReader = PyPDF2.PdfFileReader(oilFile)
#     oilFirstPage = pdfReader.getPage(0)
#     with open('watermask.pdf', 'rb') as watermaskFile:
#         pdfWatermarkReader = PyPDF2.PdfFileReader(watermaskFile)
#         oilFirstPage.mergePage(pdfWatermarkReader.getPage(0))
#         pdfWriter = PyPDF2.PdfFileWriter()
#         pdfWriter.addPage(oilFirstPage)
#         for pageNum in range(1, pdfReader.numPages):
#             pageObj = pdfReader.getPage(pageNum)
#             pdfWriter.addPage(pageObj)
#         pdfWriter.encrypt('yinlei')# 加密
#         with open('watermarkedCover.pdf', 'wb') as resultPdfFile:
#             pdfWriter.write(resultPdfFile)

# with open('油票.pdf', 'rb') as pdfFileObj:
#     pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
#     if pdfReader.isEncrypted:
#         pdfReader.decrypt('解锁pdf锁定的密钥')
#     print(pdfReader.numPages)
#     pageObj = pdfReader.getPage(0)
#     print(pageObj.extractText())


