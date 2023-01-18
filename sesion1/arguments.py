#Argumentos posicionales
def func1(a, b, c):
    print(a, b, c)

#func1(1, 2, 3)

# Keyword Arguments
#func1(c=1, a=5, b=3)


# Posicional y keyword
#func1(1, c=10, b=4)


# *Args  - Argumentos posicionales ilimitados
def add(*args):
    for n in args:
        print(n)


# add(1,3,4,5,6,7,8,43,2,3)
# **Kwargs - Unlimited keyword arguments
def calculate(**kwargs):
    #print(kwargs, type(kwargs))
    #print(kwargs['n4'])
    for key, value in kwargs.items():
        print(key, value)


#calculate(n1=5, n2= 4, n3= 7, n4=8, n5=9)

# *Args y **Kwargs
def func2(a, b, c, *args, **kwargs):
    print(a, b ,c) # Argumentos posicionales
    print(args)   # Args
    print(kwargs) # Kwargs


func2(1, 2, 3, 4, 5, 6, x=11, y=10)