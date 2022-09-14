number = input('Введите вещественное число = ')
summ = 0
for i in number:
    if i.isdigit():
        summ = summ +int(i)
print(f'Сумма цифр числа = {summ}')        