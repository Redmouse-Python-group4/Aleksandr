stroka = input('Введите предложение: ')
print('Вы ввели следующее предложение:', stroka)

findword = input('Введите слово, которое необходимо найти: ')

if stroka.find(findword) >= 0:
	print('Получилось! Мы нашли слово', findword)
else:
	print('Упс! У нас не получается найти слово', findword)
