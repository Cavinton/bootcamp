'==========strings========='
# строки это неизменяемый тип данных который предназначен для хранения текста заключенного в одинарные либо двойные ковычки

# string1 =  'строка с одинарными ковычками' 
# # string2 = "строка с двойными ковычками "
# string3 =  "don't "
# string4 = 'название магазина "азбука"'
# string5 = ''' 
# многострочный текст
#  одинарных ковычках 
# тут можно и одинарные и двойные ковычки'''
# string6 = """

# многострочный текст в двойных ковычках
# тут можно и одинарные и двонйные ковычки

# """

# string7 = 'hello'+'world'
# print(string7)
# str8 = 'A' * 20
# print(str8)

'=====экранизация строк====='
# '\n' -  перенос на новую строку

# print('hello\nworld') 

# # '\t' - это табуляция несколько пробелов 
# print('hello\tworld')

# print('he\tllo world')

# # '\v' - перенос на новую строку со смещением вправо на длину предыдущей строки

# print('hello\vworld\vmakers') # hello
#                                          #    world
#                                                  #       makers


# # '\r' - перенос каретки в самое начало строки 

# print('hello\rworldHi') # worldHi


# # '\'' - отображение '
# # "\"" - оторбажение двойных ковычек

# print('Don\'t') # Don't
# print("home\\'makers") #home\'makers


# # '\\' - отображение \
# print('команда \\n переносит строку')


'=======форматирование строк====='
# title = 'iphone 15'
# price = 1000
# shop = 'makrs'
# # print('я купил title за price')

# '1. f-строка '
# print(f'я купил {title } за {price} в магазине {shop} ') # я купил iphone 15 за 1000 в магазине makrs 

# '2. %s'
# print('я купил %s за %s в магазине %s' % (title, price,shop ))

# '3. str.format'
# print( ' я купил {} за {} в магазине {}'.format(title, price,shop)) 

'========(str) методы строк'
# методы это функции. которые относятся к определенному типу данных(классу). к ним мы обращаемся через точку 


#    print(dir(str))

# string = 'HELLO world'
# print(string.upper()) # HELLO WORLD
# print(string.lower()) # hello world
# print(string.swapcase()) # hello WORLD

# print(string.title()) #Hello World
# print(string.capitalize()) #Hello world
'--------------------------------------'
# string = 'hi'
# print(string.islower()) # true
# print(string.isupper()) # falce

# print(string.center(12, '*')) # '*****hi*****'

# print(string.count('l')) # 0 (показывает кол во введеной буквы)
# print(string.count('hi')) # 2

# print(string. ) #true 
# print(string.endswith('i')) # true
# print(string.endswith('o')) # falce
 #'--------------------------------------------------'
# string = 'makers'
# print(string.isalpha()) # true, проверяет на буквы

# print(string.isdigit()) # falce, проверяет все ли является цифрами

# print(string.isalnum()) #true, проверяет содержатся ли все буквы или только цифры
#'------------------------------------------------------'
# string = 'hello world makers bootcamp'
# print(string.split('o')) # ['hell', ' w', 'rld makers b', '', 'tcamp']

# string = 'hello'
# #print(string.replace('h', 'm')) #mello
# print(string.replace('', '$')) #$h$e$l$l$o$


#string = '##############hhello##############'
# print(string.strip('#')) #hhello, убирает сначала и с конца 

# # "".join(list)  - это переменная которая хранит тип данных list


# '=========индексы========='
# # индекс - это порядковый номер элемента последовательности (индекс начинается с нуля)
# #-11-10-9-8-7-6-5-4-3-2-1 сзади счет
# #   'h e l l o  w o r l d'
# #0 1 2 3 4 5 6 7 8 9 1 0 cспереди счет

# string = 'hello world'
# # print(string[-5]) #'w'
# # print(string[-1]) #'d'

# # срез [start:end(не включительно):step]
# # string[6:10] worl
# # string[1:5] ello
# # string[:] hello world
# print(string[::2]) #hlowrd, перепрыгивает чз два
# print(string[::-1]) # dlrow olleh, отзеркалиевает
# print(string[::-2]) #drwolh 

# string1 = 'nitro'
# string2 = 'emes'
# print(f {string1} {string2})


# string = 'nitro'
# print(string.isalpha(Python))
# string ='hello world'
# print(string.split(' '))


# string = '           nnnnn            '
# print(string.strip(), string.())


# №2
string = str(input())
m = 'True' if len(string) > 5 else 'False'
print(m)

# №3
mark = int(input())
if mark >= 90 :
    print('Отлично, Ваша оценка 5!')
elif mark >= 80 :
    print('Здорово, Ваша оценка 4!')
elif mark >= 70 :
    print('Хорошо, Ваша оценка 3!')
elif mark >= 60 :
    print('Вам стоит подучить материал')
else :
    print('Вы не сдали экзамен')

# №3
number = int(input())
if number < 0 :
    print('negative')
elif number > 0 :
    print('positive')
elif number == 0 :
    print('zero')
else :
    print('dolboeb')


# №4
x = 5
y = -3
if x > y :
    print(y)
else :
    print(x)


