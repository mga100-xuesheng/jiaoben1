import json

file = open('ceshi.json', 'r', encoding='utf-8')
print(file)
data1 = json.load(file)
print(data1)
print(data1['name'])
print(data1['ceshi']['name'])
file.close()
# file = open('ceshi.json','w', encoding='utf-8')
# data = {"name":"ceshi",
#         "data":"123",
#         "ceshi":{"name":123456}}
# print(data['name'])
# json.dump(data,file)
# file.close()
