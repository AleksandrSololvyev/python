n = [1, 4, 7]
list=[]
count = 1
number = int(input('Введите число = '))
while count <= number:
    x = count*-1
    list.append(x)
    x = count
    list.append(x)
    count += 1
list.sort()
print(list)
num_list = 1
mult = 1
for i in n:
    num_list = list[i]
    mult = mult * num_list
print(mult)