txt = open(r'numbers.txt', 'r')
act = None
import copy

def bubble_sort(num):
    for i in range(len(num) - 1):
        for j in range(len(num) - i - 1):
            if num[j] > num[j + 1]:
                num[j], num[j + 1] = num[j + 1], num[j]          
def select_sort(num):
    for i in range(len(num) - 1):
        lower = i
        for j in range(i + 1, len(num)):
            if num[j] < num[lower]:
                lower = j
        num[i], num[lower] = num[lower], num[i]
def insert_sort(num):
    for i in range(1, len(num)):
        temp = num[i]
        j = i - 1
        while j >= 0 and temp < num[j]:
            num[j + 1] = num[j]
            j -= 1
        num[j + 1] = temp

while act != 0:
    print("\nMENU")
    print("1. Загрузить числа")
    print("0. Закрыть программу")
    act = int(input("\nВыберите действие: "))
    if act == 1:
        num = list(map(int, txt.read().split(',')))
        num1 = copy.copy(num)
        print('Числа загружены')
    while act != 0:
        print("\nMENU")
        print("1. Обновить числа")
        print("2. Сортировка пузырьком")
        print("3. Сортировка выбором")
        print("4. Сортировка вставками")
        print("5. Вывод чисел")
        print("0. Закрыть программу")
        act = int(input("\nВыберите действие: "))
        if act == 1:
            num = copy.copy(num1)
            print('Числа обновлены')
        if act == 2:
            bubble_sort(num)
            print("Числа отсортированы")
        if act == 3:
            select_sort(num)
            print("Числа отсортированы")
        if act == 4:
            insert_sort(num)
            print("Числа отсортированы")
        if act == 5:
            print(str(num).strip('[]') + '.')
