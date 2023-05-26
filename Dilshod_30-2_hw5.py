Geeks = {

    'address': 'Toktogula 175',

    'courses': ['Android', 'Backend', 'Frontend'],

    'bag': {'fails', 'errors', 'stack'}
}
del Geeks['bag']
Geeks['address'] = 'БЦ Victory, Ибраимова, 103 правое крыло, 4 этаж'
Geeks['Phone'] = '+996 507‒05‒20‒18'
Geeks['Instagram'] = 'geeks_edu'
Geeks['courses'] = set(Geeks['courses'] + ['iOS,', 'JS - front', 'Python - back', 'UX/UI', 'basics of programming'])
Geeks['Birthday'] = '2018-05'
print(len(Geeks['courses']))
for key, value in Geeks.items():
    print(f"{key}: {value}")