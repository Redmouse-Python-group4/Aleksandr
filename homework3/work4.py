#Написать функцию в которую можно передать сколько угодно значений и оно возводит каждое последующее число в степень предыдущего (первое значение возводим в степень один)

def funcstepen(*args):
	massive = [x for x in args]
	count = 0
	for x in massive:
		if count == 0:
			print(x)
		elif count > 0:
			print(x**massive[count-1])
		else:
			print('Больше нечего выводить!')
		count +=1
print(funcstepen(3,2,3,4,5))
