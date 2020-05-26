from elasticsearch import Elasticsearch 
import openpyxl
import json
import csv 
es=Elasticsearch(['localhost:9200'])

wb=openpyxl.load_workbook(filename = 'D:\Python\Анализ компетенций\Компетенции.xlsx')
sheet = wb['Main']
i=1

while(i<=35):
    item = {
     'Компетенция' : sheet['A'+str(i)].value,
     'Название' : sheet['B'+str(i)].value,
     'Содержание' : sheet['C'+str(i)].value,
     }
    es.index(index = 'main', body = item, doc_type = 'list', id = i)
    i=i+1

print ('текст для поиска')
search = input()
res = es.search(index = 'main',body={'query': {'fuzzy': {'Содержание' : search}}})
ToOut=json.dumps(res, ensure_ascii=False, sort_keys=True, indent=4)
print(ToOut)

f=open('out.txt','w')
f.write(ToOut)
f.close()