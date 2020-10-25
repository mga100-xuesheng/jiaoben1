class RapName:
    def __init__(self, name:str, data:list):
        self.name = name  # 次对象名
        self.data = data  # 怎么去到次对象的数据
        self.guanxi_list = []  # 次对象能去的对象
        self.guanxi_list_data = {}  # 次对象能去的对象的数据

    def add(self, guanxi, data):
        self.guanxi_list.append(guanxi.name)
        if isinstance(data, int) is True:
            if data == 0:
                self.guanxi_list_data[guanxi.name] = guanxi.data
            else:
                self.guanxi_list_data[guanxi.name] = guanxi.data[data-1]
        if isinstance(data,str) is True:
            temp1 = data.split("q")
            self.guanxi_list_data[guanxi.name] = data[int(temp1[0])-1:int(temp1[1])]


class RapList:
    raplist = []

    def __init__(self):
        self.raplist_data = []

    def add_list(self,data):
        self.raplist_data.append(data)


ceshi1 = RapName("ceshi1",[["1"]])
ceshi2 = RapName("ceshi2",[["2"],["3"]])
ceshi3 = RapName("ceshi3",[["3"]])
ceshi4 = RapName("ceshi4",[["4"]])
ceshi5 = RapName("ceshi5",[["5"]])

ceshi1.add(ceshi2,0)
ceshi1.add(ceshi3,0)
ceshi1.add(ceshi4,0)

ceshi2.add(ceshi1,0)
ceshi2.add(ceshi4,0)
ceshi2.add(ceshi5,0)

ceshi3.add(ceshi1,0)
ceshi3.add(ceshi2,0)

ceshi4.add(ceshi5,0)

ceshi5.add(ceshi1,0)

print(ceshi1.guanxi_list)
print(ceshi2.guanxi_list)
print(ceshi3.guanxi_list)
print(ceshi4.guanxi_list)
print(ceshi5.guanxi_list)