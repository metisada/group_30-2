#Создаем переменные с названиями дней недели.
Mo = int(input("Введите расходы за ПН: "))
Tu = int(input("Введите расходы за ВТ: "))
We = int(input("Введите расходы за СР: "))
Th = int(input("Введите расходы за ЧТ: "))
Fr = int(input("Введите расходы за ПТ: "))
Sa = int(input("Введите расходы за СБ: "))
Su = int(input("Введите расходы за ВС: "))

sum_for_all_days = (Mo + Tu + We + Th + Fr + Sa + Su)
print("Сумма за все дни:", sum_for_all_days)




average_for_all_days = sum_for_all_days / 7
print("Среднее за все дни", round(average_for_all_days, 2))

