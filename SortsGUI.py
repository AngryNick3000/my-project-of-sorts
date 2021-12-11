from tkinter import messagebox
from tkinter import *
import copy
from sorted import *
from tkinter.filedialog import askopenfilename

num = None
copy_num = None


def load():
    global num
    global copy_num
    messagebox.showinfo("Вставка файла", "Выберите текстовый документ с числами через запятую и с пробелом!")
    try:
        txt = open(askopenfilename())
        num = list(map(int, txt.read().split(',')))
        copy_num = copy.copy(num)
        messagebox.showinfo("Вставка файла", "Числа загружены")
    except ValueError and FileNotFoundError:
        messagebox.showinfo("Вставка файла", "Неправильный файл")


def renew():
    global num
    num = copy.copy(copy_num)
    messagebox.showinfo("Сортировка", "Числа сброшены")


def output():
    messagebox.showinfo("Сортировка", f"Числа: {str(num).strip('[]')}.")


def stop():
    root.destroy()


def mysort(choice):
    if num is not None:
        if choice == 'bubble':
            bubble_sort(num)
        elif choice == 'select':
            select_sort(num)
        elif choice == 'insert':
            insert_sort(num)
        messagebox.showinfo("Сортировка", "Числа отсортированы")
    else:
        messagebox.showinfo("Сортировка", "Числа не были загружены!")


root = Tk()
root.title("Сортировка различными методами by Nick3000")
root.geometry("450x50")
main_menu = Menu()
sort_menu = Menu()

main_menu.add_cascade(label="Загрузить числа", command=load)

main_menu.add_cascade(label="Сбросить числа", command=renew)

main_menu.add_cascade(label="Сортировка", menu=sort_menu)

sort_menu.add_command(label="Сортировка пузырьком", command=lambda: mysort('bubble'))

sort_menu.add_command(label="Сортировка выбором", command=lambda: mysort('select'))

sort_menu.add_command(label="Сортировка вставками", command=lambda: mysort('insert'))

main_menu.add_cascade(label="Вывести числа", command=output)

main_menu.add_cascade(label="Выход", command=stop)

root.config(menu=main_menu)
root.mainloop()
