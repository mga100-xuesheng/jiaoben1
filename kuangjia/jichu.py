import json
import pythoncom
from comtypes import client
import win32gui
import random
import time


class lw_obj:
    def __init__(self):
        pythoncom.CoInitialize()
        self.lw = client.CreateObject('lw.lwsoft3')
        self.hwnd = -1
        self.state = 0
        self.word_path_num = 0
        self.x = -1
        self.y = -1

    # 雷电模拟器绑定
    def leidianbang(self, data, mingzi=""):
        hwnd = win32gui.FindWindow("LDPlayerMainFrame", data)
        ch_hwnd = win32gui.FindWindowEx(hwnd, 0, "RenderWindow", "TheRender")
        self.hwnd = ch_hwnd
        print('句柄为：' + str(ch_hwnd))
        leidianbang_temp = self.lw.BindWindow(ch_hwnd, 5, 4, 4, 1, 0)
        if leidianbang_temp == 1:
            print(mingzi + "绑定成功")
        else:
            print(mingzi + "绑定失败")

    # 雷电模拟器解绑
    def jiebang(self):
        self.lw.ForceUnBindWindow(self.hwnd)

    # 鼠标后台点击
    def click(self, click_x, click_y, cast_x: str, cast_y: str):
        cast_x_temp = cast_x.find('|')
        cast_y_temp = cast_y.find('|')
        click_temp = 0
        try:
            if cast_x_temp == -1:
                cast_x_click = random.randint(int(click_x), int(click_x) + int(cast_x))
            else:
                cast_temp = cast_x.split('|')
                cast_x_click = random.randint(int(click_x) + int(cast_temp[0]), int(click_x) + int(cast_temp[1]))
        except:
            cast_x_click = 0
        try:
            if cast_y_temp == -1:
                cast_y_click = random.randint(int(click_y), int(click_y) + int(cast_y))
            else:
                cast_temp = cast_y.split('|')
                cast_y_click = random.randint(int(click_y) + int(cast_temp[0]), int(click_y) + int(cast_temp[1]))
        except:
            cast_y_click = 0
        if cast_x_click > 0 and cast_y_click > 0:
            self.lw.MoveTo(cast_x_click, cast_y_click)
            click_temp = self.lw.LeftClick()
        if click_temp > 0:
            return 1
        else:
            return 0

    '------------------------------------------------------------------------------------------------------------------'
    '找字'

    # 字库设置
    def setdict(self, data):
        for x in range(len(data)):
            self.lw.SetDict(x, data[x])

    # 选择字库
    def usedict(self, data: int):
        if self.word_path_num != data:
            self.word_path_num = data
            self.lw.UseDict(data)

    # 普通找字
    def find_word(self, coord: list, name, col, sim, back, time_out):
        time_process = 0
        while True:
            time_start = time.time()
            temp = self.lw.FindStr(coord[0], coord[1], coord[2], coord[3],
                                   name, col, sim, back)
            if temp == 1:
                self.x = self.lw.x
                self.y = self.lw.y
                return 1
            else:
                time_end = time.time()
                time_process = time_process + time_end - time_start
                if time_process > time_out or time_process == time_out:
                    self.x = -1
                    self.y = -1
                    return 0

    # 高级找字
    def find_wordex(self, coord: list, name, col, sim, back, time_out):
        time_process = 0
        while True:
            time_start = time.time()
            temp = self.lw.FindStrEx(coord[0], coord[1], coord[2], coord[3],
                                     name, col, sim, back)
            if len(temp) == 0:
                time_end = time.time()
                time_process = time_process + time_end - time_start
                if time_process > time_out or time_process == time_out:
                    self.x = -1
                    self.y = -1
                    return ""
            else:
                self.x = -1
                self.y = -1
                return temp

    '------------------------------------------------------------------------------------------------------------------'
    '找图'

    # 普通找图
    def find_pic(self, col_cast, coord: list, data, sim, time_out, click, x_cast, y_cast, delay_time):
        temp = self.lw.findpic(coord[0],
                               coord[1],
                               coord[2],
                               coord[3],
                               data,
                               col_cast, sim, 0, time_out, click, x_cast, y_cast,
                               delay_time)
        if temp == 1:
            self.x = self.lw.x
            self.y = self.lw.y
            return 1
        else:
            self.x = -1
            self.y = -1
            return 0

    # 高级找图
    def find_picex(self, col_cast, coord: list, data, sim, time_out, click, x_cast, y_cast, delay_time):
        temp = self.lw.findpic(coord[0],
                               coord[1],
                               coord[2],
                               coord[3],
                               data,
                               col_cast, sim, 0, time_out, click, x_cast, y_cast,
                               delay_time)
        if len(temp) == 0:
            self.x = -1
            self.y = -1
            return ""
        else:
            self.x = -1
            self.y = -1
            return temp

    '------------------------------------------------------------------------------------------------------------------'
    '找色'

    # 普通找色
    def find_col(self, coord: list, col, sim, dire, time_out):
        temp = self.lw.FindColor(coord[0], coord[1], coord[2], coord[3],
                                 col,
                                 sim,
                                 dire,
                                 time_out)
        return temp


class worker:
    def __init__(self, pic_path, pic_format, pic_col):
        self.skill = lw_obj()
        self.data = {"coord": [],
                     "word_name": '',
                     "pic_data": "",
                     "find_col": "",
                     "cast_col": "000000",
                     "sim": 1,
                     "time_out": 0,
                     "pic_click": 0,
                     "x_cast": 0,
                     "y_cast": 0,
                     "delay_time": 0,
                     "pic_path": pic_path,
                     "pic_format": pic_format,
                     "pic_col": pic_col,
                     "word_data_sum": 0,
                     "word_back": 0}
        #  状态变量
        self.state = 0
        self.x = -1
        self.y = -1
        self.ret_data = []
        self.ex_ret_data = {}

    # 输入数据处理
    def data_handle_input(self, data: dict):
        for x in self.data.keys():
            if x == "pic_path" or x == "pic_format" or x == "pic_col":
                continue
            try:
                if x == "pic_data":
                    if data["pic_path"] != "" and data["pic_format"] != "":
                        self.data[str(x)] = str(data["pic_path"]) + str(data[str(x)]) + str(data["pic_format"])
                    elif data["pic_path"] != "":
                        self.data[str(x)] = str(data["pic_path"]) + str(data[str(x)]) + str(self.data["pic_format"])
                    elif data["pic_format"] != "":
                        self.data[str(x)] = str(self.data["pic_path"]) + str(data[str(x)]) + str(data["pic_format"])
                    else:
                        self.data[str(x)] = str(self.data["pic_path"]) + str(data[str(x)]) + str(
                            self.data["pic_format"])
                else:
                    self.data[str(x)] = data[str(x)]
            except:
                if str(x) == "coord":
                    self.data[str(x)] = []
                elif str(x) == "word_name":
                    self.data[str(x)] = ""
                elif str(x) == "pic_data":
                    self.data[str(x)] = ""
                elif str(x) == "find_col":
                    self.data[str(x)] = ""
                elif str(x) == "sim":
                    self.data[str(x)] = 1
                elif str(x) == "time_out":
                    self.data[str(x)] = 0
                elif str(x) == "pic_click":
                    self.data[str(x)] = 0
                elif str(x) == "x_cast":
                    self.data[str(x)] = 0
                elif str(x) == "y_cast":
                    self.data[str(x)] = 0
                elif str(x) == "delay_time":
                    self.data[str(x)] = 0
                elif str(x) == "word_data_sum":
                    self.data[str(x)] = 0
                elif str(x) == "cast_col":
                    self.data[str(x)] = "000000"

    # 输出数据处理
    def data_handle_output(self, data):
        if not isinstance(data, str):
            self.ret_data = []
            self.ex_ret_data = {}
        else:
            if len(data) == 0:
                self.ret_data = []
                self.ex_ret_data = {}
            else:
                if data.find("|") == -1:
                    temp = data.split(",")
                    self.ret_data.append(str(temp[1]) + "," + str(temp[2]))
                    self.ex_ret_data[str(temp[0])] = [str(temp[1]) + "," + str(temp[2])]
                else:
                    temp = data.split("|")
                    temp_sum = 0
                    for x in range(len(temp)):
                        temp_temp = temp[x].split(",")
                        if int(temp_temp[0]) != temp_sum:
                            temp_sum = int(temp_temp[0])
                            self.ret_data.append(str(temp_temp[1]) + "," + str(temp_temp[2]))
                            self.ex_ret_data[str(temp_temp[0])] = [str(temp_temp[1]) + "," + str(temp_temp[2])]
                        else:
                            self.ret_data.append(str(temp_temp[1]) + "," + str(temp_temp[2]))
                            self.ex_ret_data[str(temp_temp[0])].append(str(temp_temp[1]) + "," + str(temp_temp[2]))

    '''=============================================================================================================='''
    """找字功能"""

    # 字库绑定
    def setdict(self, data: list):
        self.skill.setdict(data)

    # 普通找字
    def find_word(self, data: dict):
        self.data_handle_input(data)
        self.skill.usedict(self.data["word_data_sum"])
        try:
            temp = self.skill.find_word(self.data["coord"], self.data["word_name"], self.data["cast_col"],
                                        self.data["sim"], self.data["word_back"], self.data["time_out"])
        except:
            temp = 0
            print("")
            print("===================================================================================================")
            print(self.data["word_data_sum"])
            print(self.data["coord"])
            print(self.data["word_name"])
            print(self.data["cast_col"])
            print(self.data["sim"])
            print(self.data["word_back"])
            print(self.data["time_out"])
            print("===================================================================================================")
            print("")
        if temp == 0:
            self.x = -1
            self.y = -1
            return 0
        else:
            self.x = self.skill.x
            self.y = self.skill.y
            return 1

    # 高级找字
    def find_wordex(self, data: dict):
        self.data_handle_input(data)
        self.skill.usedict(self.data["word_data_sum"])
        try:
            temp = self.skill.find_wordex(self.data["coord"], self.data["word_name"], self.data["cast_col"],
                                          self.data["sim"], self.data["word_back"], self.data["time_out"])
        except:
            temp = ""
            print("")
            print("===================================================================================================")
            print(self.data["word_data_sum"])
            print(self.data["coord"])
            print(self.data["word_name"])
            print(self.data["cast_col"])
            print(self.data["sim"])
            print(self.data["word_back"])
            print(self.data["time_out"])
            print("===================================================================================================")
            print("")
        self.data_handle_output(temp)
        if len(self.ret_data) == 0:
            return 0
        else:
            return 1

    '''=============================================================================================================='''
    """找图功能"""

    # 普通找图
    def find_pic(self, data: dict):
        self.data_handle_input(data)
        try:
            temp = self.skill.find_pic(self.data["pic_col"], self.data["coord"], self.data["pic_data"],
                                       self.data["sim"],
                                       self.data["time_out"], self.data["pic_click"], self.data["x_cast"],
                                       self.data["y_cast"], self.data["delay_time"])
        except:
            temp = 0
            print("")
            print("===================================================================================================")
            print(self.data["pic_col"])
            print(self.data["coord"])
            print(self.data["pic_data"])
            print(self.data["sim"])
            print(self.data["time_out"])
            print(self.data["pic_click"])
            print(self.data["x_cast"])
            print(self.data["y_cast"])
            print(self.data["delay_time"])
            print("===================================================================================================")
            print("")
        if temp == 1:
            self.x = self.skill.x
            self.y = self.skill.y
            return 1
        else:
            self.x = -1
            self.y = -1
            return 0

    # 高级找图
    def find_picex(self, data: dict):
        self.data_handle_input(data)
        try:
            temp = self.skill.find_picex(self.data["pic_col"], self.data["coord"], self.data["pic_data"],
                                         self.data["sim"],
                                         self.data["time_out"], self.data["pic_click"], self.data["x_cast"],
                                         self.data["y_cast"], self.data["delay_time"])
        except:
            temp = ""
            print("")
            print("===================================================================================================")
            print(self.data["pic_col"])
            print(self.data["coord"])
            print(self.data["pic_data"])
            print(self.data["sim"])
            print(self.data["time_out"])
            print(self.data["pic_click"])
            print(self.data["x_cast"])
            print(self.data["y_cast"])
            print(self.data["delay_time"])
            print("===================================================================================================")
            print("")
        self.data_handle_output(temp)
        if len(self.ret_data) == 0:
            return 0
        else:
            return 1
