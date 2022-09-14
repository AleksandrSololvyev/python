list = [2, 3, 5, 9, 3]
summ = 0
x = 0
for i in range(len(list)):
    if i%2 != 0:
        x = list[i]
        summ = summ + x
print(summ)