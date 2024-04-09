# Написать функцию, которая принимает на вход список целых чисел и
# возвращает новый список, содержащий только уникальные элементы из исходного списка.

spicok = [1, 2, 3, 3, 4, 1, 5, 5, 6]


def unique(spicok):
    unique_spisok = list(set(spicok))
    print(unique_spisok)


unique(spicok)

# или если рассмотреть вариант, что пользователь вводит значения через input

stroka_dla_spicok2 = input("Введите целые числа через пробел: ")
spicok2 = stroka_dla_spicok2.split(" ")


def unique2(spicok2):
    for a in spicok2:
        if a.isdigit() == False:
            return print("Вы не соблюли рекомендации по вводу чисел!")
    unique_spicok = list(set(spicok2))
    print(unique_spicok)


unique2(spicok2)
