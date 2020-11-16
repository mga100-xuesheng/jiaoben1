aaa = [['899', '545', 1], ['920', '545', 3], ['907', '544', 4]]
bbb = [['899', '545', 1], ['920', '545', 5], ['907', '544', 2]]


def ceshi(data, data1):
    if data == 1:
        for x in range(len(data1)):
            for y in range(len(data1) - x - 1):
                if int(data1[y][0]) > int(data1[y + 1][0]):
                    temp3 = data1[y + 1]
                    data1[y + 1] = data1[y]
                    data1[y] = temp3
    return data1


print(ceshi(1, bbb))
