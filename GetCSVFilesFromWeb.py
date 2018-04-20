import codecs
import csv
from io import StringIO
from urllib.request import urlopen

data = urlopen("http://pythonscraping.com/files/MontyPythonAlbums.csv").read().decode('ascii', 'ignore')
dataFile = StringIO(data)
# csvReader = csv.reader(dataFile)
csvReader = csv.DictReader(dataFile)
print(csvReader.fieldnames)
print('-----------------------------------------------------')
for row in csvReader:
    print(row)

def generate_csv_file():
    with codecs.open(filename='data.csv', encoding='UTF-8', mode='wb') as f:
        csv_writer = csv.writer(f, dialect='excel')
        csv_writer.writerow(['a', 'b', 'c'])
        csv_writer.writerow(['A', 'B', 'C'])

generate_csv_file()