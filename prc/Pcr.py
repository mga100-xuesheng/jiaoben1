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

    def zikusz(self, path: list):  # 绑定字库
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

    def tili_sum(self,xc_sum):  # 体力数查询
        return self.pcr.find_word_sum1(PcrData.sd_sum, 0, xc_sum)

    '''==================================================================================================='''

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
            return 1
        return 0

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
            return self.xiandingsccs()
        else:
            return 0

    '''------------------------------------------------------------------------------------------------------'''

    def putongsd(self,data):  # 普通扫荡
        if self.tili_sum("") <= 40:
            self.saodangjs(0)
            return -1
        temp1 = self.saodangcsqr(data)
        if temp1 == 1:
            self.saodangks()
            time.sleep(0.5)
            temp1 = self.saodangtc()
            self.saodangjs(temp1)

    def wuquxiaosd(self,data):  # 无取消扫荡
        if self.tili_sum("") <= 40:
            self.saodangjs(0)
            return -1
        temp1 = self.saodangcsqr(data)
        if temp1 == 1:
            self.saodangks()
            time.sleep(0.5)
            temp1 = self.saodangtc()

    def wuquxiaowutilisd(self,data):  # 无取消无体力扫荡
        temp1 = self.saodangcsqr(data)
        if temp1 == 1:
            self.saodangks()
            time.sleep(0.5)
            temp1 = self.saodangtc()

    def xiandingcssd(self,data):  # 限定次数扫荡
        temp1 = self.xiandingsccs()
        if self.tili_sum("") <= 40:
            self.saodangjs(0)
            return -1
        if temp1 == 0 and data == 1:
            sdcs = self.saodangcz()
            if sdcs == 0:
                self.saodangjs(0)
                return -1
            else:
                self.putongsd(sdcs)
        elif temp1 != 0 and data == 1:
            self.wuquxiaosd(temp1)
            temp1 = self.saodangcz()
            if temp1 != 0:
                self.putongsd(temp1)
            else:
                return -1
        elif temp1 != 0 and data == 0:
            self.putongsd(temp1)
            return 1
        elif temp1 == 0 and data == 0:
            self.saodangjs(0)
            return 2

    def tansuosd(self):
        temp1 = self.xiandingsccs()
        if temp1 == 0:
            self.saodangjs(0)
            return 2
        else:
            self.wuquxiaowutilisd(temp1)

    '''==================================================================================================='''

    def dxc_sum(self):
        dxc_sum_temp1 = self.pcr.find_word_sum1(PcrData.worddxc,0,"")
        if dxc_sum_temp1 != -1:
            print("当前层数为："+str(dxc_sum_temp1))
            return dxc_sum_temp1
        else:
            print("没有找到层数")
            return -1

    def dxc_sum_csxz(self,data):
        temp1 = self.dxc_sum()
        if temp1 != -1:
            self.pcr_find_pic(self.pcr_find_pic_config,data[temp1-1],"")
            return 1
        else:
            print("箱子没有找到")
            return -1

    def dxc_zdks(self):
        return self.pcr_find_pic(self.pcr_find_pic_config,PcrData.dxctz,"")
