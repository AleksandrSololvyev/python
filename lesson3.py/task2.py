list = [2, 3, 5, 6]
x = 0
y = 0
sum = 0
n = 0
result = []
for i in range(len(list)):
    if i < (len(list))/2:
        x = list[i]
        y = list[-i-1]
        sum = y * x
        result.append(sum)
print(f'{list} -> {result} ')