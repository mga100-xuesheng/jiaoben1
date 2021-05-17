import json
import pythoncom
from comtypes import client
import win32gui
import random
import time


class lw_obj:
    def __init__(self, pic_path, pic_format, pic_col):
        self.pic_path = pic_path
        self.pic_format = pic_format
        self.pic_col = pic_col
        pythoncom.CoInitialize()
        self.lw = client.CreateObject('lw.lwsoft3')
        self.hwnd = -1
        self.state = 0
        self.word_path_num = 0

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
