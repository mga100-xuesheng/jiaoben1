def aaa(a, b=0, c=1):
    print(a)
    print(b)
    print(c)


aaa(1, 3, 5)

a = []
bbb = ['ceshi', 'dasdawd']
for x in range(10):
    a.append([aaa, (bbb, 'dqweasd', 'dasda' + str(x))])
print(callable(aaa))

aa = []
bb = ['33,44', '44,55']
print(aa + bb)
