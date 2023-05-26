#if - если (используется 1 раз в блоке)
#elif - иначе
#else - прочее (используется 1 раз в блоке)

time = 'day'

if time == 'morning':
    print('good morning')
elif time == 'day':
    print('good afternoon')
elif time == 'evening':
    print('good evening')
else:
    print('hello')
