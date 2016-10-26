import json
myfile = json.load(open('tovar.json', 'r'))
shtuka = 0
para = 0
for name_product in myfile.keys():
	if myfile[name_product]['tip'] == 'шт':
		shtuka +=1
	elif myfile[name_product]['tip'] == 'пара':
		para +=1

print('Количество штучного товара', shtuka)
print('Количество парного товара', para)


kolinfo = {'Количество штучного товара': shtuka, 'Количество парного товара' : para}
info = json.dumps(kolinfo)

with open('jsonrez.json', 'w') as newfile:
	newfile.write(info)

newfile.close()
