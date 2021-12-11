# Home work 3
# Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.
# Например, пользователь ввёл число 2. Считаем 2 + 22 + 222 = 246.

n = input("Введите число: ")
# Конкотенация str n + n
nn = (str(n + n))
nnn = (str(n + n + n))
result = int(n) + int(nn) + int(nnn)

print(result)
print(type(result))

