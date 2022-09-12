number = int(input('Введите число для последовательности = '))
sum = 0
n = []
for i in range(number):
 x = round((1 + (1/(i+1)))**(i+1), 2)
 n.append(x)
 sum+=x    
print(n)
print(f'{sum}')