#    1. Создать список и заполнить его элементами различных типов данных. Реализовать скрипт проверки типа данных каждо-
#    го элемента. Использовать функцию type() для проверки типа. Элементы списка можно не запрашивать у пользователя, а
#    указать явно, в программе.

list = [222, 22.2,'Hello World', None,  True, False]
def type_1(a):
    for a in range(len(list)):
        print(type(list[a]))
    return
type_1(list)

#    2. Для списка реализовать обмен значений соседних элементов, т.е. Значениями обмениваются элементы с индексами 0 и
#    1, 2 и 3 и т.д. При нечетном количестве элементов последний сохранить на своем месте. Для заполнения списка элемен-
#    тов необходимо использовать функцию input().

elements_count = int(input('Введите количество элементов списка '))
list = []
a = 0
while i < elements_count:
    list.append(input('Введите следующее значение списка '))
    i += 1
for elements in range(int(len(list)/2)):
        list[a], list[a + 1] = list [a + 1], list[a]
        a += 2
print(list)

#    3. Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить к какому времени года относится месяц (зима,
#    весна, лето, осень). Напишите решения через list и через dict.

seasons_list = ['Зима!', 'Весна!', 'Лето!', 'Осень!']
seasons_dict = {1 : 'Зима', 2 : 'Весна', 3 : 'Лето', 4 : 'Осень'}
month = int(input('Введите номер месяца:'))
if month ==1 or month == 12 or month == 2:
        print(seasons_dict.get(1))
        print(seasons_list[0])
elif month == 3 or month == 4 or month ==5:
    print(seasons_dict.get(2))
    print(seasons_list[1])
elif month == 6 or month == 7 or month == 8:
    print(seasons_dict.get(3))
    print(seasons_list[2])
elif month == 9 or month == 10 or month == 11:
    print(seasons_dict.get(4))
    print(seasons_list[3])
else:
        print('Такого месяца нет')

#   4. Пользователь вводит строку из нескольких слов, разделённых пробелами. Вывести каждое слово с новой строки. Строки
#   необходимо пронумеровать. Если в слово длинное, выводить только первые 10 букв в слове.

my_string = input('Введите 2 слова через пробел: ')
my_word = []
number = 1
for a in range(my_string.count(' ') + 1):
    my_word = my_string.split()
    if len(str(my_word)) <= 10:
        print(f' {number} {my_word [a]}')
        number += 1
    else:
        print(f' {number} {my_word [a] [0:10]}')
        number += 1

#   5. Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел. У пользователя
#   необходимо запрашивать новый элемент рейтинга. Если в рейтинге существуют элементы с одинаковыми значениями, то
#   новый элемент с тем же значением должен разместиться после них.

list = [7, 5, 9, 3, 2]
print(f'Рейтинг - {list}')
digit = int(input('Введите число (111 - выход) '))
while digit != 111:
    for а in range(len(list)):
        if list[а] == digit:
            list.insert(а + 1, digit)
            break
        elif list[0] < digit:
            list.insert(0, digit)
        elif list[-1] > digit:
            list.append(digit)
        elif list[а] > digit and list[а + 1] < digit:
            list.insert(а + 1, digit)
    print(f'Текущий список - {list}')
    digit = int(input('Введите число '))

#    6. *Реализовать структуру данных «Товары». Она должна представлять собой список кортежей. Каждый кортеж хранит
#    информацию об отдельном товаре. В кортеже должно быть два элемента — номер товара и словарь с параметрами
#    (характеристиками товара: название, цена, количество, единица измерения). Структуру нужно сформировать программно,
#    т.е. запрашивать все данные у пользователя.

goods = []
features = {'Название': '', 'Цена': '', 'Кол-во': '', 'еденица': ''}
analytics = {'Название': [], 'Цена': [], 'Кол-во': [], 'еденица': []}
number = 0
feature_ = None
control = None
while True:
    control = input("Для выхода нажмите 'Q', для продолжения 'Enter', для аналитики 'A'").upper()
    if control == 'Q':
        break
    number += 1
    if control == 'A':
        print(f'\n Текущая аналитика \n {"-" * 30}')
        for key, value in analytics.items():
            print(f'{key[:25]:>30}: {value}')
            print("-" * 30)
    for f in features.keys():
        feature_ = input(f'Функция ввода {f}')
        features[f] = int(feature_) if (f == 'Цена' or f == 'Кол-во') else feature_
        analytics[f].append(features[f])
    goods.append((number, features))

#   Необходимо собрать аналитику о товарах. Реализовать словарь, в котором каждый ключ — характеристика товара, например
#   название, а значение — список значений-характеристик, например список названий товаров.

goods = int(input('Введите количество товара '))
n = 1
my_dict = []
list = []
my_analys = {}
while n <= goods:
    my_dict = dict({'название': input('введите название '), 'цена': input('Введите цену '),
                    'количество': input('Введите количество '), 'eд': input('Введите единицу измерения ')})
    list.append((n, my_dict))
    n += 1
    my_analys = dict(
        {'название': my_dict.get('название'), 'цена': my_dict.get('цена'), 'количество': my_dict.get('количество'),
         'ед': my_dict.get('ед')})
print(list)
print(my_analys)