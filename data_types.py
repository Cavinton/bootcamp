
'========перемнные====='
# переменные это ссылки на ячейку памяти, где хранятся какие-то данные, для дальнейшего использвания.
# num1 = 10
# num2 = 55
# num3 = 10
# print(num1 + num2 - num3)

'-------правила наименования переменных----'
#a = 5 #так можно называть переменые, но назначение непонятное
# 1num = 10 # переменные нельзя называть числами
#my name = 'Makers'# нельзя использовать пробел, символы . только _ в перменных
# print = 25
#ers' # нельзя писать название на кириллице

# Sneake case - пайтон стиль наименования переменных 
#my_name = 'makers'
# camel case - стиль остальных языков прогрмаирования 
#myName = 'makers'

'====ввод и вывод данных из терминала====='
# print - функция вывода данных в терминал
# input - функция ввода данных с терминала

# number = input('введите число: ') 
# print(number)

'===типы данных ======'
# типы данных в пайтое делятся на два: изменяемые, неизменяемые
'Изменяемые'
# list
# set
# dict

'Неизменяемые'
# int. float, decimal, complex
# str # это строка, текст
# tuple
# bool
# none
# frozenset




# n = 2
# print(id(n))


'======неизменяемые===='
# int - целые числа
# float - числа с плавающей точкой (15.9)
# decimal - числа с плавающей точкой , но с большим диапозоном чисел после запятой (15.92-130128401824081204801284018240810480128401820481024)
# complex - числа из высшей математики (5j)

# from decimal import Decimal

# num_1 = 10
# num_2 = Decimal(0.54365456412)
# print(num_1 + num_2)

# num_1 = '225' # '225' -> 225
# num_2 = 5
# print(int(num_1)%5)

# int() - функция инт переводит текст с числом в тип данных число

'=====операции над числами====='
# +
# -
# *
# / деление с запятой  
# //  деление целочисленное 
# % остаток от деления : 10%3=1, 3*3, 10-9
# **  возведение в степень
#  -x - Смена знака числа
# abs(x) - Модуль числа
# divmod(x, y) - Пара (x // y, x % y)
# x ** y - Возведение в степень
# pow(x, y[, z]) - xy по модулю (если модуль задан)


# bin() - двоичная система исчисления
# hex() - шеснадцатьтеричная сист исчис
# oct() - восьмиричная строка

# теорима Пифагора :

import math
dir(math)

leg_a = 2
leg_b = 3

hypotenuse = (pow(leg_a,2) + pow(leg_b, 2))
print(math.sqrt(hypotenuse))



# sec_in_min = 60
# min_in_hrs = 60
# sec_in_hrs = sec_in_min * min_in_hrs

# hrs_in_day = 24
# sec_in_day= hrs_in_day * sec_in_hrs

# days_in_year = 365
# sec_in_year = sec_in_day * days_in_year
# print(sec_in_year)

# months_in_year = 12
# sec_in_months = sec_in_year / months_in_year 
# print(sec_in_months)


# a = 123
# id(a) 
# b = 123
# id(b) 
# bool(a is b)

# my_list = [1, 2, 3, 4]
# my_list.append(7)
# print(my_list)
# append - добавление цифр в изменямые типы данных

n = 11
m = 3
print(round(n / m, 3 ))
# round(n/m, цифры(после запятой)) - округление

# PEP8 регламент написания кода в пайтоне, прочитать раздел как правильно писать переменные

# с минуса делает плюс:
# num = -1
# print(abs(num))

string = '             Как прекрасен этот мир          '
str = string.strip(' ')
len = len(str) 
print(str, len)


x = int(input())
y = int(input())
if x // y  :
    print('Частное')
elif x % y :
    print('Остаток')