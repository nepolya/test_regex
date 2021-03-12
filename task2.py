from zipfile import ZipFile
import json
file_name='test.json.zip'
with ZipFile(file_name, 'r') as zip: 
    filename=zip.extract('test.json')

def find_key():
    f=open(filename, 'r', encoding='utf-8')
    text = json.load(f)
    spisok=[]
    for k, v in text.items():
        if isinstance(k, str):
            spisok.append(k)
        else:
            find_key()
    return spisok
print(find_key())
f.close()
