
 

 # логистические операторы - выра=жения, которые возвращают2два ответа
# boolean - тип данных имеющий 2 значения :
# true; false

# print(bool(0)) #false
# print(bool(10)) #true
# print(bool(' ')) #true
# print(bool('')) #false
# print(bool(None)) #false


' равенство'
5 == 5 #true
'не равенство'
5 != 20 # true
' больше/меньше или равно'
5 >= 10 # falce
10 >= 3 # true
3 >= 3 #true
10 <= 5 # false
5 <= 5 #true

'5' == 5 #false
'hello' == 'hello' #true
'hello' == 'Hello' #false


'=======and or not===='
 
 # and - и(и то и другое
# or - или
# not - отрицание
'============and================'
# возвращает тру если свсе выражения дали тру 

a = 5
b = 6

#true   и    #true
a == 5 and b == 6 #true

#falce   и    #true
a == 6 and b == 6 #false

#true   и   #false
a == 5 and b == 2 #false

'==OR==' 
# возвращает тру, если хотя бы одно из выражений вернул тру, или все

c = 30
d = 36

#true или #true
c == 30 or d == 36 #true

#falce  или  #true
c == 1 or d == 36 #true

# true  или  #falce
c == 30 or d < 35  #rue

#false   или  #falce
c <= 31 or d >= 37 #false

'====not==='
# это частица НЕ, которая меняет значение на противоположное
# not False -> True
# not True -> False

# a = 10
# b = 5

# #not #true   или #falce  и #true
# not a == b or b > 10 and 10 == a  #true, true или #falce - true, true и true - true


# not 5 != 5 # true


# bool(None) #false
# bool('None') #true
# bool([]) #false



'=======условные операторы======'
#условные операторы - это конструкция которая используется для того чтобы при разных входных данных код работал по разному(в зависимости от условия)

# pogoda = 'солнце'
# if pogoda == 'дождь':
#     print('взял зонт')  
# elif pogoda == 'снег' :
#     print('взял шапку и шарф')
# elif pogoda == 'солнце' :
#     print('взял очки')
# else:
#     print('сижу дома') # выходит если сверху ниче неверно


# # # в одной конструкции мы можем использовать только один if    
# # в одной конструкции мы может использовать неограниченное колво elif, или не использовать его вовсе
# # в одной конструкции мы может исп-вать только один elseб или не исп-вать вовсе
    
# num = int(input('введите число')) 
# if num > 0 :
#     print('число положительное')
# elif num < 0 :
#     print('число отрицательное')
# else:
#     print('число 0')








'========тернарный оператор======='
# тертарный оператор = условия в одну строку


# тело1 if условие1 else тело2, елифа не будет

# mun = 19
# if mun > 0 :
#     massage = 'положительное число'
# else:
#     massage = 'отрицательное число'
# print(massage)


# mun = -2
# message = 'положительное число' if mun > 0 else 'отрицательное число'
# print(message) # выйдет else


# str = 'hello'
# print(ord('h'))


list_ = [1, 'abcd', 3, '1', 4, 'xyz', 5, 'pqr', 7, 5, 12] 
sum_ = 0 
res = [int(x) 
       for x in list_ 
        if type(x) == int or x.isdigit()] 
for i in res: 
    sum_ += i 
print(sum_)
