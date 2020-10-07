import gongneng.gongnengdy
from gongneng.jiben import MyThread
from zh_data import PcrData
import time
import datetime
from random import shuffle


class Pcr:
    def __init__(self, mz_data, xm_data, xc_sum_data, pic_config: list):
        self.pcr = gongneng.gongnengdy.GongNengdy(mz_data, xm_data, xc_sum_data, pic_config)
        self.pcr_find_pic_config = ["", "", ""]

    def zikusz(self, path: list):
        self.pcr.zikubd(path)

    def pcrjiemianduqugn(self, data1, data2):  # Pcr界面转页读取过程功能
        for x in range(1000):
            temp1 = MyThread(self.pcr.find_word, (tuple(data1), 1))
            temp2 = MyThread(self.pcr.find_word, (tuple(data2), 2))
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
        return self.pcr.find_pic(config, data, xc_sum)

    def pcr_find_pic_click(self, config, data, click, xc_sum):  # Pcr找图成功点击
        self.pcrjmdq()
        return self.pcr.find_pic_click(config, data, click, xc_sum)

    def pcr_find_pic_click1(self, config, data, click, xc_sum):  # Pcr找图失败点击
        self.pcrjmdq()
        return self.pcr.find_pic_click1(config, data, click, xc_sum)

    def pcr_find_word(self, data, xc_sum):  # Pcr找字
        self.pcrjmdq()
        return self.pcr.find_word(data, xc_sum)

    def pcr_find_word_click(self, data, click, xc_sum):  # Pcr找字成功点击
        self.pcrjmdq()
        return self.pcr.find_word_click(data, click, xc_sum)

    def pcr_find_word_click1(self, data, click, xc_sum):  # Pcr找字失败点击
        self.pcrjmdq()
        return self.pcr.find_word_click1(data, click, xc_sum)

    def pcr_dianji(self, data, min_time, max_time, xc_sum):  # Pcr点击
        self.pcr.dianji(data, min_time, max_time, xc_sum)

    '''--------------------------------------------------------------------------------------------------'''

    def saodangcsqr(self, data):  # 扫荡次数确认
        temp1 = self.pcr_find_pic(self.pcr_find_pic_config, PcrData.sdjmqr, "")
        if temp1 == 1:
            temp2 = self.pcr.find_word_sumzh1(PcrData.sd_sum, 0)
            if temp2 < data:
                for x in range(data - temp2):
                    self.pcr_dianji(PcrData.sdsumzj, 0.5, 1, "")
            elif temp2 > data:
                for x in range(temp2 - data):
                    self.pcr_dianji(PcrData.sdsumjs, 0.5, 1, "")

    def saodangtc(self):  # 扫荡弹窗确认
        temp1 = MyThread(self.pcr_find_pic, (tuple(self.pcr_find_pic_config), tuple(PcrData.sdtg), 1))
        temp2 = MyThread(self.pcr_find_pic, (tuple(self.pcr_find_pic_config), tuple(PcrData.sdok), 2))
        temp3 = MyThread(self.pcr_find_pic, (tuple(self.pcr_find_pic_config), tuple(PcrData.tssdjs), 3))
        temp4 = MyThread(self.pcr_find_pic, (tuple(self.pcr_find_pic_config), tuple(PcrData.xdsd), 1))
        temp5 = MyThread(self.pcr_find_pic, (tuple(self.pcr_find_pic_config), tuple(PcrData.tdztc), 2))
        temp6 = MyThread(self.pcr_find_pic, (tuple(self.pcr_find_pic_config), tuple(PcrData.djtstc), 3))
        temp1.start()
        temp2.start()
        temp3.start()
        temp1.join()
        temp2.join()
        temp3.join()
        temp4.start()
        temp5.start()
        temp6.start()
        temp4.join()
        temp5.join()
        temp6.join()
        if temp3.get_result() == 1:
            return 1
        else:
            return 0

    def saodangks(self):  # 扫荡开始
        self.pcr_dianji(PcrData.sdqr, 1.7, 3, "")
        temp1 = self.pcr_find_pic_click(self.pcr_find_pic_config, PcrData.sdqr, PcrData.sdjqrqr, "")
        if temp1 == 1:
            return 1
        else:
            return 0

    def saodangjs(self, data):  # 扫荡结束
        if data == 0:
            temp1 = 0
            while temp1 == 0:
                temp1 = self.pcr_find_pic(self.pcr_find_pic_config, PcrData.sdjmqr, "")
                time.sleep(0.1)
                if temp1 == 1:
                    self.pcr_find_pic(self.pcr_find_pic_config, PcrData.sdqx, "")

    def xiandingsccs(self):  # 限定扫荡次数查询
        temp1 = MyThread(self.pcr_find_word, (tuple(PcrData.knsd0), 1))
        temp2 = MyThread(self.pcr_find_word, (tuple(PcrData.knsd1), 2))
        temp3 = MyThread(self.pcr_find_word, (tuple(PcrData.knsd2), 3))
        temp4 = MyThread(self.pcr_find_word, (tuple(PcrData.knsd3), 4))
        temp1.start()
        temp2.start()
        temp3.start()
        temp4.start()
        temp1.join()
        temp2.join()
        temp3.join()
        temp4.join()
        temp1_sum = [temp1.get_result(),temp2.get_result(),temp3.get_result(),temp4.get_result()]
        for x in range(len(temp1_sum)):
            if temp1_sum[x] == 1:
                return x
        return -1

    def saodangcz(self):  # 扫荡重置
        self.pcr_find_pic(self.pcr_find_pic_config,PcrData.sdcz1,"")
        if self.pcr_find_pic_click(self.pcr_find_pic_config,PcrData.sdcz2,PcrData.sdcz3,"") == 1:
            self.pcr_dianji(PcrData.sdcz4,2,4,"")
            self.pcr_dianji(PcrData.sdcz5,2,4,"")
            return 3
        else:
            return 0
