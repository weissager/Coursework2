#from elasticsearch import Elasticsearch 
import openpyxl
import json
import csv 
#es=Elasticsearch(['localhost:9200'])

def FormatText(string): #Форматирование текста
    string = string.lower()
    string = string.replace('.',' ')
    string = string.replace(',',' ')
    string = string.replace(';',' ')
    string = string.replace(':',' ')
    string = string.replace('-',' ')
    string = string.replace('\n',' ')
    string = string.replace('  ',' ')
    return string

wb=openpyxl.load_workbook(filename = 'Компетенции.xlsx')
sheet = wb['Main']
i=1

#while(i<=35):  #формирование базы на основе таблицы
   # item = {
     #'Компетенция' : sheet['A'+str(i)].value,
    # 'Название' : sheet['B'+str(i)].value,
     #'Содержание' : sheet['C'+str(i)].value,
    # }
   # es.index(index = 'main', body = item, doc_type = 'list', id = i)
   # i=i+1

#print ('Введите текст для поиска')
#search = input()
#res = es.search(index = 'main',body={'query': {'fuzzy': {'Содержание' : search}}}) #нечёткий поиск
#ToOut=json.dumps(res, ensure_ascii=False, sort_keys=True, indent=4) #форматированный вывод
#print(ToOut)

file = open('ForSplitTest.txt','r')
text = file.read()
file.close()

text = FormatText(text)
search = FormatText(text) #ИЗМЕНЕНО НА TEXT

splittext = text.split()
splitsearch = search.split()
searchlist = list()
textlist = list()

#избавляемся от лишних элементов
for item in splitsearch:    
    if (len(item)>3):
        item = item[0:-1]
        searchlist.append(item) 

for item in splittext:    
    if (len(item)>3):
        item = item[0:-1]
        textlist.append(item)        



#избавляемся от повторов
textlist=set(textlist)
searchlist=set(searchlist)

end_chance = 0.0
count = 0

#сравнение и расстановка весов для поиска
for item in textlist:   
    for searchitem in searchlist:
        chance = 0
        if (item==searchitem):
                 print("1" + item + ' ' + searchitem)
                 chance = 1
                 end_chance+=chance
                 count+=1
                 break

        elif (item==searchitem[0:-int(len(item)*0.2)]):
                 print("0.8"+ item + ' ' + searchitem)
                 if (chance < 0.8) : chance = 0.8
                 end_chance+=chance
                 count+=1
                 break

        elif (item[0:-int(len(item)*0.2)]==searchitem):
                 print("0.8"+ item + ' ' + searchitem)
                 if (chance < 0.8) : chance = 0.8
                 end_chance+=chance
                 count+=1                 
                 break

        elif (item[0:-int(len(item)*0.2)]==searchitem[0:-int(len(item)*0.2)]):
                 print("0.64"+ item + ' ' + searchitem)
                 if (chance < 0.64) : chance = 0.64
                 end_chance+=chance
                 count+=1                 
                 break  

        elif (item==searchitem[0:-int(len(item)*0.4)]):
                 print("0.6"+ item + ' ' + searchitem)
                 if (chance < 0.6) : chance = 0.6
                 end_chance+=chance
                 count+=1                 
                 break

        elif (item[0:-int(len(item)*0.4)]==searchitem):
                 print("0.6"+ item + ' ' + searchitem)
                 if (chance < 0.6) : chance = 0.6
                 end_chance+=chance
                 count+=1                
                 break

        elif (item[0:-int(len(item)*0.2)]==searchitem[0:-int(len(item)*0.4)]):
                 print("0.48"+ item + ' ' + searchitem)
                 if (chance < 0.48) : chance = 0.48
                 end_chance+=chance
                 count+=1                 
                 break
                    
        elif (item[0:-int(len(item)*0.4)]==searchitem[0:-int(len(item)*0.2)]):
                 print("0.48"+ item + ' ' + searchitem)
                 if (chance < 0.48) : chance = 0.48
                 end_chance+=chance
                 count+=1               
                 break

        elif (item==searchitem[0:-int(len(item)*0.6)]):
                 print("0.4"+ item + ' ' + searchitem)
                 if (chance < 0.4) : chance = 0.4
                 end_chance+=chance
                 count+=1                 
                 break

        elif (item[0:-int(len(item)*0.6)]==searchitem):
                 print("0.4"+ item + ' ' + searchitem)
                 if (chance < 0.4) : chance = 0.4
                 end_chance+=chance
                 count+=1                 
                 break

        elif (item[0:-int(len(item)*0.4)]==searchitem[0:-int(len(item)*0.4)]):
                 print("0.36"+ item + ' ' + searchitem)
                 if (chance < 0.36) : chance = 0.36
                 end_chance+=chance
                 count+=1                 
                 break  

        elif (item[0:-int(len(item)*0.2)]==searchitem[0:-int(len(item)*0.6)]):
                 print("0.32"+ item + ' ' + searchitem)
                 if (chance < 0.32) : chance = 0.32
                 end_chance+=chance
                 count+=1                 
                 break  
        
        elif (item[0:-int(len(item)*0.6)]==searchitem[0:-int(len(item)*0.2)]):
                 print("0.32"+ item + ' ' + searchitem)
                 if (chance < 0.32) : chance = 0.32
                 end_chance+=chance
                 count+=1               
                 break

        elif (item[0:-int(len(item)*0.4)]==searchitem[0:-int(len(item)*0.6)]):
                 print("0.24"+ item + ' ' + searchitem)
                 if (chance < 0.24) : chance = 0.24
                 end_chance+=chance
                 count+=1                 
                 break

        elif (item[0:-int(len(item)*0.6)]==searchitem[0:-int(len(item)*0.4)]):
                 print("0.24"+ item + ' ' + searchitem)
                 if (chance < 0.24) : chance = 0.24
                 end_chance+=chance
                 count+=1                 
                 break

        elif (item==searchitem[0:-int(len(item)*0.8)]):
                 print("0.2"+ item + ' ' + searchitem)
                 if (chance < 0.2) : chance = 0.2
                 end_chance+=chance
                 count+=1                
                 break

        elif (item[0:-int(len(item)*0.8)]==searchitem):
                 print("0.2"+ item + ' ' + searchitem)
                 if (chance < 0.2) : chance = 0.2
                 end_chance+=chance
                 count+=1                 
                 break

        elif (item[0:-int(len(item)*0.6)]==searchitem[0:-int(len(item)*0.6)]):
                 print("0.16"+ item + ' ' + searchitem)
                 if (chance < 0.16) : chance = 0.16
                 end_chance+=chance
                 count+=1                
                 break  

        elif (item[0:-int(len(item)*0.2)]==searchitem[0:-int(len(item)*0.8)]):
                 print("0.16"+ item + ' ' + searchitem)
                 if (chance < 0.16) : chance = 0.16
                 end_chance+=chance
                 count+=1                 
                 break  

        elif (item[0:-int(len(item)*0.8)]==searchitem[0:-int(len(item)*0.2)]):
                 print("0.16"+ item + ' ' + searchitem)
                 if (chance < 0.16) : chance = 0.16
                 end_chance+=chance
                 count+=1                 
                 break

        elif (item[0:-int(len(item)*0.8)]==searchitem[0:-int(len(item)*0.4)]):
                 print("0.12"+ item + ' ' + searchitem)
                 if (chance < 0.12) : chance = 0.12
                 end_chance+=chance
                 count+=1                 
                 break

        elif (item[0:-int(len(item)*0.4)]==searchitem[0:-int(len(item)*0.8)]):
                 print("0.12"+ item + ' ' + searchitem)
                 if (chance < 0.12) : chance = 0.12
                 end_chance+=chance
                 count+=1                 
                 break

        elif (item[0:-int(len(item)*0.6)]==searchitem[0:-int(len(item)*0.8)]):
                 print("0.08"+ item + ' ' + searchitem)
                 if (chance < 0.08) : chance = 0.08
                 end_chance+=chance
                 count+=1                 
                 break

        elif (item[0:-int(len(item)*0.8)]==searchitem[0:-int(len(item)*0.6)]):
                 print("0.08"+ item + ' ' + searchitem)
                 if (chance < 0.08) : chance = 0.08
                 end_chance+=chance
                 count+=1                
                 break

        elif (item[0:-int(len(item)*0.8)]==searchitem[0:-int(len(item)*0.8)]):
                 print("0.04"+ item + ' ' + searchitem)
                 if (chance < 0.04) : chance = 0.04
                 end_chance+=chance
                 count+=1                 
                 break 


#if ((end_chance and count) !=0):
print('Соответствие: '+ str(end_chance) +' '+ str(count)+' '+str(end_chance/count))                 


#f = open('end.txt','w')
#f.writelines(result)
#f.close()
