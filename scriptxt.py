myfile = open('tovar.txt', 'r')
shtuka = 0
para = 0
total = 0
totalpara = 0
totalshtuka =0

for line in myfile:
	tmp = line.strip()
	tmp = tmp.split(' ')
	total += int(tmp[1])
	if tmp[2] == 'шт':
		shtuka +=1
		totalshtuka += int(tmp[1])
	elif tmp[2] == 'пара':
		para +=1
		totalpara += int(tmp[1])
	else:
		print('Ошибка. Что-то видать пошло не так.')

myfile.close()
myfile = open('tovar.txt', 'a')
myfile.write('\n' + '''Общее количество товара в нашем магазине %d. Наименований пнарных товаров %d. Наименований штучных товаров %d.
	Оставшееся количество парного товара %d (пар) на складе. Оставшееся количество штучного товара %d (шт) на складе.
	'''%(total, para, shtuka, totalpara, totalshtuka))