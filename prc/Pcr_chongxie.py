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

    def zhangjie_nandu(self, data):  # 主线难度选择
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

    def zhuxiangkxz(self, data: str):  # 主线章节关卡选择
        if self.pcr_find_word(PcrData.zhuxian, "") == 1:
            print("")
            print("主线关卡开始选择")
            temp1 = data.split("-")
            self.zhangjie_nandu(int(temp1[0]))
            sleep(3)
            self.zhangjie_sum_xz(int(temp1[1]))
            sleep(1)
            self.guanqia_xuanze(int(temp1[0]), int(temp1[1]), int(temp1[2]))
            print("")
            print("主线关卡结束选择")

    '''=============================================================================================================='''
    '''扫荡功能'''

    def saodang_sum_qr(self, data, xc_sum):  # 扫荡次数确认
        temp1 = self.pcr_find_pic(self.pic_config, PcrData.sdjmqr, xc_sum)
        if temp1 == 1:
            temp2 = self.pcr_find_word_sum1(PcrData.sd_sum, 0)
            if temp2 < data:
                for x in range(data - temp2):
                    self.pcr_dianji(PcrData.sdsumzj, 0.5, 1, xc_sum)
            elif temp2 > data:
                for x in range(temp2 - data):
                    self.pcr_dianji(PcrData.sdsumjs, 0.5, 1, xc_sum)
            return 1
        return 0

    def saodangtc(self):  # 扫荡弹窗确认
        temp1 = [[self.pcr_find_pic, (tuple(self.pic_config), tuple(PcrData.sdtg), 1)],
                 [self.pcr_find_pic, (tuple(self.pic_config), tuple(PcrData.sdok), 2)],
                 [self.pcr_find_pic, (tuple(self.pic_config), tuple(PcrData.tssdjs), 3)]]
        temp1_temp = self.pcr.duoxianc(temp1)
        temp2 = [[self.pcr_find_pic_click, (tuple(self.pic_config)), tuple(PcrData.xdsd), tuple(PcrData.xdsdqx), 1],
                 [self.pcr_find_pic_click, (tuple(self.pic_config)), tuple(PcrData.tdztc), tuple(PcrData.tdzqx), 2],
                 [self.pcr_find_pic_click, (tuple(self.pic_config)), tuple(PcrData.djtstc), tuple(PcrData.djtsqr), 3]]
        temp2_temp = self.pcr.duoxianc(temp2)
        if temp1_temp[2] == 1:
            return 1
        else:
            return 0

    def saodangjs(self, data):  # 扫荡结束
        if data == 0:
            temp1 = 0
            while temp1 == 0:
                temp1 = self.pcr_find_pic(self.pic_config, PcrData.sdjmqr, "")
                sleep(0.1)
                if temp1 == 1:
                    self.pcr_find_pic(self.pic_config, PcrData.sdqx, "")

    def xiandingsdcs(self):  # 限定扫荡次数查询
        temp1 = [[self.pcr_find_word, (tuple(PcrData.knsd0), 1)],
                 [self.pcr_find_word, (tuple(PcrData.knsd1), 2)],
                 [self.pcr_find_word, (tuple(PcrData.knsd2), 3)],
                 [self.pcr_find_word, (tuple(PcrData.knsd3), 4)],
                 [self.pcr_find_word, (tuple(PcrData.knsd4), 5)],
                 [self.pcr_find_word, (tuple(PcrData.knsd5), 6)]]
        temp1_temp = self.pcr.duoxianc(temp1)
        for x in range(len(temp1_temp)):
            if temp1_temp[x] == 1:
                return x
        return -1

    def saodangcz(self):  # 扫荡重置
        self.pcr_find_pic(self.pic_config, PcrData.sdcz1, "")
        if self.pcr_find_pic_click(self.pic_config, PcrData.sdcz2, PcrData.sdcz3, "") == 1:
            self.pcr_dianji(PcrData.sdcz4, 2, 4, "")
            self.pcr_dianji(PcrData.sdcz5, 2, 4, "")
            return self.xiandingsdcs()
        else:
            return 0

    '''--------------------------------------------------------------------------------------------------------------'''