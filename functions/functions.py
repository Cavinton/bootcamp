'====Функции===='
# это именованный блок кода, который может принимать аргументы, и возвращать результат


'Функции соблюдают принцип DRY(dont repeat Urself - не повторяй свой код несколько раз)'

'==аргументы и параметры==='

# параметры - переменные внутри функции, параметры создаем при создании функции
# аргументы - значения, которые мы передаем при вызове функции

def func(a,b): # параметры
    print(a,b)

func(10, 3) #аргументы


def my_sum(x,y):  # x,y - параметры
    a = x + y
    return a

res = my_sum(5, 10)  # 5,10 - аргументы
print(res) #15


'==================='


def hello_world():
    print('Hello')
print(hello_world()) # None

def hello_world():
    return 'Hello'
print(hello_world()) # Hello



def my_len(a): # переменная а
    count = 0
    for i in a:
        count = count + 1
    return count # 3,т к три элемента в а

print(my_len([12,'hi', 0])) # 3 

print(len('hello world')) # 11


'==Виды параметров==='

# 1.обязательные
# 2. необязательные:
   # 2.1 с дефолтом(значением по умолчанию)
   # 2.2 *args(все позиционные аргументы которые не попали в обязательные и с дефолтом)
   # 2.3 **kwargs (все лишние именованные аргументы)

'==Виды Аргументов==='

#1.Позиционные (по позиции)
#2. Именнованные(по названию(параметр=значение))


#pass/... - заглушка


# def func(num1,num2=2): - НЕОБЗ ДЕФОЛТ ВИД ПАРАМЕТРА НАМ2, ОБЯЗ-ЫЙ ВИД НАМ1
    

# func(10,20) - ПОЗИЦИОННЫЙ ВИД АРГ

def func(a,b, *args, **kwargs):
    print(a)
    print(b)
    print(args)
    print(kwargs)
func(5,1,10,4,2,5,1, hello = 'hi', abc = '123123')
#    a b  args(tuple)    kwargs(dict)

def div(x,y):
    if div == 0:
     print('IDINAHUI')
    else:
     print(x / y)
div(1,2)



dict_ = {'af':12,123:'asd',12321:222}
def dictionary(dict_):
    for k,v in dict_.items():
        print(k)

dictionary(dict_)


# MINI CALCULATOR

def add_(num1, num2): 
    return num1 + num2 

def sub_(num1, num2): 
    return num1 - num2 

def div_(num1, num2): 
    return num1 / num2 

def mult_(num1,num2): 
    return num1 * num2 

def calc(num1, num2, oper): 
    if oper == '+': 
        return add_(num1, num2) 
    elif oper == '-': 
        return sub_(num1, num2) 
    elif oper == '/': 
        return div_(num1, num2) 
    else: 
        return mult_(num1,num2) 
        
print(calc(1,2,'+'))

    






























