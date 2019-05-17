#def lazy_sum(*args):
#    def sum():
#        ax =0
#        for n in args:
#            ax = ax + n
#        return ax
#    return sum
#
#f = lazy_sum(1, 3, 5, 7, 9) 
#print(f)
#print(f())
#def count():
#    fs = []
#    for i in range(1, 4):
#        def f():
#            return i * i
#        fs.append(f)
#    return fs
#f1, f2, f3 = count()
#print(f1())
#print(f2())
#print(f3())
#def func():#外部函数
#    a = 1
#    print("This is func.")
#    def func1(num):
#        print("This is func1.")
#        print (num + a)
#    return func1
#
#var = func()
#var(3)

mylist = [1, 2, 3, 4, 5]

#def func(obj):
#    print('fuc', obj)
#    def func1(): 
#        obj[0] += 1
#        print('func1:', obj)
#    return func1
#var = func(mylist)
#
#var()
#var()
#var()
def func1(func):
    def func2():
        print('aaabbb')
        return func()
    return func2


@func1
def myprint():
    print('Hello')

myprint()
