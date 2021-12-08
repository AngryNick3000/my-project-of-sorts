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
