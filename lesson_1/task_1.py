# Home work 1
# Поработайте с переменными, создайте несколько, выведите на экран,
# запросите у пользователя несколько чисел и строк и сохраните в переменные, выведите на экран.


name = "Tao"
number = 25
print(name, str(number), sep=",")

i = 0
x = []
while i < 3:
    agent_1 = [input("Введите число: ")]
    agent_2 = [input("Предумайте имя: ")]
    i += 1
    x.append(agent_1)
    x.append(agent_2)

print(agent_1, agent_2)
print(x)

