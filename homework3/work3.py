def lenword(s):
	s= s.split(' ')
	for word in s:
		print('Слово %s. Его длина %d символов!'%(word, len(word)))

stroka = input('Введите строку: ')
lenword(stroka)
