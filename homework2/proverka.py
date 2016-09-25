stroka = "Самое удобное оборудование для науки это синхрофазатрон с лучевой трубкой"
maxlength = 0
spisok = stroka.split()
for i in spisok:
      if len(i)>maxlength:
          maxlength = len(i)
      else:
         pass

for i in spisok:
    if len(i) == maxlength:
        print i
    else:
       pass