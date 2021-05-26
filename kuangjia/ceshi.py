# import json
#
# ceshidata = {
#     'name': 'ceshi',
#     'data': '123456'
# }
# print(isinstance(ceshidata, list))


# def ceshi1(a,b):
#     print(a)
#     print(b)
#     return a
#
#
# def ceshi2(b):
#     print(b)
#     return b
#
#
# def ceshi3(fun, args, **kwargs):
#     temp = args
#     len(temp)
#     print('temp:')
#     print(len(temp))
#     print(temp)
#     fun(*temp, **kwargs)
#
#
# def ceshi4(*args):
#     return args
#
#
# c = [[ceshi1, ceshi4(1,2)], [ceshi2, ceshi4(2)]]
# print(c)
# for x in c:
#     ceshi3(x[0], x[1])

aaa = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
bbb = 7
ccc = len(aaa)
for x in range(len(aaa)):
    x = x + bbb
    if x == len(aaa):
        break
    if x == ccc:
        break
    print(aaa[x])
