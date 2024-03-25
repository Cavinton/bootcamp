'=======Exceptions====='
'Исключения - это обьекты которые прерывают работу кода если не были обработаны '

#SyntaxError
'исключение, которое выходит,когда в коде допущена синтаксическая ошибка'

'''
a = 
SynaxError
'''

NameError
# выходит когда обращаешься к несуществующей переменной

'''
num1 = 15
print(num5)
NameError
'''

IndexError
# выходит когда обращаешься к несуществующему индексу

'''
list1 = [1,2,3,4]
print(list1[7])
IndexError
'''
KeyError
# выходит когда обращаешься по несуществующему ключу

'''
dict1 = {'a':1}
dict1['c']
KeyError
'''

'''
dict1 = {'a':1}
dict1.get('c') 
None
ошибки не будет! гет не вызывает ошибку, возвращает None
'''

ValueError
# когда передаем в функцию некорректный для нее тип данных
# когда распаковываем итерируемый обьект на несколько переменных и кол-во переменных не совпадает с кол-во элементов

'''
int('10fdjj)
ValueError
'''

'''
a,b,c = 1,2
ValueError
'''

TypeError
# исключение выходит, когда мы пытаемся использовать методы, не свойственные какому-то типу данных
# когда пытаемся передать функции больше или меньше аргументов чем принимает

'''
for i in 1234:
    ...
    TypeError
'''


'''
"5" + 5
TypeError
'''

'''
{[1,2,3]:'hi'}
TypeError
'''

'''
input('dkfjgkj', 123)
TypeError 
'''

ZeroDivisionError
'''
45//0
ZeroDivisionError
'''

'''
45 % 0
ZeroDivisionError
'''

AttributeError
# выходит когда обращаемся к несущ аттрибуту или методу обьекта(типу данных)
'''
[1,12,34].replace('a', '')
AttributeError
'''

'''
'makers'.pop(0)
AttributeError
'''

IndentationError
# выходит когда неправильно используем отступы

'''
   a = 5
IndentationError
'''

'''
for i in range():
print(i)
IndentationError
'''

Exception
# исключение, которое создали, чтобы его вызывать

'====Вызов исключений===='
# raise NameError('просто вызываю NameError')
# raise IndentationError
# raise KeyError

'=====обработка исключений====='
# нужна чтобы код не прекращал работу мы можем использовать конструкцию try-except, и обрабатывать вызванное исключение

# try: # код который может вызвать ошибку, исключение
#     num = int(input('Введите число'))
# except ValueError: # ожидаемую ошибку,исключение
#     # обработку на исключение которое поймали
#     print('Вы ввели не число')
# else: # отработает если исключение не вышло
#     print(f'Вы ввели число {num}')
# finally: #работает всегда
#     print('Dos-Vi-Dos')

# try:
#     num = int(input('введите число'))
#     res = 10 / num
# except ValueError:
#     print('что-то пошло не так')
# except ZeroDivisionError:
#     print('вы ввели 0')

try:
    string = 'hello'
    num = 5
    r = string + num
    print(r)
except Exception:
        print('Unsupported option')

# except Exception - обрабатывает все исключения которые могут выйти

# try:
#     num = int(input('введите число'))
#     res = 10 / num
# except ValueError as e:
#     print('что-то пошло не так')


# можем указать в ексепт несколько исключений при помщи скобок и запятой except(ValueError, TypeError,ZeroDivisionError)


# try:
#     raise NameError
# except NameError:
#     print(1)


# try:
#     num = int(input('введите число'))
#     if num > 1:
#         raise ValueError
#     elif num < 1:
#         raise TypeError
#     elif num == 0:
#         raise ZeroDivisionError
# except ValueError:
#     print('+')
# except TypeError:
#     print('-')
# except ZeroDivisionError:
#     print('no')


# try:
#     age = int(input())
#     if age < 18:
#         raise ValueError('Доступ запрещён')
# except Exception:
#     print('Введён некорректный возраст')
# else:
#     print('Спасибо')
# finally:
#     print('До свидания!')

# try:
#     cash = int(input())
#     if cash < 0:
#         raise ValueError('Сумма не может быть отрицательной! ')
# finally:
#     print(cash)

list_ = [1, 2, 3, 4]
for i in range(0, len(list_) + 1):
     print(list_[i])