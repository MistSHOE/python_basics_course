# Home work 2
# Пользователь вводит время в секундах. Переведите время в часы,
# минуты и секунды и выведите в формате чч:мм:сс. Используйте форматирование строк.

clocks = input("Введите время в секундах: ")
seconds = int(clocks)
minutes = seconds / 60
hours = minutes / 60

print(f'{int(hours)}, {int(minutes)}, {int(seconds, 1)}')
print(int(hours), int(minutes), int(seconds), sep=" : ")
