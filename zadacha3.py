#рекурсия функция сама себя вызыва
try:
    a = int(input('Введите первое число:'))
    b = int(input('Введите второе число:'))
    i = a / b
except Exception:
    print('Нельзя делить на ноль')
else:
    print(i)


