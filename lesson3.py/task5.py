list=[]
x = 0
y = 1
n = int(input('Введите число = '))
for i in range(n+1):
        list.append(x) 
        list.append(-x)
        x, y = y, x + y
list.sort()
print(list)