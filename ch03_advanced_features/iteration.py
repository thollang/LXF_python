def findMinAndMax(L):
    if L == []:
        return (None,None)
    min_num = L[0]
    max_num = L[0]
    for i in range(1,len(L)):
        if min_num > L[i]:
            min_num = L[i]
        if max_num < L[i]:
            max_num = L[i]
    return (min_num,max_num)
# 测试
if findMinAndMax([]) != (None, None):
    print('测试失败!')
elif findMinAndMax([7]) != (7, 7):
    print('测试失败!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('测试失败!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!')
else:
    print('测试成功!')



