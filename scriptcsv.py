import csv
shtuka = 0
para = 0
total = 0
totalpara = 0
totalshtuka =0
with open('tovar.csv') as myfile:
	openfile = csv.reader(myfile)
	for line in myfile:
		tmp = line.strip()
		tmp = tmp.split(',')
		total += int(tmp[1])
		if tmp[2] == 'шт':
			shtuka +=1
			totalshtuka += int(tmp[1])
		elif tmp[2] == 'пара':
			para +=1
			totalpara += int(tmp[1])
		else:
			print('Ошибка. Что-то видать пошло не так.')
print('''Общее количество товара в нашем магазине %d. Наименований пнарных товаров %d. Наименований штучных товаров %d.
	Оставшееся количество парного товара %d (пар) на складе. Оставшееся количество штучного товара %d (шт) на складе.
	'''%(total, para, shtuka, totalpara, totalshtuka))
myfile.close()

with open('tovar.csv', 'w') as myfile:
	writer = csv.writer(myfile)
	writer.writerows([[
		'Общее количество товара в нашем магазине',str(total), 'Наименований парных товаров',str(para), 'Наименований штучных товаров', str(shtuka),'Оставшееся количество парного товара на складе.',str(totalpara), 'Оставшееся количество штучного товара на складе.',str(totalshtuka)
	]])
	print(total)
	print(totalpara)
	print(totalshtuka)
myfile.close()


#Работает.