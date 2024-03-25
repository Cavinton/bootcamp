"========================Декараторы===================="
#ФУНКЦИЯ ВЫСШЕГО ПОРЯДКА-ФУНКЦИЯБ,КОТОРАЯ ПРИНИМАЕТ В АРГУМЕНТЫ ФУНКЦИЮ ДРУГУЮ,СОЗДАЕТ ВНУТРИ СЕБЯ ФУНКЦИЮ,ВЫЗЫВАЕТ ВНУТРИ ДРУГУЮ ФУНКЦИЮ


# def func1():
#     pass


# def func2( a):# aфункцию вышего порядка так как принимает друггую функцию в аргументы
#     a()


# #декараторы-функция высшего порядка,которая нужна расширить функционал функции не изменяя ее (функция обертка)

# def glushitel(func):
#     def wrapper(*args,**kwargs):
#         text = func(*args,**kwargs)
#         return text + ' Тихо'
#     return wrapper

# def gun():
#     return 'Стреляет'

# wrapper = glushitel(gun)
# result = wrapper()
# print(result) #Стреляет Тихо
# print(gun()) # Cтреляет


# def glushitel(func):
#     def wrapper(*args,**kwargs):
#         text = func(*args,**kwargs)
#         return text + ' Тихо'
#     return wrapper

# @glushitel
# def gun():
#     return 'Стреляет'

# result = gun()
# print(result) #Стреляет Тихо



from datetime import datetime

def func_start_time(func):
    def wrapper():
        time_ = datetime.now().strftime('%d.%m.%Y %H:%M') 
        print(f'Функция запустилась {time_}')
        func()
    return wrapper
    
@func_start_time
def func():
    print('hi') #Функция запустилась 20.03.2024 19:53
                # hi

@func_start_time
def func1():
    print('hello') #ункция запустилась 20.03.2024 19:53
                    #hello

func()
func1() 

def decorator(num):
    def inner_decorator(func):
        def wrapper():
            for i in range(1,num+1):
               func()
            return wrapper
        return inner_decorator

@decorator(3)
def hello():
    print('helo world')

hello()