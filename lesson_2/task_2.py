# 2. Для списка реализовать c, т.е.
# Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
# При нечетном количестве элементов последний сохранить на своем месте.
# Исходные списки можете инициализировать прямо в коде,
# но обязательно проверьте работоспособность, для пустого списка, списка из 1 элемента,
# списка с четным количеством элементов и с нечетным.
# (Опционально) Если получится, реализуйте обмен, как функцию.

a = 100
b = 200
c = 300
x = 0
my_list = [a, b, c, 500, 1000, 2000, "End"]

for i in range(int(len(my_list) / 2)):
    my_list[x], my_list[x + 1] = my_list[x + 1], my_list[x]
    x += 2

print(my_list)

