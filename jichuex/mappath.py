class InterFace:
    def __init__(self, name: str, data: list, guanxi: list):
        self.name = name  # 此对象名
        self.data = data  # 怎么去到次对象的数据
        self.guanxi_list = []
        for x in guanxi:
            if x != self.name:
                self.guanxi_list.append(x)
        self.guanxi_list1 = guanxi  # 此对象能去的对象名字
        self.guanxi_list2 = []
        self.guanxi_list_data = {}  # 此对象能去的对象的数据
        self.guanxi_list_obj = []  # 此对象能去的对象

    def add(self, guanxi, data):
        if guanxi.name != self.name:
            self.guanxi_list2.append(guanxi.name)
            self.guanxi_list_obj.append(guanxi)
            if isinstance(data, int) is True:
                if data == 0:
                    self.guanxi_list_data[guanxi.name] = guanxi.data
                else:
                    self.guanxi_list_data[guanxi.name] = guanxi.data[data - 1]
            if isinstance(data, str) is True:
                temp1 = data.split("q")
                self.guanxi_list_data[guanxi.name] = data[int(temp1[0]) - 1:int(temp1[1])]


class Map:
    def __init__(self):
        self.raplist_data = {}
        self.raplist_name = {}
        self.raplist_keyword = {}

    def add_list(self, data):  # 添加地图对象
        self.raplist_name[data.name] = data.guanxi_list
        self.raplist_data[data.name] = data

    @staticmethod
    def map_obj_list_seek(data, name):  # 地图对象列表寻找
        for obj in data:
            if obj == name:
                return True
        return False

    def get_go_map_path(self, xz_data, zhao_data, yizhao_list=None):  # 获取当前对象去目标对象路径
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
            if self.map_obj_list_seek(all_list, zhao_temp1.name):
                continue
            zhao_temp2 = self.get_go_map_path(zhao_temp1, zhao_data, all_list)
            #
            if 0 < len(zhao_temp2) < len(res) or len(res) == 0:
                res = zhao_temp2
        #
        if len(res) > 0:
            res.insert(0, xz_data)
        return res

    def present_go_target(self, now: str, target: str):
        return self.get_go_map_path(self.raplist_data[now], self.raplist_data[target])
