lst = list(map(int, input("Введите числа через пробел :\n").split()))
second_lst = []
[second_lst.append(i) for i in lst if i not in second_lst]
second_lst.sort()
print(second_lst)