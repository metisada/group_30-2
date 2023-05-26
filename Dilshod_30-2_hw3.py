while True:
    Slovo = input('Введите слово: ')
    if Slovo == 'Раз, два, три - закончили':
        break

    Glasnye = range(1, 5)
    Soglasnye = range(6, 10)

    Glasnyh = 0
    Soglasnyh = 0

    for Nabor in Slovo:
        if Nabor.lower() in Glasnye:
            Glasnyh += 1
        elif Nabor.lower() in Soglasnye:
            Soglasnyh += 1

    Kolichestvo_bukv = Glasnyh + Soglasnyh

    print(f'Количество букв: {Kolichestvo_bukv}')
    print(f'Количество гласных букв: {Glasnyh}')
    print(f'Количество согласных букв: {Soglasnyh}')
    if Kolichestvo_bukv != 0:

        Procent_glasnyh = round(Glasnyh / Kolichestvo_bukv * 100, 2)
        Procent_soglasnyh = round(Soglasnyh / Kolichestvo_bukv * 100, 2)

    print(f'Процентное соотношение гласных и согласных букв: {Procent_glasnyh} / {Procent_soglasnyh}' )

else:
    print('Вы не ввели ни одну букву')
