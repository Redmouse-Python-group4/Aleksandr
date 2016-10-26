from datetime import datetime

#1 задание
mydate = 20010915
print(datetime.strptime(str(mydate), "%Y%m%d"))

#2 задание
month = 10
day = 14
year = 1993
print(datetime.strptime(str(year) + str(month) + str(day), '%Y%m%d'))

#3 задание
nowdate = datetime.today()
a = nowdate.replace(month=(nowdate.month-1), year=(nowdate.year+1)) 
b = a.replace(month=1, day=1)
c = (a-b)
print("День %s. %s день в этом году" %(a,c))

#4 задание
today = datetime.today() 
print(today)
k = today.replace(month=1, day=1)
print(k)
g = (today-k)
print("Сегодняшний день %s. %s по счету день в этом году" %(today,g))

#7 задание

newdate =  datetime.now()
mynewdate = datetime.strftime(newdate, '%d, %B, %Y')
print(mynewdate)