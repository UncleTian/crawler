from io import BytesIO
from urllib.request import urlopen
from zipfile import ZipFile

wordFile = urlopen("http://pythonscraping.com/pages/AWordDocument.docx").read()
wordFile = BytesIO(wordFile)
document = ZipFile(wordFile)

xml_content = document.read('word/document.xml')
print(xml_content.decode('utf-8'))
