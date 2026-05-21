fahrenheit = float(input("Введите градусы Фаренгейта: "))
celsius = (fahrenheit - 32) * 5 / 9
print("Цельсия:", celsius)
if celsius > 0:
    print("На улице тепло")
elif celsius < 0:
    print("На улице холодно")
elif celsius == 0:
    print("На улице ноль")
