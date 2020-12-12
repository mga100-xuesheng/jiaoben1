from jichu.gnzh import *
from jichu.jichugn import *
from datetime import datetime
from time import sleep


class LwGnDy:
    def __init__(self, pic_config):
        self.pic_config = pic_config
        self.lw = FindCol(self.pic_config)
        self.state = False
        self.dqzk = -1

    def lw_dianji(self, data, min_time, max_time):  # 鼠标点击
        self.lw.random_time(min_time, max_time)
        temp1 = self.lw.click(data)
        return temp1

    def lw_findpic(self, data, pic_config=None):  # 找图
        if pic_config is None:
            pic_config = self.pic_config
        self.lw.find_pic_data_shezhi(pic_config, data)
        temp1 = self.lw.find_pic()
        return temp1

    def lw_findpicex(self, data, pic_config=None):  # 找图扩展
        self.lw.find_pic_data_shezhi(pic_config, data)
        temp1 = self.lw.find_pic_ex()
        return temp1

    def find_pic_click(self, config, data, click):  # 找图成功点击
        temp1 = self.lw_findpic(config, data)
        if temp1 == 1:
            self.lw_dianji(click, 1, 2)
            return 1
        else:
            return 0

    def find_pic_click1(self, config, data, click):  # 找图失败点击
        temp1 = self.lw_findpic(config, data)
        if temp1 == 1:
            return 0
        else:
            self.lw_dianji(click, 1, 2)
            return 1

    '''==================================================================================================='''

    def lw_zikubd(self, data):  # 字库绑定
        for y in range(len(data)):
            self.lw.lw.SetDict(y, data[y])

    def lw_dqziku(self, data):  # 当前字库选择
        if self.dqzk != data:
            self.lw.lw.UseDict(data)
            self.dqzk = data
            return 2
        else:
            return 1

    def le_findword(self, data: list, dqzk=0):  # 找字
        self.lw_dqziku(dqzk)
        self.lw.find_data_shezhi(data)
        temp1 = self.lw.find_word()
        return temp1

    def lw_findword_click(self, data, click, dqzk=0):  # 找字成功点击
        temp1 = self.le_findword(data, dqzk=dqzk)
        if temp1 == 1:
            self.lw_dianji(click, 1, 2)
            return 1
        else:
            return 0

    def lw_findword_click1(self, data, click, dqzk=0):  # 找字失败点击
        temp1 = self.le_findword(data, dqzk=dqzk)
        if temp1 == 1:
            return 0
        else:
            self.lw_dianji(click, 1, 2)
            return 1

    def lw_findwordex(self, data, dqzk=0):  # 找字扩展
        self.lw_dqziku(dqzk)
        self.lw.find_data_shezhi(data)
        temp1 = self.lw.find_word_ex()
        return temp1

    def lw_findwordex1(self, data, dqzk=0):  # 找字扩展1
        self.lw_dqziku(dqzk)
        self.lw.find_data_shezhi(data)
        temp1 = self.lw.find_word_ex1()
        return temp1

    def lw_findwordex1_shujucl2(self, data, dqzk=0):  # 找字扩展1:数据处理2
        temp1 = self.lw_findwordex1(data, dqzk=dqzk)
        if temp1[0] == 1:
            temp2 = self.lw.shujuchuli2(temp1[1])
            return temp2
        else:
            return [0]
