import gongneng.gongnengdy
from gongneng.jiben import MyThread
from zh_data import PcrData
import time
import datetime
from random import shuffle


class Pcr:
    def __init__(self, mz_data, xm_data, xc_sum_data, pic_comfig: list):
        self.prc = gongneng.gongnengdy.GongNengdy(mz_data, xm_data, xc_sum_data, pic_comfig)

    def zikusz(self, path: list):
        self.prc.zikubd(path)

    def pcrjiemianduqugn(self, data1, data2):  # Pcr界面转页读取过程功能
        for x in range(1000):
            temp1 = MyThread(self.prc.find_word, (tuple(data1), 1))
            temp2 = MyThread(self.prc.find_word, (tuple(data2), 2))
            temp1.start()
            temp2.start()
            temp1.join()
            temp2.join()
            if temp1.get_result() == 0 and temp2.get_result() == 0:
                return 1
            time.sleep(2)

    def pcrjmdq(self):  # Pcr界面转页读取过程
        self.pcrjiemianduqugn(PcrData.dqgc1, PcrData.dqgc2)

    def pcr_find_pic(self, config, data, xc_sum):  # Pcr找图
        self.pcrjmdq()
        return self.prc.find_pic(config, data, xc_sum)

    def pcr_find_pic_click(self, config, data, click, xc_sum):  # Pcr找图成功点击
        self.pcrjmdq()
        return self.prc.find_pic_click(config, data, click, xc_sum)

    def pcr_find_pic_click1(self, config, data, click, xc_sum):  # Pcr找图失败点击
        self.pcrjmdq()
        return self.prc.find_pic_click1(config, data, click, xc_sum)

    def pcr_find_word(self,data,xc_sum):  # Pcr找字
        self.pcrjmdq()
        return self.prc.find_word(data,xc_sum)

    def pcr_find_word_click(self,data,click,xc_sum):  # Pcr找字成功点击
        self.pcrjmdq()
        return self.prc.find_word_click(data,click,xc_sum)

    def pcr_find_word_click1(self,data,click,xc_sum):  # Pcr找字失败点击
        self.pcrjmdq()
        return self.prc.find_word_click1(data,click,xc_sum)

    '''--------------------------------------------------------------------------------------------------'''
