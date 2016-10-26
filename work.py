from abc import ABCMeta, abstractmethod, abstractproperty

class MyMetaClass():
	__metaclass__=ABCMeta
	def __init__():
		x = 0


class PackFunc(MyMetaClass):
	def __init__(self):
		x = int(input('Приветствую тебя, друже! Братуха введи число от 1 до 9: '))
		if x>=1 and x <=3:
			self.povtor()
		elif x>= 4 and x<= 6: ### Узнать. Почему не нужно здесь self.x. Т.к с ним не работает.
			self.stepen(x)
		elif x >=7 and x<=9:
			self.count(x)
		else:
			print('Ой, что-то пошло не так! Вероятно ошибка ввода.')
	
	def povtor(self):
		s=input('Введите строку: ')
		n=int(input('Введите число повторов: '))
		i = 0
		while i!=n:
			print(s)
			i+=1

	def stepen(self, x):
		m=int(input('Введите степень, в которую вы хотите возвести число: '))
		rez= x**m
		print('Вы возвели число %s в степень %s. И получили %s'%(x,m,rez))

	def count(self, x):
		count = 0
		while count !=10:
			x += 1
			count += 1
			print(x)

class MyThirdClass(PackFunc, MyMetaClass):
	def __init__(self):
		self.x = 5
		
mygame = MyThirdClass()