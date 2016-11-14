#1 задание. Использование генератора списков.
def proverka(x):
	if x>=1 and x <=3:
		s=input('Введите строку: ')
		n=int(input('Введите число повторов: '))
		i = 0
		while i!=n:
			print(s)
			i+=1

	elif x>= 4 and x<= 6:
		m=int(input('Введите степень, в которую вы хотите возвести число: '))
		rez= x**m
		print('Вы возвели число %s в степень %s. И получили %s'%(x,m,rez))

	elif x >=7 and x<=9:
		count = 0
		while count !=10:
			x += 1
			count += 1
			print(x)
	else:
		print('Ой, что-то пошло не так! Вероятно ошибка ввода.')


x = int(input('Приветствую тебя, друже! Братуха введи число от 1 до 9: '))
proverka(x)
