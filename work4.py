import re
string = input("Введите слово: ")
# Находим 1 и последнюю букву в слове
result = re.findall(r'^\w+', string) + re.findall(r'\w+$', string)
# Реверс
if string == result[0] or string == result[1]:
    tmp = 1
    l = []
    for i in string:
        l.append(string[len(string) - tmp])
        tmp += 1
    l = "".join(l)
print (l)