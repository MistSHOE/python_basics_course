# Home work 6
# Спортсмен занимается ежедневными пробежками.
# В первый день его результат составил a километров.
# Каждый день спортсмен увеличивал результат на 10 % относительно предыдущего.
# Требуется определить номер дня, на который результат спортсмена составит не менее b километров.
# Программа должна принимать значения параметров a и b и выводить одно натуральное число — номер дня.

b = 21
number_day = 1
a = 1.5

while number_day < b:
    percent = a / 100 * 10
    print(number_day, "День,", int(a), "км")
    number_day += 1
    a += percent

print("День:", number_day, "км:", int(a))