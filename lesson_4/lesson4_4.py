# 4. Представлен список чисел. Определить элементы списка, не имеющие повторений.
# Сформировать итоговый массив чисел, соответствующих требованию.
# Элементы вывести в порядке их следования в исходном списке.
# Для выполнения задания обязательно использовать генератор списка.
# (Можно использовать list.count()).
# Пример исходного списка: [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11].
# Результат: [23, 1, 3, 10, 4, 11]

my_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]

new_list = []

# for element in my_list:
#     i = 0
#     for element_2 in my_list:
#         if element == element_2:
#             i += 1
#     if i == 1:
#         new_list.append(element)
#
# print(new_list)

for element in my_list:
    if my_list.count(element) == 1:
        new_list.append(element)

print(new_list)
