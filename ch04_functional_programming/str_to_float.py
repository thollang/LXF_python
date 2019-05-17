"""
利用map和reduce编写一个str2float函数，把字符串'123.456'转换成浮点数123.456：
"""

from functools import reduce
def str2int(s):
    digits={'1' : 1,
            '2' : 2,
            '3' : 3,
            '4' : 4,
            '5' : 5,
            '6' : 6,
            '7' : 7,
            '8' : 8,
            '9' : 9,
            '0' : 0}
    return digits[s]
def int2float(x, y):
    return 10 * x + y
def str2float(s):
    a, b = s.split(".")
    front = reduce(int2float, map(str2int, a)) 
    end = reduce(int2float, map(str2int, b)) / pow(10,len(b))
    return front + end



print('str2float(\'123.456\') =', str2float('123.456'))
if abs(str2float('123.456') - 123.456) < 0.00001:
    print('测试成功!')
else:
    print('测试失败!')
