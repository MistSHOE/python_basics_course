# 3. Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.

month = int(input("Введите месяц от 1 до 12: "))
winter = [12, 1, 2]
spring = [3, 4, 5]
summer = [6, 7, 8]
autumn = [9, 10, 11]

if month in winter:
    print("это зима")
elif month in spring:
    print("это весна")
elif month in summer:
    print("это лето")
elif month in autumn:
    print("это осень")
else:
    print("Пусто")

month = int(input("Введите месяц от 1 до 12: "))

my_dict = {"winter": [12, 1, 2],
           "spring": [3, 4, 5],
           "summer": [6, 7, 8],
           "autumn": [9, 10, 11]
           }

print(my_dict)
print(my_dict["winter"])

if month in my_dict.setdefault("winter"):
    print("это зима")
elif month in my_dict.setdefault("spring"):
    print("это весна")
elif month in my_dict.setdefault("summer"):
    print("это лето")
elif month in my_dict.setdefault("autumn"):
    print("это осень")
else:
    print("Пусто")
