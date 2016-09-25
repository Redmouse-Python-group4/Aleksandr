stroka = "Самое;удобное;оборудование;для;науки;это;синхрофазатрон;с;лучевой;трубкой"
maxlen = 0
spisok = stroka.split(;)
for i in spisok:
      if len(i)>maxlen:
          maxlen = len(i)
      else:
         pass

for i in spisok:
    if len(i) == maxlen:
        print('Самое длинное слово в этой строке "%s"!'%i)
    else:
       pass