import PyPDF2
import textract

filename = 'Xiao'
pdfFileObj = open(filename, 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

num_pages = pdfReader.num_Pages
count = 0
text = ""

while count < num_pages:
    pageObj = pdfReader.getPage(count)
    count += 1
    text += pageObj.extractText()

print(text)
