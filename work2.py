class MyPack():
	def __init__(self, x):
		if x > 0 and x <7:
			self.detsad()
		elif x >= 7 and x <= 18:
			self.school()
		elif x >=18 and x <= 25:
			self.univer()
		elif x >= 25 and x < 60:
			self.job()
		elif x >=60 and x <=120:
			self.yourchoice()
		else:
			i = 5
			while i != 0:
				print('Ты что не человек? Или ты уникальный представитель книги рекордов Гиннеса?')
				i -=1

	def detsad(self):
		print('Вам пора в детский сад!')

	def school(self):
		print('Вам пора уже в школу!')

	def univer(self):
		print('Вам в профессиональное учебное заведение.')

	def job(self):
		print('Вам пора на работу!')

	def yourchoice(self):
		print('Вам предоставляется выбор!')
		while True:
			choice = int(input('1 - Я хочу уже помереть. 2 - А у вас есть трансплантация органов? (введите 1 или 2): '))
			if choice == 1:
				print('Жалко! А ведь многие в вашем возрасте только начинают жить!')
				break
			elif choice == 2:
				print('Пссс, тихо! Вот тебе телефончик Бакыта, возможно он тебе поможет')
				break
			else:
				print('Упс! Походу вы ввели что-то не так! Вам нужно ввести цифру 1 или 2, в зависимости от выбора!')


print('Общество в начале XX1 века')
howold = int(input('Сколько вам полных лет: '))

mybook = MyPack(howold)