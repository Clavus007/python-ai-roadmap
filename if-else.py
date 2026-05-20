# a, b, c = int(input()), int(input()), int(input())
# if a == b == c:
#     print("Числа равны")
# else:
#    print("Числа неравны")

# Напишите программу, которая считывает одну строку. Если это строка «Python», программа выводит «ДА», в противном случае программа выводит «НЕТ».

# a = str(input())
# if a == "Python":
#    print("ДА")
# else:
#     print("НЕТ")

# Напишите программу, которая определяет, состоит ли двузначное число, введенное с клавиатуры, из одинаковых цифр. Если состоит, то программа выводит «ДА»,
# в противном случае программа выводит «НЕТ».

# a = int(input())
# last_a = a % 10
# first_a = a // 10
# if last_a == first_a:
#    print("YES!")
# else:
#    print("NO!")

# a, b, c = int(input()), int(input()), int(input())
# counter = 0

# if a % 2 == 0:
#    counter = counter + 1
# if b % 2 == 0:
#    counter = counter + 1
# if c % 2 == 0:
#    counter = counter + 1

# print(counter)

# n = int(input())
# a = (n // 10 ** (4 - 1)) % 10
# b = (n // 10 ** (4 - 2)) % 10
# c = (n // 10 ** (4 - 3)) % 10
# d = (n // 10 ** (4 - 4)) % 10
# print("ДА" if a + d == b - c else "НЕТ")

# a,b,c=(int(input()) for _ in range(3))


# age = int(input())
# print(
#    "детство"
#    if age < 14
#    else "молодость" if age < 25 else "зрелость" if age <= 59 else "старость"
# )

# age = int(input())
# print(
#    "детство"
#    if age < 14
#    else (
#        "молодость"
#        if age < 25
#        else "зрелость" if age < 60 else "старость" if age <= 200 else "DEAD"
#    )
# )

secret = 7
n = int(input("Какое число я загадал? "))
if n == secret:
    print("Поздравляю! Ты угадал!")
else:
    print("Не угадал, я загадал число", secret)

secret = 7  # Загаданное число — поменяй, если хочешь
n = int(input("Какое число я загадал? "))

if n == secret:
    print("Поздравляю! Ты угадал!")
else:
    print("Не угадал, я загадал число", secret)

secret = 7  # Загаданное число — поменяй, если хочешь
n = int(input("Какое число я загадал? "))
if n == secret:
    print("Поздравляю! Ты угадал!")
else:
    print("Не угадал, я загадал число", secret)


# a = int(input())
# if a < 14:
#    print("детство")
# elif a < 25:
#    print("молодость")
# elif a < 60:
#    print("зрелость")
# else:
#    print("старость")

# print("детство" if n <= 13 else "молодость" if n <= 24 else "зрелость" if n <= 59 else "старость")
