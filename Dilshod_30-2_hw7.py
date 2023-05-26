ten = [i for i in range(1, 11)]
#
# evens_filter = list(filter(lambda e: e % 2 == 0, ten))
# evens_map = list(map(lambda e: e ** 2, evens_filter))
# print(ten)
# print(evens_filter)
# print(evens_map)

def func(index, lst=None):
    if lst is None:
        lst = [i for i in range(1, 11)]
    while True:
        try:
            item = lst[index]
            print(item)
            break
        except IndexError:
            print('Index out of range.')
            index = int(input('Enter an index:' ))
index = int(input('Enter an index:'))

func(index, lst=ten)