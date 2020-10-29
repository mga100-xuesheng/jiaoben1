class RapName:
    def __init__(self, name: str, data: list):
        self.name = name  # 次对象名
        self.data = data  # 怎么去到次对象的数据
        self.guanxi_list = []  # 次对象能去的对象
        self.guanxi_list_data = {}  # 次对象能去的对象的数据
        self.guanxi_list_obj = []

    def add(self, guanxi, data):
        self.guanxi_list.append(guanxi.name)
        self.guanxi_list_obj.append(guanxi)
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
        self.raplist_keyword = {}

    def add_list(self, data):
        self.raplist_name[data.name] = data.guanxi_list
        self.raplist_data[data.name] = data

    @staticmethod
    def xunzhaogx(data,name):
        for obj in data:
            if obj == name:
                return True
        return False

    def xunzhaogx1(self,xz_data,zhao_data,yizhao_list=None):
        if yizhao_list is None:
            yizhao_list = []
        #
        all_list = yizhao_list[:]
        all_list.append(xz_data.name)
        res = []
        #
        if xz_data.name == zhao_data.name:
            goWay = [xz_data]
            return goWay
        #
        for zhao_temp1 in xz_data.guanxi_list_obj:
            if self.xunzhaogx(all_list,zhao_temp1.name):
                continue
            zhao_temp2 = self.xunzhaogx1(zhao_temp1,zhao_data,all_list)
            #
            if 0 < len(zhao_temp2) < len(res) or len(res) == 0:
                res = zhao_temp2
        #
        if len(res) > 0:
            res.insert(0,xz_data)
        return res
    def fanhuilujin(self,nowdata:str,godata:str):
        return self.xunzhaogx1(self.raplist_data[nowdata],self.raplist_data[godata])


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


temp2 = temp1.xunzhaogx1(ceshi5,ceshi2)

for x in range(len(temp2)):
    print(temp2[x].name)
    print(temp2[x].data)
    print("")
temp3 = temp1.fanhuilujin("ceshi5","ceshi2")
for x in temp3:
    print(x.name)
    print(x.data)
    print("")



