import os
from datetime import *
#Написать программу которая в интерактивном режиме просит ввести путь к папкам. 
#Затем просит ввести название папки/файла. Затем если по заданному пути находится файл/папка то выводить:
# ее полный путь, размер, тип объекта (файл или директория), дату создания изменения объекта.

yourpath = input('Введите путь к папкам: ')
papkaname = input('Введите название папки или файла: ')

spisok = os.listdir(yourpath)
fullpath = yourpath + papkaname

for i in spisok:
	if i == papkaname:
		print(fullpath)
		print('Размер %s %s'%(os.stat(fullpath).st_size, 'байт'))
		print('Дата создания: %s'%(ds.stat(fullpath).st_ctime))
		print('Дата изменения: %s'%(os.stat(fullpath).st_mtime))


#http://stackoverflow.com/questions/2555904/python-dealing-with-dates-and-times