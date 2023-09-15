x = int(input("Введите число: "))
count = 0
while x > 0:
    count = count + 1
    x = x // 10
print("Количество цифр равно:", count)
