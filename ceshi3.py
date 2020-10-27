def di_gui(n):
    print(n, "<===1====>")
    if n > 0:
        di_gui(n - 1)
    print(n, '<===2====>')

def ceshi(n,temp1):
    print(n)
    if n < 10:
        if n > 5:
            temp1.append(n)
            if len(temp1) == 3:
                return 1
        ceshi(n+1,temp1)
    print(n)

# di_gui(7) # 外部调用后打印的结果是？

temp1 = []
ceshi(1,temp1)
print(temp1)