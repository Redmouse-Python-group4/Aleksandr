print('Программа поиска и выделения самого короткого словая в строке')
znak = input('Каким знаком вы бы хотели выделить самое короткое слово: ')

stroka = "Самое удобное оборудование для науки это синхрофазатрон"
maxlen = 0
spisok = stroka.split()
for i in spisok:
      if len(i)<maxlen:
          maxlen = len(i)
      else:
         pass

for i in spisok:
    if len(i) == maxlen:
    	maxlen = len(i)
    	findword = znak+i+znak
    	print(findword)
        #stroka.replace(i,findword)
        #print(stroka)
    else:
       pass