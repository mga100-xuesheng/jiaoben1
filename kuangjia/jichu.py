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
        self.x = 0
        self.y = 0

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
            if cast_x_temp != -1:
                cast_x_click = random.randint(int(click_x), int(click_x) + int(cast_x))
            else:
                cast_temp = cast_x.split('|')
                cast_x_click = random.randint(int(click_x) + int(cast_temp[0]), int(click_x) + int(cast_temp[1]))
        except:
            cast_x_click = 0
        try:
            if cast_y_temp != -1:
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
            return ""
        else:
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
