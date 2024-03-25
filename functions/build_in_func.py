



'Zip'
# соединяет несколько последовательностей (поучаем генератор, в котором элементы - tuple)

list1 = [1,2,3]
list2 = ['a','b','c']
list3 = [10.3,19.2,18.4]

zipped = zip(list1,list2,list3)
print(list(zipped)) # [(1, 'a', 10.3), (2, 'b', 19.2), (3, 'c', 18.4)] - (list[tuple])

d_zip = zip(list1,list2)
print(dict(d_zip)) # {1: 'a', 2: 'b', 3: 'c'} - (dict{k:v})

'enumerate'
# нумерует последовательность (по дефолту с 0, тоже возвращает генератор)

#enumerated = enumerate('hello')
# print(enumerated) #<enumerate object at 0x7fa6d853bf80>
# print(list(enumerated))  #[(0, 'h'), (1, 'e'), (2, 'l'), (3, 'l'), (4, 'o')]

# enumerated = enumerate('hello',-99)
# print(list(enumerated)) #[(-99, 'h'), (-98, 'e'), (-97, 'l'), (-96, 'l'), (-95, 'o')]

#for i in enumerated:
    #print(i) #(0, 'h')
             #(1, 'e')
             #(2, 'l')
             # (3, 'l')
             # (4, 'o')
    

enum = enumerate([12,8,'hi',True,None,'go'], 100)
print(list(enum)) #[(100, 12), (101, 8), (102, 'hi'), (103, True), (104, None), (105, 'go')]

for i,v in enum:
    print(f'Номер: {i},Значение: {v} ')
# Номер: 100,Значение: 12 
# Номер: 101,Значение: 8 
# Номер: 102,Значение: hi 
# Номер: 103,Значение: True 
# Номер: 104,Значение: None 
# Номер: 105,Значение: go 
    
'map'
#принимает другую функцию и последовательность, мэп применяет функцию, которую мы передали на каждый элмент из последовательности. Возвращает map object.


list_ = [1,2,3,4]
def dunc(a):
    return str(a)
mapped = map(dunc, list_)
print(mapped) #<map object at 0x7f4cf34d6610>
print(list(mapped)) #['1', '2', '3', '4']


l1 = [1,2,3,4]
def func(l1):
    return l1 ** 2
m = map(func, l1)
print(list(m)) #[1, 4, 9, 16]


'lambda - это, одноразовая анонимная функция'

def func(n):
    return n ** 3
func(2) # 8

r = lambda n: n ** 3
print(r(2)) # 8

print((lambda n: n ** 3)(3)) # 27


l1 = [1,2,3,4]
m = map(lambda a:round(a**2, 3), l1)
print(list(m)) #[1, 4, 9, 16]

'Filter'
# эта функция принимает другую функцию и последовательность. Применяет функцию которую мы передали на каждый элемент последовательности и оставляет только те элементы, которые прошли проверку


list_1 = [-10,0,39,-12,-3,23,1,0]

def func(a):
    return a >= 0

filtered = filter(func, list_1)
print(list(filtered)) # [0, 39, 23, 1, 0]


f2 = filter(lambda a: a<=0, list_1)
print(list(f2)) #[-10, 0, -12, -3, 0]



ll1 = [1,2,3,4,5,6,7,7,8,]
print(list(filter(lambda a:a%2==0, ll1)))  #[2, 4, 6, 8]

'reduce'
# принимает функцию и последовательность, возвращает один результат (передоваемая функция должна принимать 2 аргумента)

from functools import reduce

list_ = [12,123,54,35,45]
r = reduce(lambda a,b: a + b , list_)
print(r) #269

d = {'a':1, 'a':2}
print(d)

from functools import reduce
list_ = [5, 6, 7, 8] 
result = reduce(lambda i,a: i * a, list_)
print(result)



#Eсли число в списке меньше 0, замените его на False, если больше, то на True. Результат сохраните в новой переменной result и выведите в консоль.
list_ = [-1, 2, 3, 5, -3, 7] 
result =list(map(lambda x: x > 0, list_)) 
print(result) #[False, True, True, True, False, True]