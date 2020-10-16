from jichu.gnzh import FindCol


class GongNengdy:
    def __init__(self, xm_data, pic_comfig, xc_sum_data):
        self.sum_names = locals()
        self.xm_data = xm_data
        self.xc_sum_data = xm_data
        self.dqzk = -1
        for x in range(xc_sum_data):
            self.sum_names[self.xm_data + str(x)] = FindCol(pic_comfig)

    def ldbangding(self, data):  # 雷电模拟器多线程绑定
        for x in range(self.xc_sum_data):
            self.sum_names[self.xm_data + str(x)].leidianbang(data, self.xm_data)

    def ldjiebang(self):  # 雷电模拟器解绑
        self.sum_names[self.xm_data + str(1)].jiebang()

    def shujucl1(self, data, xc_sum):  # 数据处理1  格式为：[[第一个数据],[第二个数据]]
        if xc_sum == "":
            xc_sum = 1
        return self.sum_names[self.xm_data + str(xc_sum)].shujuchuli11(data)

    def shujucl2(self, data, xc_sum):  # 数据处理2 格式为：[第一个数据,第二个数据]
        return self.sum_names[self.xm_data + str(xc_sum)].shujuchuli12(data)

    def dianji(self,data,min_time,max_time,xc_sum):  # 鼠标点击
        if xc_sum == "":
            xc_sum = 1
        self.sum_names[self.xm_data + str(xc_sum)].random_time(min_time,max_time)
        return self.sum_names[self.xm_data + str(xc_sum)].click(data)

    '''==================================================================================================='''

    def find_pic(self,config,data,xc_sum):  # 找图
        if xc_sum == "":
            xc_sum = 1
        self.sum_names[self.xm_data + str(xc_sum)].find_pic_data_shezhi(config,data)
        return self.sum_names[self.xm_data + str(xc_sum)].find_pic()

    def find_pic_ex(self,config,data,xc_sum):  # 找图扩展
        if xc_sum == "":
            xc_sum = 1
        self.sum_names[self.xm_data + str(xc_sum)].find_pic_data_shezhi(config,data)
        return self.sum_names[self.xm_data + str(xc_sum)].find_pic_ex()

    def find_pic_click(self,config,data,click,xc_sum):  # 找图成功点击
        temp1 = self.find_pic(config,data,xc_sum)
        if temp1 == 1:
            self.dianji(click,1,2,xc_sum)
            return 1
        else:
            return 0

    def find_pic_click1(self,config,data,click,xc_sum):  # 找图失败点击
        temp1 = self.find_pic(config,data,xc_sum)
        if temp1 == 1:
            return 0
        else:
            self.dianji(click,1,2,xc_sum)
            return 1

    '''==================================================================================================='''

    def zikubd(self,data):  # 字库绑定
        for x in range(self.xc_sum_data):
            self.sum_names[self.xm_data + str(x)].SetDict(x,data[x])

    def dqziku(self,data):  # 当前字库选择
        if self.dqzk != data:
            for x in range(self.xc_sum_data):
                self.sum_names[self.xm_data + str(x)].UseDict(data)
            self.dqzk = data
            return 2
        else:
            return 1

    def find_word(self,data,xc_sum):  # 找字
        self.sum_names[self.xm_data + str(xc_sum)].find_data_shezhi(data)
        return self.sum_names[self.xm_data + str(xc_sum)].find_word()

    def find_word_click(self,data,click,xc_sum):  # 找字成功点击
        temp1 = self.find_word(data,xc_sum)
        if temp1 == 1:
            self.dianji(click, 1, 2, xc_sum)
            return 1
        else:
            return 0

    def find_word_click1(self,data,click,xc_sum):  # 找字失败点击
        temp1 = self.find_word(data,xc_sum)
        if temp1 == 1:
            return 0
        else:
            self.dianji(click, 1, 2, xc_sum)
            return 1

    def find_word_ex(self,data,xc_sum):  # 找字扩展
        self.sum_names[self.xm_data + str(xc_sum)].find_data_shezhi(data)
        return self.sum_names[self.xm_data + str(xc_sum)].find_word_ex()

    def find_word_ex1(self,data,xc_sum):  # 找字扩展1
        self.sum_names[self.xm_data + str(xc_sum)].find_data_shezhi(data)
        return self.sum_names[self.xm_data + str(xc_sum)].find_word_ex()

    def find_word_ex1_shujucl2(self,data,xc_sum):  # 找字扩展1:数据处理2
        self.sum_names[self.xm_data + str(xc_sum)].find_data_shezhi(data)
        temp1 = self.find_word_ex1(data,xc_sum)
        if temp1[0] == 1:
            temp2 = self.sum_names[self.xm_data + str(xc_sum)].shujuchuli2(temp1[1])
            return temp2
        else:
            return [0]
    '''---------------------------------------------------------------------------------------------------'''
    def find_word_sum(self, data, find_sum, dizhi, sim: int, xc_sum):
    '''==================================================================================================='''



