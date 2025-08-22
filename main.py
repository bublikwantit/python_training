import time

# def average(*args):
#     return sum(args) / len(args)
# print(average(1,2,3,4,5,6,7))
#
# def dict(**kwargs):
#     for key, value in kwargs.items():
#         print(f"{key}: {value}", end='\n')
# dict(name="Mitya", age=34)
# dict(name="Mitya", age=34, city="SPB")

# def list_sum(*args):
#     if not args:
#         return 0
#     else:
#         return args[0] + list_sum(*args[1:])
# res = list_sum(1,2,3,4,5)
# print(res)

# def calculate_total(**kwargs):
#     '''Считаем суммму чека'''
#     total = 0
#     for item, price in kwargs.items():
#         total += price
#     return total

# order_total = calculate_total(apple=0.5, banana=1, adasd=5)
# print('Общая стоимость составляетЖ ', order_total)

# help(calculate_total())
# calculate_total.__doc__
# print(13 % -3*3-3**2)
# day = 14
# month = 10
# year = 2012

# print("%d.%02d.%d" % (day, month, year))
# # 14.02.2012
# print("%d-%02d-%d" % (year, month, day))
# # 2012-02-14
# print("%d/%d/%d" % (year, day, month))
# # 2012/14/2

# abit1 = {"ФИО": 'Фадеев О.Е.', "Количество баллов": 283, "Заявление": True}
# abit2 = {"ФИО": 'Дружинин И.Я.', "Количество баллов": 278, "Заявление": False}
# abit3 = {"ФИО": 'Афанасьев Д.Н.', "Количество баллов": 276, "Заявление": True}
# abit4 = {"ФИО": 'Афанасьев Д.Н.',
#          "Количество баллов": 4566, "Заявление": False}


# dict_list = [abit1, abit2, abit3]
# dict_list.append(abit4)

# print(dict_list)


# my_str = """      The Zen of PythonBeautiful is better than ugly.Explicit is better than implicit.Simple is better than complex.Complex is better than complicated.Flat is better than nested.Sparse is better than dense.Readability counts.Special cases aren't special enough to break the rules.Although practicality beats purity.Errors should never pass silently.Unless explicitly silenced.In the face of ambiguity, refuse the temptation to guess.There should be one-- and preferably only one --obvious way to do it.Although that way may not be obvious at first unless you're Dutch.Now is better than never.Although never is often better than *right* now.If the implementation is hard to explain, it's a bad idea.If the implementation is easy to explain, it may be a good idea.Namespaces are one honking great idea -- let's do more of those!"""
# res = len(list(set(my_str)))
# print(res)


# list_a = [1, 2, 3, 4, 5, 6, 7, 8]
# list_b = [2, 4, 6, 8, 10, 12]

# set_a, set_b = set(list_a), set(list_b)
# list_uniq = list(set_a.symmetric_difference(set_b))
# print(*list_uniq, sep=' ')
# L = ['a', 'b', 'c']
# print(id(L))

# L.append('d')
# print(id(L))

# a = 5
# b = 3+2
# print(id(a), id(b))
# c = id(a) - id(b)
# print(c)


# L = ['Hello', 'world']
# M = L

# print(M is L)
# M.append('!')

# print(L)


# M = L.copy()
# print(M is L)


# shopping_center = ("Галерея", "Санкт-Петербург",
#                    "Лиговский пр., 30", ["H&M", "Zara"])
# list_id_before = id(shopping_center[-1])

# shopping_center[-1].append("Uniqlo")
# list_id_after = id(shopping_center[-1])

# print(list_id_before == list_id_after)


# person_age = int(input())
# print(18 <= person_age <= 35)

# list_1 = [1, 2]

# list_2 = [1, 2, 3]
# val = list_2.pop()

# print(val)
# print(list_2)

# print(list_1 == list_2)
# print(list_1 is list_2)
# print(id(list_1) == id(list_2))


# sum = 0
# num = 1

# while sum < 500:
#     sum += 1
#     num += 1
#     print("Еще считаю")
# print(sum, 'ИГра закончена')


# count = 0
# n = 1  # 2^0
# while n <= 10000:
#     count += 1
#     n *= 2
#     print(n)

# print(count)

# money = 1000
# years = 0

# while money < 3000:
#     money *= 1.08
#     years += 1
# print(years)


# P = 1
# N = 5

# for item in range(1, N + 1):
#     P *= item
# print(P)

# N = int(input())
# for item in range(1, N + 1):
#     print('*' * item)


# matrix = [
#     [1, 2], [3, 4], [5, 6]
# ]

# for row in matrix:
#     for element in row:
#         print(element, end=" ")
#     print()


# max_num = 0
# test_matrix = [[1, 2, 3],
#                [7, -1, 2],
#                [123, 2, -1]]

# for row in test_matrix:
#     for j in range(len(row)):
#         if row[j] > max_num:
#             max_num = row[j]
# print(max_num)

# test_matrix = [[1, 2, 3, 3],
#                [7, -1, 2],
#                [123, 2, -1]]
# is_square = True
# rows_count = len(test_matrix)

# for row in test_matrix:
#     columns_count = 0
#     for row_index in range(len(row)):
#         columns_count += 1
#     if columns_count != rows_count:
#         is_square = False
#         break

# print(is_square)


text = """
У лукоморья дуб зелёный;
Златая цепь на дубе том:
И днём и ночью кот учёный
Всё ходит по цепи кругом;
Идёт направо -- песнь заводит,
Налево -- сказку говорит.
Там чудеса: там леший бродит,
Русалка на ветвях сидит;
Там на неведомых дорожках
Следы невиданных зверей;
Избушка там на курьих ножках
Стоит без окон, без дверей;
Там лес и дол видений полны;
Там о заре прихлынут волны
На брег песчаный и пустой,
И тридцать витязей прекрасных
Чредой из вод выходят ясных,
И с ними дядька их морской;
Там королевич мимоходом
Пленяет грозного царя;
Там в облаках перед народом
Через леса, через моря
Колдун несёт богатыря;
В темнице там царевна тужит,
А бурый волк ей верно служит;
Там ступа с Бабою Ягой
Идёт, бредёт сама собой,
Там царь Кащей над златом чахнет;
Там русский дух... там Русью пахнет!
И там я был, и мёд я пил;
У моря видел дуб зелёный;
Под ним сидел, и кот учёный
Свои мне сказки говорил.
"""

# text = text.lower()
# text_char = [',', '.', '-', '!', ':', ';']
# for char in text:
#     if char in text_char:
#         text = text.replace(char, "")

# text_words = text.split()
# print(len(text_words))


# print(7 // 3)
# print(7 % 3)

# def print_2_add_2():
#     print(2 + 2)


# print_2_add_2()


# def delitel(a):
#     count = 0
#     for i in range(1, a + 1):
#         if a % i == 0:
#             count += 1
#     return count


# print(delitel(5))


# def check_palindrome(input_str):
#     input_str = input_str.lower()
#     input_str = input_str.replace(' ', '')
#     if input_str == input_str[::-1]:
#         return True
#     else:
#         return False


# print(check_palindrome("Кит на море не романтик"))  # False


# def get_mul_func(m):
#     nonlocal_m = m

#     def local_mul(n):
#         return n * nonlocal_m

#     return local_mul


# # возвращаем функцию, которая будет умножать числа на 2
# two_mul = get_mul_func(2)
# print(two_mul(5))


# def muliply(*args):
#     mult = 1
#     for i in args:
#         mult *= i
#     return mult


# print(muliply(5, 10, 9))


# def incorrect_func(name_arg=[]):
#     # name_arg является локальной переменной
#     print("Аргумент до изменения", name_arg)
#     name_arg.append(1)
#     print("Аргумент после изменения", name_arg)


# # вызовем два раза одну и ту же функцию
# incorrect_func()
# print('-----')
# incorrect_func()

# def natural_numbers(start=1, step=1):
#     num = start
#     while True:
#         yield num
#         num += step


# for n in natural_numbers():  # начнёт с 1, шаг 1
#     print(n)
#     if n >= 10:
#         break

# print("---")


# def func(list):
#     list_values = list.copy()
#     while True:
#         value = list_values.pop(0)
#         result = list_values.append(value)
#         yield value

# def twice_func(inside_func):
#     """Функция, выполняющая дважды функцию принятую в качестве аргумента"""
#     inside_func()
#     inside_func()

# def hello():
#     print("Hello")
# test = twice_func(hello)


# def make_adder(x):
#     def adder(n):
#         return x + n  # захват переменной "x" из nonlocal области
#     return adder  # возвращение функции в качестве результата


# add_5 = make_adder(5)
# print(add_5(10))  # 15
# print(add_5(100))  # 105

# ДЕКОРАТОРЫ
# def twice_func(inside_func):
#     """Функция, выполняющая дважды функцию принятую в качестве аргумента"""
#     inside_func()
#     inside_func()


# def hello():
#     print("Hello")


# test = twice_func(hello)
# print(test)


# def my_decorator(a_function_to_decorate):
#     # Здесь мы определяем новую функцию - «обёртку». Она нам нужна, чтобы выполнять
#     # каждый раз при вызове оригинальной функции, а не только один раз
#     def wrapper():
#         # здесь поместим код, который будет выполняться до вызова, потом вызов
#         # оригинальной функции, потом код после вызова
#         print("Я буду выполнен до основного вызова!")

#         result = a_function_to_decorate()  # не забываем вернуть значение исходной функции

#         print("Я буду выполнен после основного вызова!")
#         return result
#     return wrapper


# def my_function():
#     print("Я - оборачиваемая функция!")
#     return 0


# print(my_function())
# decorated_function = my_decorator(my_function)  # декорирование функции
# print(decorated_function())


# def decorator_time(fn):
#     def wrapper():
#         print(f"Запустилась функция {fn}")
#         t0 = time.time()
#         result = fn()
#         dt = time.time() - t0
#         print(f"Функция выполнилась. Время: {dt:.10f}")
#         return dt  # задекорированная функция будет возвращать время работы
#     return wrapper


# def pow_2():
#     return 10000000 ** 2


# def in_build_pow():
#     return pow(10000000, 2)


# pow_2 = decorator_time(pow_2)
# in_build_pow = decorator_time(in_build_pow)

# pow_2()
# # Запустилась функция <function pow_2 at 0x7f938401b158>
# # Функция выполнилась. Время: 0.0000011921

# in_build_pow()


# def time_count(my_func):
#     def wrapper():
#         print(f"Запускаем функцию {my_func}")
#         t0 = time.perf_counter()
#         for _ in range(100):
#             res = my_func()
#         t2 = time.perf_counter() - t0
#         print(f"Программа выполнилась за время {t2:.10f}")
#         return t2
#     return wrapper


# def pow_2():
#     return 10000000 ** 2


# pow_2 = time_count(pow_2)
# pow_2()

# L = ['a', 'b', 'c']
# print(id(L))

# L.append('d')
# print(id(L))

# print(L)

# a = 5
# b = 3+2
# print(id(a))
# print(id(b))


# a = 0
# b = 0

# while id(a) == id(b):
#     a -= 1
#     b -= 1

# print(a)


# shopping_center = ("Галерея", "Санкт-Петербург",
#                    "Лиговский пр., 30", ["H&M", "Zara"])
# list_id_before = id(shopping_center[-1])
# print(shopping_center[-1])

# shopping_center[-1].append("Uniqlo")
# list_id_after = id(shopping_center[-1])
# print(shopping_center[-1])

# print(list_id_before)
# print(list_id_after)

# print(list_id_before == list_id_after)


# L = [1, 1, 2, 3, 2]

# b = set(L)

# print(b)
# print(b)
# print(b)
# # {1,2,3}


# text = "        The Zen of Python"

# unique = set(text)

# print("Количество уникальных символов: ", len(unique))


# L = [_ for _ in range(1, 11)]
# M = [_ for _ in range(10, 0, -1)]

# for a, b in zip(L, M):
#     print(a, b)

# N = []

# for i in range(10):
#     N.append(L[i] * M[i])
# print(N)


# for a in zip(L, M):
#     print(a)

# for a, b in zip(L, M):
# print(f"a= {a} b={b}")

# a3b2c4d1a2
# my_str = 'aaabbccccdaa'

# first_char = my_str[0]
# count = 0
# res_str = ''

# for i in my_str:
#     if i == first_char:
#         count += 1
#     else:
#         res_str += (first_char + str(count))
#         count = 1
#         first_char = i
# res_str += first_char + str(count)
# print(res_str)


# numbers = [1, 2, 3, 4, 5]
# more_numbers = [*numbers, 6, 7]
# print(more_numbers)


# def my_foo(*args):
#     res = " ".join(str(i) for i in args)
#     print(res)


# my_foo(5, 6, 7, 8, 9)
# print(*numbers)

# Числа Фибоначи
# def fib():
#     a, b = 0, 1
#     yield a
#     yield b

#     while True:
#         a, b = b, a + b
#         yield b

# итераторы
# for num in fib():
#     print(num)

# def repeat_list(list_):
#     list_values = list_.copy()
#     while True:
#         value = list_values.pop(0)
#         list_values.append(value)
#         yield value


# for i in repeat_list([1, 2, 3]):
#     print(i)

# iter_obj = iter("Hello!")
# print(next(iter_obj))
# print(next(iter_obj))
# print(next(iter_obj))
# print(next(iter_obj))
# print(next(iter_obj))
# print(next(iter_obj))
# print(next(iter_obj))

#  =======================================================================================

# декоратор
# USERS = ['admin', 'guest', 'director', 'root', 'superstar']

# yesno = input("""Введите Y, если хотите авторизоваться, или N,
#              если хотите продолжить работу как анонимный пользователь: """)

# auth = yesno == "Y"

# if auth:
#     username = input("Введите ваш username:")


# def is_auth(func):
#     def wrapper():
#         if auth:
#             print("Пользователь авторизован")
#             func()
#         else:
#             print("Пользователь не авторизован. Функция выполнена не будет")
#     return wrapper


# def has_access(func):
#     def wrapper():
#         if username in USERS:
#             print("Авторизован как", username)
#             func()
#         else:
#             print("Доступ пользователю", username, "запрещён")
#     return wrapper


# @is_auth
# @has_access
# def from_db():
#     print("some data from database")


# from_db()
#  =======================================================================================
