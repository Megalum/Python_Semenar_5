# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

string = input('Введите строку: ')
stringList = string.split()
string = ''
k = 0
while (k < len(stringList)):
    i = stringList[k]
    for j in range(len(i)):
        if (i[j] == 'а') & (j < (len(i) - 2)):
            if (i[j+1] == 'б') & (i[j+2] == 'в'):
                stringList.remove(i)
                k -= 1
    k += 1
for i in stringList:
    string += i + ' '
print(string)
