import win32gui
from comtypes import client
import random
import time
import math
import pythoncom
import threading

"乐玩对象池"


class JiChu:
    def __init__(self, pic_comfig):
        self.pic_path = pic_comfig[0]
        self.pic_format = pic_comfig[1]
        self.pic_col = pic_comfig[2]
        self.hwnd = 0
        self.xc_sum = 1
        self.dqzifu_sum = -1
        pythoncom.CoInitialize()
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

    def leidianbang(self, data, mingzi=""):  # 雷电模拟器绑定
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
    '------------------------------------------------------------------------------------------------------------------'
    '找字'

    def find_word_data_shezhi(self, data, find_word_data_coord=None, find_word_data_col=None, find_word_data_sim=None,
                              find_word_data_back=None, find_word_data_time=None):
        if find_word_data_coord is not None:
            self.find_word_data_coord = find_word_data_coord
        else:
            self.find_word_data_coord = data[0]
        self.find_word_data_name = data[1]
        if find_word_data_col is not None:
            self.find_word_data_col = find_word_data_col
        else:
            self.find_word_data_col = data[2]
        if find_word_data_sim is not None:
            self.find_word_data_sim = find_word_data_sim
        else:
            self.find_word_data_sim = data[3]
        if find_word_data_back is not None:
            self.find_word_data_back = find_word_data_back
        else:
            self.find_word_data_back = data[4]
        if find_word_data_time is not None:
            self.find_word_data_time = find_word_data_time
        else:
            self.find_word_data_time = data[5]
        self.find_word_data_x = -1
        self.find_word_data_y = -1

    def find_word(self):
        find_word_temp1 = 1
        time_process = 0
        while find_word_temp1 == 1:
            time_start = time.time()
            find_word_temp2 = self.lw.FindStr(self.find_word_data_coord[0],
                                              self.find_word_data_coord[1],
                                              self.find_word_data_coord[2],
                                              self.find_word_data_coord[3],
                                              self.find_word_data_name,
                                              self.find_word_data_col,
                                              self.find_word_data_sim,
                                              self.find_word_data_back)
            if find_word_temp2 == 1:
                self.find_word_data_x = self.lw.x
                self.find_word_data_y = self.lw.y
                return 1
            else:
                time_end = time.time()
                time_process = time_process + time_end - time_start
                if time_process > self.find_word_data_time or time_process == self.find_word_data_time:
                    self.find_word_data_x = -1
                    self.find_word_data_y = -1
                    return 0

    def find_word_ex(self):
        find_word_ex_temp1 = 1
        ex_time_process = 0
        while find_word_ex_temp1 == 1:
            ex_time_start = time.time()
            find_word_ex_temp2 = self.lw.FindStrEx(self.find_word_data_coord[0],
                                                   self.find_word_data_coord[1],
                                                   self.find_word_data_coord[2],
                                                   self.find_word_data_coord[3],
                                                   self.find_word_data_name,
                                                   self.find_word_data_col,
                                                   self.find_word_data_sim,
                                                   self.find_word_data_back)
            if find_word_ex_temp2 is not None:
                find_word_ex_temp3 = find_word_ex_temp2.find("|")
            else:
                find_word_ex_temp3 = -1
            if find_word_ex_temp3 == -1 and find_word_ex_temp2 is not None:
                find_word_ex_temp2 = find_word_ex_temp2.split(",")
                return [1, find_word_ex_temp2]
            if find_word_ex_temp3 > -1:
                find_word_ex_temp2 = find_word_ex_temp2.split("|")
                for xx in range(len(find_word_ex_temp2)):
                    find_word_ex_temp2[xx] = find_word_ex_temp2[xx].split(",")
                return [1, find_word_ex_temp2]
            else:
                ex_time_end = time.time()
                ex_time_process = ex_time_process + ex_time_end - ex_time_start
                if ex_time_process == self.find_word_data_time or ex_time_process > self.find_word_data_time:
                    self.find_word_data_x = -1
                    self.find_word_data_y = -1
                    return [0]

    def find_word_ex1(self):
        find_word_ex_temp1 = 1
        ex_time_process = 0
        while find_word_ex_temp1 == 1:
            ex_time_start = time.time()
            find_word_ex_temp2 = self.lw.FindStrEx(self.find_word_data_coord[0],
                                                   self.find_word_data_coord[1],
                                                   self.find_word_data_coord[2],
                                                   self.find_word_data_coord[3],
                                                   self.find_word_data_name,
                                                   self.find_word_data_col,
                                                   self.find_word_data_sim,
                                                   self.find_word_data_back)
            if find_word_ex_temp2 is not None:
                return [1, find_word_ex_temp2]
            else:
                ex_time_end = time.time()
                ex_time_process = ex_time_process + ex_time_end - ex_time_start
                if ex_time_process == self.find_word_data_time or ex_time_process > self.find_word_data_time:
                    self.find_word_data_x = -1
                    self.find_word_data_y = -1
                    return [0]

    '------------------------------------------------------------------------------------------------------------------'
    '找图'

    def find_pic_data_shezhi(self, config, data):
        self.find_pic_data_path = config[0]
        self.find_pic_data_format = config[1]
        self.find_pic_data_col_cast = config[2]
        if self.find_pic_data_path == "":
            self.find_pic_data_path = self.pic_path
        if self.find_pic_data_format == "":
            self.find_pic_data_format = self.pic_format
        if self.find_pic_data_col_cast == "":
            self.find_pic_data_col_cast = self.pic_col
        self.find_pic_data_coord = data[0]
        self.find_pic_data_name = data[1][0]
        self.find_pic_data_sum = data[1][1]
        self.find_pic_data_sim = data[2][0]
        self.find_pic_data_click = data[2][1]
        self.find_pic_data_x_cast = data[2][2]
        if isinstance(self.find_pic_data_x_cast, int) is True:
            self.find_pic_data_x_cast = int(
                random.randint(0 - self.find_pic_data_x_cast, self.find_pic_data_x_cast))
        if isinstance(self.find_pic_data_x_cast, str) is True:
            self.find_pic_data_x_cast_temp = self.find_pic_data_x_cast.split("q")
            self.find_pic_data_x_cast = int(
                random.randint(int(self.find_pic_data_x_cast_temp[0]), int(self.find_pic_data_x_cast_temp[1])))
        self.find_pic_data_y_cast = data[2][3]
        if isinstance(self.find_pic_data_y_cast, int) is True:
            self.find_pic_data_y_cast = int(
                random.randint(0 - self.find_pic_data_y_cast, self.find_pic_data_y_cast))
        if isinstance(self.find_pic_data_y_cast, str) is True:
            self.find_pic_data_y_cast_temp = self.find_pic_data_y_cast.split("q")
            self.find_pic_data_y_cast = int(
                random.randint(int(self.find_pic_data_y_cast_temp[0]), int(self.find_pic_data_y_cast_temp[1])))
        self.find_pic_data_time_out = data[3][0] * 1000
        self.find_pic_data_Delay_time = data[3][1] * 1000
        self.find_pic_data_x = -1
        self.find_pic_data_y = -1

    def find_pic_data_shezhi1(self, data, config=None, find_pic_data_coord=None, find_pic_data_sim=None,
                              find_pic_data_click=None, find_pic_data_x_cast=None, find_pic_data_y_cast=None,
                              find_pic_data_time_out=None, find_pic_data_Delay_time=None):
        if config is not None:
            self.find_pic_data_path = config[0]
            self.find_pic_data_format = config[1]
            self.find_pic_data_col_cast = config[2]
        else:
            self.find_pic_data_path = self.pic_path
            self.find_pic_data_format = self.pic_format
            self.find_pic_data_col_cast = self.pic_col
        if self.find_pic_data_path == "":
            self.find_pic_data_path = self.pic_path
        if self.find_pic_data_format == "":
            self.find_pic_data_format = self.pic_format
        if self.find_pic_data_col_cast == "":
            self.find_pic_data_col_cast = self.pic_col
        if find_pic_data_coord is not None:
            self.find_pic_data_coord = find_pic_data_coord
        else:
            self.find_pic_data_coord = data[0]
        if find_pic_data_sim is not None:
            self.find_pic_data_sim = find_pic_data_sim
        else:
            self.find_pic_data_sim = data[2][0]
        if find_pic_data_click is not None:
            self.find_pic_data_click = find_pic_data_click
        else:
            self.find_pic_data_click = data[2][1]
        if find_pic_data_x_cast is not None:
            self.find_pic_data_x_cast = find_pic_data_x_cast
        else:
            self.find_pic_data_x_cast = data[2][2]
        self.find_pic_data_x_cast = self.data_cast(self.find_pic_data_x_cast)
        if find_pic_data_y_cast is not None:
            self.find_pic_data_y_cast = find_pic_data_y_cast
        else:
            self.find_pic_data_y_cast = data[2][2]
        self.find_pic_data_y_cast = self.data_cast(self.find_pic_data_y_cast)
        if find_pic_data_time_out is not None:
            self.find_pic_data_time_out = find_pic_data_time_out
        else:
            self.find_pic_data_time_out = data[3][0] * 1000
        if find_pic_data_Delay_time is not None:
            self.find_pic_data_Delay_time = find_pic_data_Delay_time
        else:
            self.find_pic_data_Delay_time = data[3][1] * 1000

    @staticmethod
    def data_cast(data):
        if isinstance(data, int) is True:
            return int(random.randint(0 - data, data))
        if isinstance(data, str) is True:
            data_temp = data.split("q")
            return int(random.randint(int(data_temp[0]), int(data_temp[1])))

    def find_pic(self):
        find_pic_temp1 = 0
        for z in range(int(self.find_pic_data_sum)):
            find_pic_temp1 = self.lw.findpic(self.find_pic_data_coord[0],
                                             self.find_pic_data_coord[1],
                                             self.find_pic_data_coord[2],
                                             self.find_pic_data_coord[3],
                                             self.find_pic_data_path +
                                             self.find_pic_data_name +
                                             str(z + 1) +
                                             self.find_pic_data_format,
                                             self.find_pic_data_col_cast,
                                             self.find_pic_data_sim, 0,
                                             self.find_pic_data_time_out,
                                             self.find_pic_data_click,
                                             self.find_pic_data_x_cast,
                                             self.find_pic_data_y_cast,
                                             self.find_pic_data_Delay_time)
            if find_pic_temp1 == 1:
                self.find_pic_data_x = self.lw.x
                self.find_pic_data_y = self.lw.y
                return 1
        if find_pic_temp1 == 0:
            return 0

    def find_pic1(self, num=1):
        find_pic_temp1 = self.lw.findpic(self.find_pic_data_coord[0],
                                         self.find_pic_data_coord[1],
                                         self.find_pic_data_coord[2],
                                         self.find_pic_data_coord[3],
                                         self.find_pic_data_path +
                                         self.find_pic_data_name +
                                         str(num) +
                                         self.find_pic_data_format,
                                         self.find_pic_data_col_cast,
                                         self.find_pic_data_sim, 0,
                                         self.find_pic_data_time_out,
                                         self.find_pic_data_click,
                                         self.find_pic_data_x_cast,
                                         self.find_pic_data_y_cast,
                                         self.find_pic_data_Delay_time)
        if find_pic_temp1 == 1:
            self.find_pic_data_x = self.lw.x
            self.find_pic_data_y = self.lw.y
            return 1
        else:
            return 0

    def find_pic_ex(self):
        find_pic_ex_temp1 = 0
        find_pic_ex_temp2 = ""
        for x in range(self.find_pic_data_sum):
            find_pic_ex_temp2 = find_pic_ex_temp2 + str(
                self.find_pic_data_path + self.find_pic_data_name + str(x + 1) + self.find_pic_data_format + "|")
        find_pic_ex_temp2 = find_pic_ex_temp2.strip('|')
        find_pic_ex_temp1 = self.lw.FindPicEx(self.find_pic_data_coord[0],
                                              self.find_pic_data_coord[1],
                                              self.find_pic_data_coord[2],
                                              self.find_pic_data_coord[3],
                                              find_pic_ex_temp2,
                                              self.find_pic_data_col_cast,
                                              self.find_pic_data_sim, 0,
                                              self.find_pic_data_time_out,
                                              self.find_pic_data_click,
                                              self.find_pic_data_x_cast,
                                              self.find_pic_data_y_cast,
                                              self.find_pic_data_Delay_time)
        return [1, find_pic_ex_temp1]

    '------------------------------------------------------------------------------------------------------------------'
    '找色'

    def find_col_data_chuli(self, data, time_out):
        self.find_col_data_coord = data[0]
        self.find_col_data_find_color = data[1]
        self.find_col_data_sim = data[2]
        self.find_col_data_dire = data[3]
        if len(data) > 4:
            self.find_col_data_offset_color = data[4]
        else:
            self.find_col_data_offset_color = ""
        self.find_col_data_time_out = int(time_out) * 1000
        self.find_col_data_x = -1
        self.find_col_data_y = -1

    def find_col1(self):
        temp1 = self.lw.FindColor(self.find_col_data_coord[0],
                                  self.find_col_data_coord[1],
                                  self.find_col_data_coord[2]
                                  , self.find_col_data_coord[3],
                                  self.find_col_data_find_color,
                                  self.find_col_data_sim,
                                  self.find_col_data_dire,
                                  self.find_col_data_time_out)
        if temp1 == 1:
            return 1
        else:
            return 0

    def find_multi_color1(self):
        temp1 = self.lw.FindMultiColor(self.find_col_data_coord[0],
                                       self.find_col_data_coord[1],
                                       self.find_col_data_coord[2]
                                       , self.find_col_data_coord[3],
                                       self.find_col_data_find_color,
                                       self.find_col_data_offset_color,
                                       self.find_col_data_sim,
                                       self.find_col_data_dire
                                       , self.find_col_data_time_out)
        if temp1 == 1:
            return 1
        else:
            return 0

    def find_col2(self):
        temp1 = self.lw.FindColorEx(self.find_col_data_coord[0],
                                    self.find_col_data_coord[1],
                                    self.find_col_data_coord[2]
                                    , self.find_col_data_coord[3],
                                    self.find_col_data_find_color,
                                    self.find_col_data_sim,
                                    self.find_col_data_dire,
                                    self.find_col_data_time_out)
        return temp1

    def find_multi_color2(self):
        temp1 = self.lw.FindMultiColor(self.find_col_data_coord[0],
                                       self.find_col_data_coord[1],
                                       self.find_col_data_coord[2]
                                       , self.find_col_data_coord[3],
                                       self.find_col_data_find_color,
                                       self.find_col_data_offset_color,
                                       self.find_col_data_sim,
                                       self.find_col_data_dire
                                       , self.find_col_data_time_out)
        return temp1


class WorK:
    def __init__(self, config, xm_name, windos_name, add_num, limit_state=False, limit_add_sum=0):
        self.pic_config = config
        self.xm_name = xm_name
        self.stater = []
        self.worker = {}
        self.worker_sum = 0
        self.lock = threading.Lock()
        self.add_num = add_num
        self.limit_state = limit_state
        self.limit_add_sum = limit_add_sum
        self.windos_name = windos_name
        self.worker_rec(self.add_num)

    def worker_add(self, num: int):
        for x in range(num):
            worker_temp1 = x + 1 + self.worker_sum
            self.worker[self.xm_name + str(worker_temp1)] = JiChu(self.pic_config)
            self.stater.append(1)
            self.worker[self.xm_name + str(worker_temp1)].ldbangding(self.windos_name,
                                                                     mingzi=self.windos_name + str(worker_temp1))
        self.worker_sum = self.worker_sum + num

    def worer_distr(self, data: int, name=None, num=None):
        while True:
            self.lock.acquire()
            if data == 1:
                for x in range(self.worker_sum):
                    if self.stater[x] == 1:
                        self.stater[x] = 0
                        self.lock.release()
                        return self.xm_name + str(x + 1)
            if data == 2:
                data_temp = 0
                for x in self.worker.keys():
                    if x == name:
                        self.stater[data_temp] = 1
                        self.lock.release()
                        return 1
                    data_temp = data_temp + 1
            if data == 3:
                self.worker_add(num)
                self.lock.release()
                return 1
            if data == 4:
                self.worker_add(1)
                for x in range(self.worker_sum):
                    if self.stater[x] == 1:
                        self.stater[x] = 0
                        self.lock.release()
                        return self.xm_name + str(x + 1)
            self.lock.release()
            data_temp1 = 0
            while True:
                for x in range(self.worker_sum):
                    if self.stater[x] == 1:
                        break
                data_temp1 = data_temp1 + 1
                time.sleep(0.1)
                if data_temp1 > 5:
                    data_temp1 = 0
                    if self.worker_sum < self.add_num + self.limit_add_sum:
                        self.worer_distr(4)

    def worker_find(self, num):
        if num == 1:
            return self.worer_distr(1)
        else:
            temp = []
            for x in range(num):
                temp.append(self.worer_distr(1))
            return temp

    def worker_complete(self, name):
        if isinstance(name, str) is True:
            self.worer_distr(2, name=name)
        if isinstance(name, list) is True:
            for x in range(len(name)):
                self.worer_distr(2, name=name[x])

    def worker_rec(self, num):
        self.worer_distr(3, num=num)


"======================================================================================================================"

"线程池"


class MyThreadEx(threading.Thread):

    def __init__(self, name1):
        super().__init__()
        self.result = None
        self.name1 = name1
        self.func: object
        self.args = ()
        self.keyword = {}
        self.event = threading.Event()
        self.result_state_wait = threading.Event()  # 返回等待
        self.event.clear()
        self.state = False  # 线程是否循环执行任务（默认非循环执行任务）
        self.run_state = False  # 线程任务是否在运行（默认没有运行）
        self.run_whether_state = False  # 线程是否就绪（默认非就绪）
        self.stop = False  # 是否停止线程（默认不停止）
        self.result_state = False  # 线程是否发送返回值
        self.subscribe = False  # 线程是否无任务

    def on_theard_subscribe(self):
        self.subscribe = True

    def on_join(self):
        while True:
            if self.result_state is True:
                break

    def mytask(self, func, args, keyword=None):
        self.func = func
        self.args = args
        self.keyword = keyword
        self.event.set()

    def on_state(self):
        self.state = True

    def off_state(self):
        self.state = False

    def Thread_stop(self):
        self.stop = True
        self.result_state_wait.set()
        self.event.set()

    def run(self):
        self.run_whether_state = True
        while True:
            self.event.wait()
            if self.state is False:
                self.event.clear()
            if self.stop is True:
                break
            self.run_state = True
            self.result_state_wait.clear()
            self.result_state = False
            if self.keyword is None:
                temp1 = self.func(*self.args)
            else:
                temp1 = self.func(*self.args, **self.keyword)
            self.result_state = True
            self.result = temp1
            self.result_state_wait.wait()
            if self.state is False:
                self.run_state = False
        self.run_whether_state = False

    def get_result(self):
        try:
            self.result_state = None
            self.result_state_wait.set()
            self.subscribe = False
            return self.result
        except Exception:
            return None


class ListThread:
    def __init__(self, limit_state: bool, limit_num_add: int, thread_name: str, thread_num=10):
        self.limit_state = limit_state
        self.limit_num_add = limit_num_add
        self.thread_num = thread_num
        self.thread_now_num = 0
        self.thread_name = thread_name
        self.thread_list_obj = {}
        self.lock = threading.Lock()
        self.batch_listthread_add(thread_num)

    def batch_listthread_add(self, num):
        for x in range(num):
            self.thread_now_num = self.thread_now_num + 1
            self.thread_list_obj[str(self.thread_name) + str(self.thread_now_num)] = MyThreadEx(
                str(self.thread_name) + str(self.thread_now_num))
            self.thread_list_obj[str(self.thread_name) + str(self.thread_now_num)].start()

    def Theard_start_testing(self):
        for x in range(self.thread_now_num):
            if not self.thread_list_obj[str(self.thread_name) + str(x + 1)].run_whether_state:
                self.thread_list_obj[str(self.thread_name) + str(x + 1)].start()

    @staticmethod
    def task_state_set(data):
        temp = []
        for x in range(len(data)):
            temp.append([data[x], 0])
        return temp

    @staticmethod
    def task_tate_detection(data):
        for x in range(len(data)):
            if data[x][1] == 0:
                data[x][1] = 1
                return data[x]
        return False

    def findtheard(self):
        self.lock.acquire()
        for x in range(self.thread_now_num):
            if not self.thread_list_obj[str(self.thread_name) + str(x + 1)].subscribe:
                self.thread_list_obj[str(self.thread_name) + str(x + 1)].on_theard_subscribe()
                self.lock.release()
                return str(self.thread_name) + str(x + 1)
        if self.limit_state == True and self.thread_now_num < self.thread_num + self.limit_num_add:
            self.batch_listthread_add(1)
        self.lock.release()
        return False

    def findtheard_state(self):
        temp = 0
        for x in range(self.thread_now_num):
            if not self.thread_list_obj[str(self.thread_name) + str(x + 1)].subscribe:
                temp = temp + 1
        return temp

    def many_task(self, data):
        temp1 = self.task_state_set(data)
        temp2 = []
        while True:
            temp3 = []
            while True:
                temp4 = self.findtheard()
                if temp4 is not False:
                    temp5 = self.task_tate_detection(temp1)
                    if temp5 is False:
                        break
                    temp3.append(temp4)
                    if len(temp5[0]) == 2:
                        self.thread_list_obj[temp4].mytask(temp5[0][0], temp5[0][1])
                    else:
                        self.thread_list_obj[temp4].mytask(temp5[0][0], temp5[0][1], temp5[0][2])
                else:
                    break
            for x in range(len(temp3)):
                temp6 = self.theard_name_get_result(temp3[x])
                temp2.append(temp6)
                if len(temp2) == len(temp1):
                    return temp2

    def sing_task(self, data):
        while True:
            temp1 = self.findtheard()
            if temp1 is not False:
                if len(data[0]) == 2:
                    self.thread_list_obj[temp1].mytask(data[0][0], data[0][1])
                else:
                    self.thread_list_obj[temp1].mytask(data[0][0], data[0][1], data[0][2])
            return self.theard_name_get_result(temp1)

    def theard_name_join(self, name):
        self.thread_list_obj[name].on_join()

    def theard_name_get_result(self, name):
        self.theard_name_join(name)
        return self.thread_list_obj[name].get_result()

    def task_run(self, data):
        temp1 = self.findtheard()
        if len(data) == 1:
            self.thread_list_obj[temp1].mytask(self.sing_task, (data,))
        else:
            self.thread_list_obj[temp1].mytask(self.many_task, (data,))
        return temp1

    def take_run1(self, data):
        temp1 = self.findtheard()
        if len(data) == 1:
            self.thread_list_obj[temp1].mytask(self.sing_task, (data,))
        else:
            self.thread_list_obj[temp1].mytask(self.many_task, (data,))
        return self.theard_name_get_result(temp1)

    def stop(self):
        for x in range(self.thread_now_num):
            self.thread_list_obj[str(self.thread_name) + str(x + 1)].Thread_stop()


"======================================================================================================================"

"基础功能设置"


class AssemblyLine:
    def __init__(self, config, xm_name, windos_name, add_num, limit_state=False, limit_add_sum=0):
        self.worker = WorK(config, xm_name, windos_name, add_num, limit_state=limit_state, limit_add_sum=limit_add_sum)
        self.equip = ListThread(limit_state, limit_add_sum, xm_name, add_num)
        self.run_fun_state = {}
        self.lock = threading.Lock()

    '------------------------------------------------------------------------------------------------------------------'
    '基础功能'

    '点击'

    def click(self, data, min_time=0, max_time=1):
        temp1 = self.worker.worker_find(1)
        self.worker.worker[temp1].random_time(min_time, max_time)
        self.worker.worker[temp1].click(data)
        self.worker.worker_complete(temp1)
        return 1

    '------------------------------------------------------------------------------------------------------------------'
    '运行集合接口'

    def func(self, find: str, data, bottom: list = None, judge=False,
             #  找字默认数值
             find_word_data_coord=None,
             find_word_data_col=None,
             find_word_data_sim=None,
             find_word_data_back=None,
             find_word_data_time=None,
             # 找图默认数值
             find_pic_config=None,
             find_pic_data_coord=None,
             find_pic_data_sim=None,
             find_pic_data_click=None,
             find_pic_data_x_cast=None,
             find_pic_data_y_cast=None,
             find_pic_data_time_out=None,
             find_pic_data_Delay_time=None,
             #  功能数值
             fun1_right=None,
             fun1_fail=None,
             fun2_right=None,
             fun2_fail=None,
             fun3_right=None,
             fun3_fali=None
             ):
        if bottom is None:
            bottom = []
        if fun1_right is None:
            fun1_right = []
        if fun1_fail is None:
            fun1_fail = []
        if fun2_right is None:
            fun2_right = []
        if fun2_fail is None:
            fun2_fail = []
        if fun3_right is None:
            fun3_right = []
        if fun3_fali is None:
            fun3_fali = []
        if self.run_fun_process('top', fun1_right, fun1_fail) == 1:
            temp3 = 0
            while True:
                temp1 = self.equip.task_run([self.run_fun_process, ('middle', fun2_right, fun2_fail)])
                temp2 = 0
                if find == '找字':
                    temp2 = self.equip.task_run([[self.find_word, (data,
                                                                   find_word_data_coord,
                                                                   find_word_data_col,
                                                                   find_word_data_sim,
                                                                   find_word_data_back,
                                                                   find_word_data_time)]])
                    temp1_temp = [[self.find_word, (data,
                                                    find_word_data_coord,
                                                    find_word_data_col,
                                                    find_word_data_sim,
                                                    find_word_data_back,
                                                    find_word_data_time)]]
                    temp1 = self.equip.task_run([self.run_fun_process, ('middle', fun2_right, fun2_fail + temp1_temp)])
                elif find == '找字ex':
                    temp2 = self.equip.task_run([self.find_wordex, (data,
                                                                    find_word_data_coord,
                                                                    find_word_data_col,
                                                                    find_word_data_sim,
                                                                    find_word_data_back,
                                                                    find_word_data_time)])
                    temp1_temp = [[self.find_wordex, (data,
                                                      find_word_data_coord,
                                                      find_word_data_col,
                                                      find_word_data_sim,
                                                      find_word_data_back,
                                                      find_word_data_time)]]
                    temp1 = self.equip.task_run([self.run_fun_process, ('middle', fun2_right, fun2_fail + temp1_temp)])
                elif find == '找字ex1':
                    temp2 = self.equip.task_run([self.find_wordex1, (data,
                                                                     find_word_data_coord,
                                                                     find_word_data_col,
                                                                     find_word_data_sim,
                                                                     find_word_data_back,
                                                                     find_word_data_time)])
                elif find == '找图':
                    temp2 = self.equip.task_run([self.find_pic, (find_pic_config, data)])
                elif find == '找图1':
                    temp2 = self.equip.task_run([self.find_pic1, (data, find_pic_config,
                                                                  find_pic_data_coord,
                                                                  find_pic_data_sim,
                                                                  find_pic_data_click,
                                                                  find_pic_data_x_cast,
                                                                  find_pic_data_y_cast,
                                                                  find_pic_data_time_out,
                                                                  find_pic_data_Delay_time)])
                elif find == '找图ex':
                    temp2 = self.equip.task_run([self.find_picex, (find_pic_config, data)])
                temp1 = self.equip.theard_name_get_result(temp1)
                temp2 = self.equip.theard_name_get_result(temp2)
                if isinstance(temp2, int) is True:
                    if temp3 == 0:
                        temp3 = temp2
                if isinstance(temp2, list) is True:
                    if isinstance(temp3, int) is True:
                        if temp3 == 0 and temp2[0] == 1:
                            temp3 = temp2
                if isinstance(temp2, list) is True:
                    if temp1 == 1 and temp2[0] == 1:
                        break
                else:
                    if temp1 == 1 and temp2 == 1:
                        break
                if judge:
                    break
            if self.run_fun_process('bottom', fun1_right, fun1_fail) == 0:
                bottom[0] = False
            else:
                bottom[0] = True
            return temp2

    def run_process(self, find, data, judge=False, time_out_num=4,  # 找字默认数值
                    find_word_data_coord=None,
                    find_word_data_col=None,
                    find_word_data_sim=None,
                    find_word_data_back=None,
                    find_word_data_time=None,
                    # 找图默认数值
                    find_pic_config=None,
                    find_pic_data_coord=None,
                    find_pic_data_sim=None,
                    find_pic_data_click=None,
                    find_pic_data_x_cast=None,
                    find_pic_data_y_cast=None,
                    find_pic_data_time_out=None,
                    find_pic_data_Delay_time=None,
                    #  功能数值
                    fun1_right=None,
                    fun1_fail=None, ):
        if fun1_right is None:
            fun1_right = [[]]
        if fun1_fail is None:
            fun1_fail = [[]]
        while True:
            temp1 = []
            temp2 = [[]]
            temp1_temp1 = 0
            temp1_temp2 = 0
            temp1_temp3 = 0
            temp2_temp = 0
            if find == "找字":
                temp1 = self.equip.task_run([[self.find_word, (data,
                                                               find_word_data_coord,
                                                               find_word_data_col,
                                                               find_word_data_sim,
                                                               find_word_data_back,
                                                               find_word_data_time)]])
                temp2 = [[self.find_word, (data,
                                           find_word_data_coord,
                                           find_word_data_col,
                                           find_word_data_sim,
                                           find_word_data_back,
                                           find_word_data_time)]]
                temp2_temp = 1
            elif find == "找字ex":
                temp1 = self.equip.task_run([self.find_wordex, (data,
                                                                find_word_data_coord,
                                                                find_word_data_col,
                                                                find_word_data_sim,
                                                                find_word_data_back,
                                                                find_word_data_time)])
                temp2 = [[self.find_wordex, (data,
                                             find_word_data_coord,
                                             find_word_data_col,
                                             find_word_data_sim,
                                             find_word_data_back,
                                             find_word_data_time)]]
                temp2_temp = 1
            elif find == "找字ex1":
                temp1 = self.equip.task_run([[self.find_wordex1, (data,
                                                                  find_word_data_coord,
                                                                  find_word_data_col,
                                                                  find_word_data_sim,
                                                                  find_word_data_back,
                                                                  find_word_data_time)]])
                temp2 = [[self.find_wordex1, (data,
                                              find_word_data_coord,
                                              find_word_data_col,
                                              find_word_data_sim,
                                              find_word_data_back,
                                              find_word_data_time)]]
                temp2_temp = 1
            elif find == "找图":
                temp1 = self.equip.task_run([[self.find_pic, (find_pic_config, data)]])
            if temp2_temp == 1:
                temp3 = self.equip.task_run([[self.run_fun_process, ('middle', fun1_right, fun1_fail + temp2)]])
            else:
                temp3 = self.equip.task_run([[self.run_fun_process, ('middle', fun1_right, fun1_fail)]])
            temp1 = self.equip.theard_name_get_result(temp1)
            temp3 = self.equip.theard_name_get_result(temp3)
            if temp1_temp2 == 0:
                if issubclass(temp1, list) is True:
                    if issubclass(temp1[0], int):
                        if temp1[0] == 1:
                            temp1_temp1 = temp1
                            temp1_temp2 = 1
                elif issubclass(temp1, int) is True:
                    if temp1 == 1:
                        temp1_temp1 = temp1
                        temp1_temp2 = 1
            if temp1_temp2 == 1 and temp3 == 1:
                return temp1_temp1
            elif judge:
                return temp1_temp1

            if temp1_temp3 == time_out_num:
                return None
            else:
                temp1_temp3 = temp1_temp3 + 1

    '运行过程额外操作过程设置'

    def run_fun(self, data, judge):
        if judge == '正确' or judge == 1:
            judge_temp = 1
        else:
            judge_temp = 0
        while True:
            if len(data) == 0:
                return 1
            elif len(data) == 1:
                temp1 = self.equip.take_run1(data)
                if temp1 == judge_temp:
                    return 1
            else:
                temp1 = self.equip.take_run1(data)
                temp2 = len(temp1)
                temp3 = 0
                for x in range(len(temp1)):
                    if JiChu.list_sum(temp1[x]) == 1:
                        if temp1[x][0] == judge_temp:
                            temp3 = temp3 + 1
                    elif JiChu.list_sum(temp1[x]) == 0:
                        if temp1[x][0] == judge_temp:
                            temp3 = temp3 + 1
                if temp2 == temp3:
                    return 1

    '运行过程额外操作设置'

    def run_funex(self, right_fun, fail_fun):
        temp1 = [self.run_fun, (right_fun, 1)]
        temp2 = [self.run_fun, (fail_fun, 0)]
        temp3 = self.equip.task_run(temp1)
        temp4 = self.equip.task_run(temp2)
        temp3 = self.equip.theard_name_get_result(temp3)
        temp4 = self.equip.theard_name_get_result(temp4)
        if temp3 == 1 and temp4 == 1:
            return 1
        else:
            return 0

    '运行过程额外操作状态设置'

    def run_fun_state_modify(self, name, value: bool = None, find=False):
        self.lock.acquire()
        if value is None:
            for x in self.run_fun_state.keys():
                if find:
                    if x == name:
                        self.run_fun_state[name] = True
                        self.lock.release()
                        return 1
                else:
                    if x == name:
                        if self.run_fun_state[name]:
                            self.run_fun_state[name] = False
                            self.lock.release()
                            return 1
                        else:
                            self.lock.release()
                            return 0
            if find:
                self.lock.release()
                return 0
            self.run_fun_state[name] = False
            self.lock.release()
            return 1
        else:
            for x in self.run_fun_state.keys():
                if x == name:
                    self.run_fun_state[name] = value
                    self.lock.release()
                    return 1
        return 1

    '运行过程额外操作设置接口'

    def run_fun_process(self, name: str, right_fun, fail_fun):
        judge = 0
        if self.run_fun_state_modify(name) == 1:
            while True:
                temp1 = self.run_funex(right_fun, fail_fun)
                if temp1 == 1:
                    return 1
                else:
                    judge = judge + 1
                if judge == 5:
                    return 0
        else:
            while True:
                if self.run_fun_state_modify(name, find=True) == 1:
                    return 1
                elif judge == 5:
                    return 0

    '------------------------------------------------------------------------------------------------------------------'

    def assem_add(self, num):
        self.worker.worker_add(num)
        self.equip.batch_listthread_add(num)

    '------------------------------------------------------------------------------------------------------------------'
    '找字基础功能设置'

    def find_word(self, data,
                  find_word_data_coord,
                  find_word_data_col,
                  find_word_data_sim,
                  find_word_data_back,
                  find_word_data_time):
        temp1 = self.worker.worker_find(1)
        self.worker.worker[temp1].find_word_data_shezhi(data, find_word_data_coord=find_word_data_coord,
                                                        find_word_data_col=find_word_data_col,
                                                        find_word_data_sim=find_word_data_sim,
                                                        find_word_data_back=find_word_data_back,
                                                        find_word_data_time=find_word_data_time)
        temp2 = self.worker.worker[temp1].find_word()
        self.worker.worker_complete(temp1)
        return temp2

    def find_wordex(self, data,
                    find_word_data_coord,
                    find_word_data_col,
                    find_word_data_sim,
                    find_word_data_back,
                    find_word_data_time):
        temp1 = self.worker.worker_find(1)
        self.worker.worker[temp1].find_word_data_shezhi(data, find_word_data_coord=find_word_data_coord,
                                                        find_word_data_col=find_word_data_col,
                                                        find_word_data_sim=find_word_data_sim,
                                                        find_word_data_back=find_word_data_back,
                                                        find_word_data_time=find_word_data_time)
        temp2 = self.worker.worker[temp1].find_wordex()
        self.worker.worker_complete(temp1)
        return temp2

    def find_wordex1(self, data,
                     find_word_data_coord,
                     find_word_data_col,
                     find_word_data_sim,
                     find_word_data_back,
                     find_word_data_time):
        temp1 = self.worker.worker_find(1)
        self.worker.worker[temp1].find_word_data_shezhi(data, find_word_data_coord=find_word_data_coord,
                                                        find_word_data_col=find_word_data_col,
                                                        find_word_data_sim=find_word_data_sim,
                                                        find_word_data_back=find_word_data_back,
                                                        find_word_data_time=find_word_data_time)
        temp2 = self.worker.worker[temp1].find_wordex1()
        self.worker.worker_complete(temp1)
        return temp2

    '------------------------------------------------------------------------------------------------------------------'
    '找图基础功能设置'

    def find_pic(self, config, data):
        temp1 = self.worker.worker_find(1)
        self.worker.worker[temp1].find_pic_data_shezhi(config, data)
        temp2 = self.worker.worker[temp1].find_pic()
        self.worker.worker_complete(temp1)
        return temp2

    def find_pic1(self, data, config,
                  find_pic_data_coord,
                  find_pic_data_sim,
                  find_pic_data_click,
                  find_pic_data_x_cast,
                  find_pic_data_y_cast,
                  find_pic_data_time_out,
                  find_pic_data_Delay_time):
        temp1 = self.worker.worker_find(1)
        self.worker.worker[temp1].find_pic_data_shezhi1(data, config=config, find_pic_data_coord=find_pic_data_coord,
                                                        find_pic_data_sim=find_pic_data_sim, find_pic_data_click=
                                                        find_pic_data_click, find_pic_data_x_cast=find_pic_data_x_cast,
                                                        find_pic_data_y_cast=find_pic_data_y_cast,
                                                        find_pic_data_time_out
                                                        =find_pic_data_time_out, find_pic_data_Delay_time=
                                                        find_pic_data_Delay_time)
        temp2 = self.worker.worker[temp1].find_pic1()
        self.worker.worker_complete(temp1)
        return temp2

    def find_picex(self, config, data):
        temp1 = self.worker.worker_find(1)
        self.worker.worker[temp1].find_pic_data_shezhi(config, data)
        temp2 = self.worker.worker[temp1].find_picex()
        self.worker.worker_complete(temp1)
        return temp2
