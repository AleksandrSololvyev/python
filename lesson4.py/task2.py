result = []
n = int(input("Введите число: "))
i = 2
old = n
while i <= n:
    if n % i == 0:
        result.append(i)
        n //= i
        i = 2
    else:
        i += 1
print(result)