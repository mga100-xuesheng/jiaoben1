from jichu.gndy import GongNengdy
from zh_data import PcrData
from time import sleep


class PcR:
    def __init__(self, xm_data, pic_config, xc_sum_data):
        self.pcr = GongNengdy(xm_data, pic_config, xc_sum_data)
        self.pic_config = pic_config

    def ldbangding(self, data):  # 雷电绑定
        self.pcr.ldbangding(data)

    def ldjiebang(self):  # 雷电解绑
        self.pcr.ldjiebang()

    def zikusz(self, path: list):  # 字库绑定
        self.pcr.zikubd(path)

    def dqziku(self, data: int):  # 当前字库选择
        self.pcr.dqziku(data)

    '''--------------------------------------------------------------------------------------------------------------'''

    def jiemiandqgc(self):  # Pcr界面转页读取过程
        for x in range(1000):
            temp1 = [[self.pcr.find_word, (tuple(PcrData.dqgc1), 1)],
                     [self.pcr.find_word, (tuple(PcrData.dqgc2), 2)]]
            temp2 = self.pcr.duoxianc(temp1)
            if temp2[0] == 0 and temp2[1] == 0:
                return 1
            sleep(2)

    '''--------------------------------------------------------------------------------------------------------------'''

    def pcr_find_pic(self, config, data, xc_sum):  # Pcr找图
        self.jiemiandqgc()
        return self.pcr.find_pic(config, data, xc_sum)

    def pcr_find_pic_click(self, config, data, click, xc_sum):  # Pcr找图成功点击
        self.jiemiandqgc()
        return self.pcr.find_pic_click(config, data, click, xc_sum)

    def pcr_find_pic_click1(self, config, data, click, xc_sum):  # Pcr找图失败点击
        self.jiemiandqgc()
        return self.pcr.find_pic_click1(config, data, click, xc_sum)

    '''--------------------------------------------------------------------------------------------------------------'''

    def pcr_find_word(self, data, xc_sum):  # Pcr找字
        self.jiemiandqgc()
        return self.pcr.find_word(data, xc_sum)

    def pcr_find_word_click(self, data, click, xc_sum):  # Pcr找字成功点击
        self.jiemiandqgc()
        return self.pcr.find_word_click(data, click, xc_sum)

    def pcr_find_word_click1(self, data, click, xc_sum):  # Pcr找字失败点击
        self.jiemiandqgc()
        return self.pcr.find_word_click1(data, click, xc_sum)

    def pcr_dianji(self, data, min_time, max_time, xc_sum):  # Pcr点击
        self.jiemiandqgc()
        self.pcr.dianji(data, min_time, max_time, xc_sum)

    def tili_sum(self):  # 体力数查询
        self.jiemiandqgc()
        return self.pcr.find_word_sumzh1(PcrData.sd_sum, 0)

    def pcr_find_word_sum1(self, data, fangxiang):  # pcr文字找数
        self.jiemiandqgc()
        return self.pcr.find_word_sumzh1(data, fangxiang)

    '''=============================================================================================================='''
    '''主线关卡选择'''
    def zhangjie_sum(self):  # 查询主线章节数
        return self.pcr_find_word_sum1(PcrData.gklist, 0)

    '''--------------------------------------------------------------------------------------------------------------'''

    def zhangjie_sum_xz(self, data):  # 选择主线章节
        temp1 = self.zhangjie_sum()
        if temp1 == -1:
            return -1
        print("")
        print("当前关卡为：" + str(temp1))
        print("选择关卡为：" + str(data))
        print("")
        if data < temp1:
            temp2 = temp1 - data
            for x in range(temp2):
                self.pcr_dianji(PcrData.gk_zuo, 1.5, 2, "")
        else:
            temp2 = data - temp1
            for x in range(temp2):
                self.pcr_dianji(PcrData.gk_you, 1.5, 2, "")

    def zhangjie_nandu(self,data):  # 主线难度选择
        if data == 1:
            temp1 = self.pcr_find_word_click1(PcrData.gk_normal, PcrData.gk_normal_dj, "")
            print("选择简单模式")
        elif data == 2:
            temp1 = self.pcr_find_word_click1(PcrData.gk_hard, PcrData.gk_hard_dj, "")
            print("选择困难模式")

    def guanqia_xuanze(self, nandu_data, zhangjie, guanka):  # 关卡选择
        if nandu_data == 1:
            return 0
        elif nandu_data == 2:
            self.pcr_dianji(PcrData.hguanka[int(zhangjie) - 1][int(guanka) - 1], 3, 4, "")

    '''--------------------------------------------------------------------------------------------------------------'''

    def zhuxiangkxz(self,data:str):  # 主线章节关卡选择
        if self.pcr_find_word(PcrData.zhuxian, "") == 1:
            print("")
            print("主线关卡开始选择")
            temp1 = data.split("-")
            self.zhangjie_nandu(int(temp1[0]))
            sleep(3)
            self.zhangjie_sum_xz(int(temp1[1]))
            sleep(1)
            self.guanqia_xuanze(int(temp1[0]),int(temp1[1]),int(temp1[2]))
            print("")
            print("主线关卡结束选择")