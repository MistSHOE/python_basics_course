# 7. Реализовать генератор с помощью функции с ключевым словом yield, создающим очередное значение.
# При вызове функции должен создаваться объект-генератор.
# Функция должна вызываться следующим образом: for el in fact(n).
# Функция отвечает за получение факториала числа, а в цикле необходимо выводить только первые n чисел, начиная с 1! и до n!.
# Подсказка: факториал числа n — произведение чисел от 1 до n.
# Например, факториал четырёх 4! = 1 * 2 * 3 * 4 = 24. На вебинаре реализовали похожий пример для чисел Фиббоначи.


def gen_fact(max_n):
    current_fact = 1
    current_n = 1
    while current_n <= max_n:
        current_fact *= current_n
        yield current_fact

        current_n += 1


my_list = gen_fact(10)
print(list(my_list))