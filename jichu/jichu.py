import win32gui
from comtypes import client
import random
import time
import threading
import math
import datetime


class JiChu:
    def __init__(self, pic_comfig):
        self.pic_path = pic_comfig[0]
        self.pic_format = pic_comfig[1]
        self.pic_col = pic_comfig[2]
        self.hwnd = 0
        self.xc_sum = 1
        self.dqzifu_sum = -1
        self.lw = client.CreateObject('lw.lwsoft3')
        "--------------------------------------------"
        self.find_word_data_coord = []
        self.find_word_data_name = ""
        self.find_word_data_col = ""
        self.find_word_data_sim = 0
        self.find_word_data_back = 0
        self.find_word_data_time = 0
        self.find_word_data_x = -1
        self.find_word_data_y = -1
        "--------------------------------------------"
        self.find_pic_data_path = ""
        self.find_pic_data_format = ""
        self.find_pic_data_col_cast = ""
        self.find_pic_data_coord = []
        self.find_pic_data_name = ""
        self.find_pic_data_sum = 0
        self.find_pic_data_sim = 0
        self.find_pic_data_click = 0
        self.find_pic_data_x_cast_temp = []
        self.find_pic_data_x_cast = 0
        self.find_pic_data_y_cast_temp = []
        self.find_pic_data_y_cast = 0
        self.find_pic_data_time_out = 0
        self.find_pic_data_elay_time = 0
        self.find_pic_data_Delay_time = 0
        self.find_pic_data_x = -1
        self.find_pic_data_y = -1
        "--------------------------------------------"
        self.find_col_data_coord = []
        self.find_col_data_find_color = ""
        self.find_col_data_sim = 0
        self.find_col_data_dire = 0
        self.find_col_data_offset_color = ""
        self.find_col_data_time_out = 0
        self.find_col_data_x = -1
        self.find_col_data_y = -1

    def leidianbang(self, data, mingzi):  # 雷电模拟器绑定
        hwnd = win32gui.FindWindow("LDPlayerMainFrame", data)
        ch_hwnd = win32gui.FindWindowEx(hwnd, 0, "RenderWindow", "TheRender")
        self.hwnd = ch_hwnd
        print('句柄为：' + str(ch_hwnd))
        leidianbang_temp = self.lw.BindWindow(ch_hwnd, 5, 4, 4, 1, 0)
        if leidianbang_temp == 1:
            print(mingzi + "绑定成功")
        else:
            print(mingzi + "绑定失败")

    def jiebang(self):  # 雷电模拟器解绑
        self.lw.ForceUnBindWindow(self.hwnd)

    def click(self, data):  # 点击
        x1 = data[0]
        y1 = data[1]
        click_temp2 = len(data)
        if click_temp2 == 3:
            if isinstance(data[2], str) is True:
                click_temp2 = data[2].split("q")
                offset = random.randint(click_temp2[0], click_temp2[1])
                x3 = random.randint(x1, x1 + offset)
                y3 = random.randint(y1, y1 + offset)
            else:
                offset = random.randint(0 - data[2], data[2])
                x1_temp = x1 + offset
                y1_temp = y1 + offset
                if x1_temp < x1:
                    x1_temp1 = x1
                    x1 = x1_temp
                    x1_temp = x1_temp1
                if y1_temp < y1:
                    y1_temp1 = y1
                    y1 = y1_temp
                    y1_temp = y1_temp1
                x3 = random.randint(x1, x1_temp)
                y3 = random.randint(y1, y1_temp)
        else:
            x2 = data[2]
            y2 = data[3]
            x3 = random.randint(x1, x2)
            y3 = random.randint(y1, y2)
        if x3 > 0 and y3 > 0:
            self.lw.MoveTo(x3, y3)
            click_temp3 = self.lw.LeftClick()
        else:
            return 0
        if click_temp3 > 0:
            return 1
        else:
            return 0

    def locus1(self, data):  # 坐标移动
        x1 = data[0]
        y1 = data[1]
        x2 = data[2]
        y2 = data[3]
        while x1 > x2 or x1 < x2 or y1 > y2 or y1 < y2:
            if x1 < x2:
                locus_temp1 = random.randint(3, 6)
                x1 = x1 + locus_temp1
            else:
                locus_temp1 = random.randint(3, 6)
                x1 = x1 - locus_temp1
            if y1 < y2:
                locus_temp1 = random.randint(3, 6)
                y1 = y1 + locus_temp1
            else:
                locus_temp1 = random.randint(3, 6)
                y1 = y1 - locus_temp1
            print("x:" + str(x1) + "   " + "y:" + str(y1))  # daying
            self.lw.MoveTo(x1, y1)
            self.random_time(0.001, 0.005)

    def huaping1(self, data):  # 滑屏1
        self.random_time(0.5, 1)
        self.lw.MoveTo(data[0], data[1])
        self.random_time(0.5, 1)
        self.lw.LeftDown()
        self.locus1(data)
        self.random_time(0.5, 1)
        self.lw.LeftUp()

    @staticmethod
    def random_time(min_data, max_data):  # 时间随机
        random_time_temp = random.randint(min_data * 1000, max_data * 1000) / 1000
        time.sleep(random_time_temp)
        return random_time_temp

    @staticmethod
    def zuobiaosuiji(data):  # 坐标随机
        return [random.randint(data[0], data[2]), random.randint(data[1], data[3])]

    @staticmethod
    def block(bl, data):  # 平均分块
        block_temp1 = bl.split("|")
        x = data[2] - data[0]
        y = data[3] - data[1]
        block_x1 = x / int(block_temp1[0])
        block_y1 = y / int(block_temp1[1])
        block_x3 = []
        block_y3 = []
        block_temp2 = []
        block_y2 = 0
        block_x2 = 0
        for i in range(int(block_temp1[0])):
            if i == 0:
                block_x2 = data[0]
                block_x3.append(block_x2)
                i = i + 1
            block_x2 = block_x2 + block_x1
            block_x3.append(int(block_x2))
        print(block_x3)
        for i in range(int(block_temp1[1])):
            if i == 0:
                block_y2 = data[1]
                block_y3.append(block_y2)
                i = i + 1
            block_y2 = block_y2 + block_y1
            block_y3.append(int(block_y2))
        print(block_y3)
        for i in range(int(block_temp1[0])):
            for k in range(int(block_temp1[1])):
                block_temp3 = [block_x3[i], block_y3[k], block_x3[i + 1], block_y3[k + 1]]
                block_temp2.append(block_temp3)
        return block_temp2

    @staticmethod
    def list_sum(data):  # 数组维度鉴定
        if isinstance(data, list) is True:
            if isinstance(data[0], list) is True:
                if isinstance(data[0][0], list) is True:
                    if isinstance(data[0][0][0], list) is True:
                        return 4
                    else:
                        return 3
                else:
                    return 2
            else:
                return 1
        else:
            return 0

    @staticmethod
    def dianjuli(datax1, datay1, datax2, datay2):
        tempx = int(datax1) - int(datax2)
        tempy = int(datay1) - int(datay2)
        if tempx < 0:
            tempx = 0 - tempx
        if tempy < 0:
            tempy = 0 - tempy
        temp1 = (tempx * tempx) + (tempy * tempy)
        tempzuobiao = math.sqrt(temp1)
        return tempzuobiao

    @staticmethod
    def shujuchuli1(data: str):
        if data == "":
            return -1
        temp1 = data.find("|")
        temp2 = []
        if temp1 != -1:
            temp1 = data.split("|")
            if len(temp1) > 1:
                for x in range(len(temp1)):
                    temp2[x] = temp1[x].split(",")
            '''格式为：[[第一个数据],[第二个数据]]'''
        else:
            temp2[0] = data.split(",")
        if len(temp2) == 0:
            return -1
        else:
            return temp2

    @staticmethod
    def shujuchuli2(data: str):
        if data == "":
            return [-1]
        temp1 = data.find("|")
        temp2 = []
        if temp1 != -1:
            temp1 = data.split("|")
            for x in range(len(temp1)):
                temp1[x] = temp1[x][2:]
            return [1, temp1]
        else:
            temp1 = data[2:]
            return [1, [temp1]]

    '''格式为：[第一个数据,第二个数据]'''

    @staticmethod
    def shujuchuli3(data: str):
        if data == "":
            return [-1]
        temp1 = data.find("|")
        temp2 = []
        if temp1 != -1:
            temp1 = data.split("|")
            for x in range(len(temp1)):
                temp2[x] = temp1[x].split(",")

        else:
            temp2[0] = data.split(",")
        if len(temp2) == 0:
            return [0]
        else:
            return [1, temp2]

    '''格式为：[[第一个数据],[第二个数据]]'''


class MyThread(threading.Thread):
    def __init__(self, func, args):
        super(MyThread, self).__init__()
        self.func = func
        self.args = args
        self.result = None
        self.__flag = threading.Event()  # 用于暂停线程的标识
        self.__flag.set()  # 设置为True
        self.__running = threading.Event()  # 用于停止线程的标识
        self.__running.set()  # 将running设置为True

    def run(self):
        self.__flag.wait()
        self.result = self.func(*self.args)

    def get_result(self):
        try:
            return self.result
        except Exception:
            return None

    def pause(self):
        self.__flag.clear()  # 设置为False, 让线程阻塞

    def resume(self):
        self.__flag.set()  # 设置为True, 让线程停止阻塞

    def stop(self):
        self.__flag.set()  # 将线程从暂停状态恢复, 如何已经暂停的话
        self.__running.clear()  # 设置为False


class RiZhi:
    rizhi1 = []
    shijian = ""
    renwu = 0
    gonghuizhijia = 0
    taisuo = 0
    dxc = 0

    def __init__(self, dizhi, mingcheng):
        self.dizhi = dizhi
        self.mingcheng = mingcheng

    def prcduqu1(self):
        f = open(self.dizhi + self.mingcheng, "r")
        data = f.readlines()
        for x in range(len(data)):
            temp1 = data[x].strip('\n')
            RiZhi.rizhi1.append(temp1)
        RiZhi.shijian = RiZhi.rizhi1[0]
        RiZhi.renwu = RiZhi.rizhi1[1]
        RiZhi.gonghuizhijia = RiZhi.rizhi1[2]
        RiZhi.taisuo = RiZhi.rizhi1[3]
        RiZhi.dxc = RiZhi.rizhi1[4]
        f.close()

    def prcxieru(self):
        RiZhi.rizhi1[0] = datetime.datetime.now().strftime('%Y-%m-%d') + "\n"
        RiZhi.rizhi1[1] = str(str(RiZhi.renwu) + "\n")
        RiZhi.rizhi1[2] = str(str(RiZhi.gonghuizhijia) + "\n")
        RiZhi.rizhi1[3] = str(str(RiZhi.taisuo) + "\n")
        RiZhi.rizhi1[4] = str(str(RiZhi.dxc) + "\n")
        f = open(self.dizhi + self.mingcheng, "w")
        f.writelines(RiZhi.rizhi1)
        f.close()


class RiZhi1:
    def __init__(self, path):
        self.path = path

    def utf_8_duqu(self, name):
        temp1 = open(self.path + name, "r", encoding='utf-8')
        temp2 = []
        temp1_data = temp1.readlines()
        for x in range(len(temp1_data)):
            temp1_data1 = temp1_data[x].strip('\n')
            temp2.append(temp1_data1)
        temp1.close()
        return temp2

    def utf_8_xieru(self, xieru_time: str, name, data):
        temp1 = []
        temp1.append(datetime.datetime.now().strftime('%Y-%m-%d') + '-' + xieru_time + "\n")
        for x in range(len(data)):
            data[x] = str(data[x]) + "\n"
        temp1 = temp1 + data
        temp2 = open(self.path + name, "w", encoding='utf-8')
        temp2.writelines(temp1)
        temp2.close()
        return 1


class InterFace:
    def __init__(self, name: str, data: list):
        self.name = name  # 此对象名
        self.data = data  # 怎么去到次对象的数据
        self.guanxi_list = []  # 此对象能去的对象名字
        self.guanxi_list_data = {}  # 此对象能去的对象的数据
        self.guanxi_list_obj = []  # 此对象能去的对象

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

    def get_go_map_path(self,xz_data,zhao_data,yizhao_list=None):  # 获取当前对象去目标对象路径
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
            if self.map_obj_list_seek(all_list,zhao_temp1.name):
                continue
            zhao_temp2 = self.get_go_map_path(zhao_temp1,zhao_data,all_list)
            #
            if 0 < len(zhao_temp2) < len(res) or len(res) == 0:
                res = zhao_temp2
        #
        if len(res) > 0:
            res.insert(0,xz_data)
        return res

    def present_go_target(self, now: str, target: str):
        return self.get_go_map_path(self.raplist_data[now], self.raplist_data[target])
