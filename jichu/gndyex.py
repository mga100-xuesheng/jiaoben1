from jichu.gnzh import *
from jichu.jichugn import *
from time import sleep


class LwGnDy:
    def __init__(self, pic_config):
        self.pic_config = pic_config
        self.lw = FindCol(self.pic_config)
        self.state = False
        self.dqzk = -1

    def ld_lwbd(self, data, name):  # 雷电默认绑定
        self.lw.leidianbang(data, name)

    def ld_jiebang(self):  # 雷电默认解绑
        self.lw.jiebang()

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
        if pic_config is None:
            pic_config = self.pic_config
        self.lw.find_pic_data_shezhi(pic_config, data)
        temp1 = self.lw.find_pic_ex()
        return temp1

    def find_pic_click(self, data, click, config=None):  # 找图成功点击
        if config is None:
            config = self.pic_config
        temp1 = self.lw_findpic(data, pic_config=config)
        if temp1 == 1:
            self.lw_dianji(click, 1, 2)
            return 1
        else:
            return 0

    def find_pic_click1(self, data, click, config=None):  # 找图失败点击
        if config is None:
            config = self.pic_config
        temp1 = self.lw_findpic(data, pic_config=config)
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

    '''---------------------------------------------------------------------------------------------------'''

    def find_word_sum(self, data, find_sum, dizhi, sim: int):  # 文字数字查找
        temp1 = []
        for x in range(len(data)):
            data[x][0] = dizhi
            data[x][3] = sim
            temp2 = self.lw_findwordex1_shujucl2(data[x])
            if temp2[0] == 1:
                for x in range(len(temp2[1])):
                    temp2[1][x] = temp2[1][x].split(",")
                    temp2[1][x].append(find_sum)
                    temp1.append(temp2[1][x])
        if len(temp1) == 0:
            return [[-1]]
        else:
            return temp1

    def find_word_sum1(self, data, find_sum):  # 文字数字查找1
        temp1 = []
        for x in range(len(data)):
            temp2 = self.lw_findwordex1_shujucl2(data[x])
            if temp2[0] == 1:
                for x in range(len(temp2[1])):
                    temp2[1][x] = temp2[1][x].split(",")
                    temp2[1][x].append(find_sum)
                    temp1.append(temp2[1][x])
        if len(temp1) == 0:
            return [[-1]]
        else:
            return temp1


class LwGndyExObj:
    def __init__(self, name: str, win_name, pic_config, limit=False, limit_num=0, add_sum=10):
        self.lw_obj = {}
        self.name = name
        self.win_name = win_name
        self.obj_sum = 0
        self.limit = limit
        self.limit_num = limit_num
        self.add_sum = add_sum
        self.pic_config = pic_config
        self.lock = threading.Lock()
        self.obj_find(3, num=add_sum)

    def add_obj(self, num):
        for x in range(num):
            temp1 = self.name + str(self.obj_sum + 1)
            self.lw_obj[temp1] = LwGnDy(self.pic_config)
            self.obj_sum = self.obj_sum + 1
            self.lw_obj[temp1].ld_lwbd(self.win_name, self.name)

    def obj_find(self, data: int, name=None, num=None):
        state = 0
        self.lock.acquire()
        while True:
            for z in range(5):
                if data == 1:
                    for x in range(self.obj_sum):
                        if self.lw_obj[self.name + str(x + 1)].state is False:
                            self.lw_obj[self.name + str(x + 1)].state = True
                            self.lock.release()
                            return self.name + str(x + 1)
                elif data == 2:
                    self.lw_obj[name].state = False
                    self.lock.release()
                    return 1
                elif data == 3:
                    self.add_obj(num)
                    if state == 1:
                        data = 1
                        state = 0
                        continue
                    self.lock.release()
                    return 1
                sleep(0.1)
            self.lock.release()
            while True:
                for x in range(self.obj_sum):
                    if self.lw_obj[self.name + str(x + 1)].state is False:
                        break
                sleep(0.1)
                if self.limit is True and self.obj_sum > self.add_sum + self.limit_num:
                    data = 3
                    num = 1
                    state = 1
                    break

    def obj_dis(self):
        return self.obj_find(1)

    def obj_rec(self, name: str):
        return self.obj_find(2, name=name)

    def obj_add(self, num):
        return self.obj_find(3, num=num)

    def obj_stop(self):
        for x in range(self.obj_sum):
            self.lw_obj[self.name + str(x + 1)].ld_jiebang()

    def obj_word_path(self, data: list):
        for x in range(self.obj_sum):
            self.lw_obj[self.name + str(x + 1)].lw_zikubd(data)
