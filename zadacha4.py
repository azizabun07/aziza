fruits = ["apple", "banana", "orange"]

try:
    i = int(input())
    print(fruits[i])
except IndexError:
    print('такого индекса в списке нет')
except ValueError:
    print('только число')