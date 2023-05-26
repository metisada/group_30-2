# def func(*args):
#     operation = 1
#     for number in args:
#         operation *= number
#     return operation
#
# primer_chisel = [1, 2, 3]
#
# result = func(*primer_chisel)
#
# print(result)


def is_mirror(slovo, hello_str='hello'):
    slovo = slovo.lower()
    hello_str = hello_str.lower()
    if slovo == slovo[::-1] and hello_str not in slovo:
        return True
    else:
        return False


print(is_mirror('qweewq'))

#
# def calc(numb1, operator, numb2):
#     if operator == '+':
#         return numb1 + numb2
#     elif operator == '-':
#         return numb1 - numb2
#     elif operator == '/':
#         return numb1 / numb2
#     elif operator == '*':
#         return numb1 * numb2
#     elif operator == '%':
#         return numb1 % numb2
#     elif operator == '**':
#         return numb1 ** numb2
#     else:
#         print('Неправильный оператор или неверный синтаксис')
#
# result = calc(1, '+', 2)
# print(result)