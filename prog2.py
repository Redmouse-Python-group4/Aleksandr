print('Общество в начале XX1 века')

howold = int(input('Сколько вам полных лет: '))

if howold > 0 and howold <7:
	print('Вам пора в детский сад!')
elif howold >=18 and howold <= 25:
	print('Вам в профессиональное учебное заведение.')
elif howold >= 25 and howold <= 60:
	print('Вам пора на работу!')
elif howold >=60 and howold <=120:
	print()