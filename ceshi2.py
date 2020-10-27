class RapName:
    def __init__(self, name: str, data: list):
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
                self.guanxi_list_data[guanxi.name] = guanxi.data[data - 1]
        if isinstance(data, str) is True:
            temp1 = data.split("q")
            self.guanxi_list_data[guanxi.name] = data[int(temp1[0]) - 1:int(temp1[1])]


class RapList:
    raplist = []

    def __init__(self):
        self.raplist_data = {}
        self.raplist_name = {}

    def add_list(self, data):
        self.raplist_name[data.name] = data.guanxi_list
        self.raplist_data[data.name] = data

    def xunzhaogx(self,data,name):
        for obj in data.guanxi_list:
            if obj == name:
                return True
        return False

    def xunzhaogx1(self,data,name,yizhao_list=None):
        if yizhao_list == None:
            yizhao_list = []
        yizhao_list.append(data.name)



ceshi1 = RapName("ceshi1", [["1"]])
ceshi2 = RapName("ceshi2", [["2"], ["3"]])
ceshi3 = RapName("ceshi3", [["3"]])
ceshi4 = RapName("ceshi4", [["4"]])
ceshi5 = RapName("ceshi5", [["5"]])

ceshi1.add(ceshi2, 0)
ceshi1.add(ceshi3, 0)
ceshi1.add(ceshi4, 0)

ceshi2.add(ceshi1, 0)
ceshi2.add(ceshi4, 0)
ceshi2.add(ceshi5, 0)

ceshi3.add(ceshi1, 0)
ceshi3.add(ceshi2, 0)

ceshi4.add(ceshi5, 0)

ceshi5.add(ceshi1, 0)
temp1 = RapList()
temp1.add_list(ceshi1)
temp1.add_list(ceshi2)
temp1.add_list(ceshi3)
temp1.add_list(ceshi4)
temp1.add_list(ceshi5)

print(temp1.raplist_name)

# def chazhaoguanxi(data,name):
#     for obj in data.guanxi_list:
#         if obj == name:
#             return True
#     return False
#
#
# def guanxicz(data, name, yizhao_data=None):
#     if yizhao_data is None:
#         yizhao_data = []
#     yizhao_data.append(data.name)
#     if chazhaoguanxi(data,name) == False:
#

