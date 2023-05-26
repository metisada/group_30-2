#Объявлеяем переменные с номерами месяцев:
day = int(input('День: '))
month = int(input('Порядковый номер месяца:' ))

if (month == 3 and day > 20 and day < 32 or month == 4 and day < 20):
       print('Овен')

elif (month == 4 and day > 19 and day < 31 or month == 5 and day < 21):
       print('Телец')

elif (month == 5 and day > 20 and day < 32 or month == 6 and day < 21):
       print('Близнецы')

elif (month == 6 and day > 20 and day < 31 or month == 7 and day < 23):
       print('Рак')

elif (month == 7 and day > 22 and day < 32 or month == 8 and day < 23):
       print('Лев')

elif (month == 8 and day > 22 and day < 32 or month == 9 and day < 23):
           print('Дева')

elif (month == 9 and day > 22 and day < 30 or month == 10 and day < 23):
           print('Весы')

elif (month == 10 and day > 22 and day < 31 or month == 11 and day < 22):
           print('Скорпион')

elif (month == 11 and day > 21 and day < 31 or month == 12 and day < 22):
           print('Стрелец')

elif (month == 12 and day and day < 32 or month == 1 and day < 20):
           print('Козерог')

elif (month == 1 and day > 19 and day < 32 or month == 2 and day < 19):
           print('Водолей')

elif (month == 2 and day > 18 and day < 29 or month == 3 and day < 21):
           print('Рыбы')

else:
    print('Несуществующая дата')
