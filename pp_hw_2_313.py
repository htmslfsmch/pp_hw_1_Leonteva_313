counter = int(input("Количество чисел:"))
y = 0
for i in range(counter):
    x = float(input("{} Число: ".format(i + 1)))
    y += x
y = y / counter
