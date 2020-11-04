from jichu.gndy import GongNengdy
from zh_data import PcrData
from time import sleep
from datetime import datetime


class PcR:
    def __init__(self, xm_data, pic_config, chuangkou_name, ziku_path: list):
        self.pcr = GongNengdy(xm_data, pic_config, chuangkou_name, ziku_path)
        self.pic_config = pic_config
        self.pcr_jm_obj()

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
            temp1 = [[self.pcr.find_word, (PcrData.dqgc1,)],
                     [self.pcr.find_word, (PcrData.dqgc2,)]]
            temp2 = self.pcr.duoxianc(temp1)
            # print(temp2)
            if temp2[0] == 0 and temp2[1] == 0:
                return 1
            sleep(2)

    '''--------------------------------------------------------------------------------------------------------------'''

    def pcr_find_pic(self, config, data):  # Pcr找图
        self.jiemiandqgc()
        return self.pcr.find_pic(config, data)

    def pcr_find_pic_click(self, config, data, click):  # Pcr找图成功点击
        self.jiemiandqgc()
        return self.pcr.find_pic_click(config, data, click)

    def pcr_find_pic_click1(self, config, data, click):  # Pcr找图失败点击
        self.jiemiandqgc()
        return self.pcr.find_pic_click1(config, data, click)

    '''--------------------------------------------------------------------------------------------------------------'''

    def pcr_find_word(self, data):  # Pcr找字
        self.jiemiandqgc()
        return self.pcr.find_word(data)

    def pcr_find_word1(self, data):
        return self.pcr.find_word(data)

    def pcr_find_word_click(self, data, click):  # Pcr找字成功点击
        self.jiemiandqgc()
        return self.pcr.find_word_click(data, click)

    def pcr_find_word_click1(self, data, click):  # Pcr找字失败点击
        self.jiemiandqgc()
        return self.pcr.find_word_click1(data, click)

    def pcr_dianji(self, data, min_time, max_time):  # Pcr点击
        self.jiemiandqgc()
        self.pcr.dianji(data, min_time, max_time)

    def tili_sum(self):  # 体力数查询
        self.jiemiandqgc()
        temp1 = self.pcr.find_word_sumzh1(PcrData.tili, 0)
        print('体力为：' + str(temp1))
        return temp1

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
                self.pcr_dianji(PcrData.gk_zuo, 1.5, 2)
        else:
            temp2 = data - temp1
            for x in range(temp2):
                self.pcr_dianji(PcrData.gk_you, 1.5, 2)

    def zhangjie_nandu(self, data):  # 主线难度选择
        if data == 1:
            temp1 = self.pcr_find_word_click1(PcrData.gk_normal, PcrData.gk_normal_dj)
            print("选择简单模式")
        elif data == 2:
            temp1 = self.pcr_find_word_click1(PcrData.gk_hard, PcrData.gk_hard_dj)
            print("选择困难模式")

    def guanqia_xuanze(self, nandu_data, zhangjie, guanka):  # 关卡选择
        if nandu_data == 1:
            return 0
        elif nandu_data == 2:
            self.pcr_dianji(PcrData.hguanka[int(zhangjie) - 1][int(guanka) - 1], 3, 4)

    '''--------------------------------------------------------------------------------------------------------------'''

    def zhuxiangkxz(self, data: str):  # 主线章节关卡选择
        if self.pcr_find_word(PcrData.zhuxian) == 1:
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

    def saodang_sum_qr(self, data):  # 扫荡次数确认
        temp1 = self.pcr_find_pic(self.pic_config, PcrData.sdjmqr)
        if temp1 == 1:
            temp2 = self.pcr_find_word_sum1(PcrData.sd_sum, 0)
            if temp2 < data:
                for x in range(data - temp2):
                    self.pcr_dianji(PcrData.sdsumzj, 0.5, 1)
            elif temp2 > data:
                for x in range(temp2 - data):
                    self.pcr_dianji(PcrData.sdsumjs, 0.5, 1)
            return 1
        return 0

    def saodangks(self):  # 扫荡开始
        self.pcr_dianji(PcrData.sdqr, 1.7, 3)
        temp1 = self.pcr_find_pic_click(self.pic_config, PcrData.sdjqr, PcrData.sdjqrqr)
        if temp1 == 1:
            return 1
        else:
            return 0

    def saodangtc(self):  # 扫荡弹窗确认
        temp1 = [[self.pcr_find_pic, (tuple(self.pic_config), tuple(PcrData.sdtg))],
                 [self.pcr_find_pic, (tuple(self.pic_config), tuple(PcrData.sdok))],
                 [self.pcr_find_pic, (tuple(self.pic_config), tuple(PcrData.tssdjs))]]
        temp1_temp = self.pcr.duoxianc(temp1)
        temp2 = [[self.pcr_find_pic_click, (tuple(self.pic_config), tuple(PcrData.xdsd), tuple(PcrData.xdsdqx))],
                 [self.pcr_find_pic_click, (tuple(self.pic_config), tuple(PcrData.tdztc), tuple(PcrData.tdzqx))],
                 [self.pcr_find_pic_click, (tuple(self.pic_config), tuple(PcrData.djtstc), tuple(PcrData.djtsqr))]]
        temp2_temp = self.pcr.duoxianc(temp2)
        if temp1_temp[2] == 1:
            return 1
        else:
            return 0

    def saodangjs(self, data):  # 扫荡结束
        if data == 0:
            temp1 = 0
            while temp1 == 0:
                temp1 = self.pcr_find_pic(self.pic_config, PcrData.sdjmqr)
                sleep(0.1)
                if temp1 == 1:
                    self.pcr_find_pic(self.pic_config, PcrData.sdqx)

    def xiandingsdcs(self):  # 限定扫荡次数查询
        temp1 = [[self.pcr_find_word, (tuple(PcrData.knsd0),)],
                 [self.pcr_find_word, (tuple(PcrData.knsd1),)],
                 [self.pcr_find_word, (tuple(PcrData.knsd2),)],
                 [self.pcr_find_word, (tuple(PcrData.knsd3),)],
                 [self.pcr_find_word, (tuple(PcrData.knsd4),)],
                 [self.pcr_find_word, (tuple(PcrData.knsd5),)]]
        temp1_temp = self.pcr.duoxianc(temp1)
        for x in range(len(temp1_temp)):
            if temp1_temp[x] == 1:
                return x
        return -1

    def saodangcz(self):  # 扫荡重置
        self.pcr_find_pic(self.pic_config, PcrData.sdcz1)
        if self.pcr_find_pic_click(self.pic_config, PcrData.sdcz2, PcrData.sdcz3) == 1:
            self.pcr_dianji(PcrData.sdcz4, 2, 4)
            self.pcr_dianji(PcrData.sdcz5, 2, 4)
            return self.xiandingsdcs()
        else:
            return 0

    '''--------------------------------------------------------------------------------------------------------------'''

    def putongsd(self, data):  # 普通扫荡
        temp1 = self.saodang_sum_qr(data)
        if temp1 == 1:
            temp2 = self.saodangks()
            if temp2 != 1:
                return -2
            else:
                temp3 = self.saodangtc()
                return temp3

    def xiandingsd(self):  # 限定次数扫荡
        temp1 = self.xiandingsdcs()
        if temp1 != 0:
            return self.putongsd(temp1)

    def xiandingsd1(self, data):  # 限定次数扫荡
        temp1 = self.xiandingsdcs()
        if temp1 == 0 and data == 1:
            sdcs = self.saodangcz()
            if sdcs == 0:
                return 2
            else:
                self.putongsd(sdcs)
                return 2
        elif temp1 == 0 and data == 0:
            return 1
        elif temp1 != 0 and data == 1:
            self.putongsd(temp1)
            temp1 = self.saodangcz()
            if temp1 != 0:
                self.putongsd(temp1)
                return 2
            else:
                return 2
        elif temp1 != 0 and data == 0:
            self.putongsd(temp1)
            return 1

    '''--------------------------------------------------------------------------------------------------------------'''

    def tlptsd(self, data):  # 体力检测和点击取消--普通扫荡
        if self.tili_sum() < 40:
            return -1
        self.putongsd(data)
        self.saodangjs(0)

    def tlptsd1(self, data):  # 体力检测和无点击取消--普通扫荡
        if self.tili_sum() < 40:
            return -1
        self.putongsd(data)

    def tlxiandingsd(self, data):  # 体力检测和点击取消——限定次数扫荡
        if self.tili_sum() < 40:
            return -1
        self.xiandingsd1(data)
        self.saodangjs(0)

    def tlxiandingsd1(self, data):  # 体力检测和无点击取消——限定次数扫荡
        if self.tili_sum() < 40:
            return -1
        self.xiandingsd1(data)

    '''--------------------------------------------------------------------------------------------------------------'''

    def tansuosd(self):  # 探索扫荡
        self.saodangjs(self.xiandingsd())

    def zhuxiansd(self, data):  # 主线扫荡
        self.tlptsd(data)

    def kunnansd(self, data):  # 困难扫荡
        self.tlxiandingsd(data)

    '''=============================================================================================================='''
    '''战斗过程'''

    def wodeduiwudk(self):  # 我的队伍打开
        self.pcr_find_pic(self.pic_config, PcrData.dxcwddw)

    def bianduixz(self, data):  # 编队选择
        self.pcr_find_pic(self.pic_config, PcrData.biandui[data - 1])

    def duiwuxz(self, data):  # 队伍选择
        if data < 4:
            self.pcr_find_pic(self.pic_config, PcrData.duiwu[data - 1])

    '''--------------------------------------------------------------------------------------------------------------'''
    '''地下城功能'''

    def dxc_sum(self):  # 查找地下城层数
        temp1 = self.pcr.find_word_sumzh1(PcrData.worddxc, 0)
        if temp1 != -1:
            print("当前层数为：" + str(temp1))
            return temp1
        else:
            print("没有找到层数")
            return -1

    def dxc_sum_xz(self, data):  # 地下城层数选择
        temp1 = self.dxc_sum()
        if temp1 != -1:
            self.pcr_find_pic(self.pic_config, data[temp1 - 1])
            return 1
        else:
            print("箱子没有找到")
            return -1

    def dxc_zhandouks(self):  # 地下城战斗开始
        return self.pcr_find_pic(self.pic_config, PcrData.dxczdks)

    def dxc_zhandougc(self):  # 地下城战斗过程
        for x in range(60):
            print("地下城战斗开始-------------------")
            temp1 = [[self.pcr_find_pic, (tuple(self.pic_config), tuple(PcrData.dxcxyb2))],
                     [self.pcr_find_pic, (tuple(self.pic_config), tuple(PcrData.dxcggsb))]]
            temp2 = self.pcr.duoxianc(temp1)
            if temp2[0] == 1:
                print("查找下一步：成功")
                return 1
            elif temp2[1] == 1:
                print("查找返回地下城：成功")
                return 0
            else:
                print("查找失败")
                return -1
        return -2

    def dxc_zhandoujs(self, data):  # 战斗结束
        if data == 1:
            sleep(5)
            return self.pcr_find_pic(self.pic_config, PcrData.dxcok)

    def dxc_duiwu1(self):  # 地下城队伍选择1
        self.wodeduiwudk()
        sleep(4)
        self.duiwuxz(1)

    def dxc_duiwu2(self):  # 地下城队伍选择2
        self.wodeduiwudk()
        sleep(4)
        self.duiwuxz(2)

    def richangdxc(self, data, dadao_ceng_sum):  # 地下城执行过程
        temp1 = self.dxc_sum()
        if temp1 > dadao_ceng_sum:
            return 2
        if temp1 != -1:
            if self.dxc_sum_xz(temp1) == 1:
                if self.dxc_zhandouks() == 1:
                    if temp1 == 1:
                        self.dxc_duiwu1()
                    self.dxc_zhandouks()
                    sleep(1)
                    temp2 = self.dxc_zhandougc()
                    self.dxc_zhandoujs(temp2)
                    return 1
        return 0

    '''=============================================================================================================='''
    '''日志记录'''

    @staticmethod
    def pcr_rizhixieru(key_word, data):  # 日志写入
        GongNengdy.rizhi_xieru(PcrData.rizhi_path, PcrData.rizhi_name, key_word, data, "05")

    @staticmethod
    def pcr_rizhiduqu(key_word):  # 日志读取
        return GongNengdy.rizhi_duqu(PcrData.rizhi_path, PcrData.rizhi_name, key_word)

    def pcr_rizhi_update(self):  # 日志刷新
        temp1 = datetime.now().strftime('%Y-%m-%d-%H')
        temp2 = self.pcr_rizhiduqu('-')
        if GongNengdy.time_db(temp2, temp1) > 24:
            for x in PcrData.rizhi_keyword:
                self.pcr_rizhixieru(x, "未做")

    @staticmethod
    def rizhi_db(data):  # 日志对比确认
        if data == "已做":
            return 0
        elif data == '未做':
            return 1
        return -1

    def rw_tili(self):  # 任务体力领取确认
        return self.rizhi_db(self.pcr_rizhiduqu('任务领取'))

    def rw_xieru(self):  # 任务体力领取确认写入
        self.pcr_rizhixieru('任务领取', '已做')

    def jy_tili(self):  # 家园体力领取确认
        return self.rizhi_db(self.pcr_rizhiduqu('家园领取'))

    def jy_xieru(self):  # 家园体力领取写入
        self.pcr_rizhixieru('家园领取', '已做')

    def tansuo_qr(self):  # 探索关卡执行确认
        return self.rizhi_db(self.pcr_rizhiduqu('探索'))

    def tansuo_xieru(self):  # 探索关卡执行确认写入
        self.pcr_rizhixieru('探索', '已做')

    def dxc_db(self):  # 地下城关卡执行确认
        return self.rizhi_db(self.pcr_rizhiduqu('地下城'))

    def dxc_xieru(self):  # 地下城关卡执行确认写入
        self.pcr_rizhixieru('地下城', '已做')

    '''=============================================================================================================='''

    def jiemianxz(self, godata):
        temp1 = self.jmqr_jmtiaozhuan_path(godata)
        if isinstance(temp1, int) is True:
            print('查找页面失败')
            return False
        for obj in temp1:
            for obj1 in obj.data:
                if obj1[0] == 1:
                    sleep(2)
                    temp2 = self.pcr_find_pic(self.pic_config, obj1[1])
                    if temp2 == 1:
                        break
                if obj1[0] == 2:
                    sleep(2)
                    temp2 = self.pcr_find_word(obj1[1])
                    if temp2 == 1:
                        break
                if obj1[0] == 3:
                    sleep(2)
                    temp2 = self.pcr_find_pic_click(self.pic_config, obj1[1], obj1[2])
                    if temp2 == 1:
                        break

    def pcr_jm_obj(self):
        data = [
                # 主页
                PcrData.jm_zhuye,
                PcrData.jm_renwu,
                # 冒险
                PcrData.jm_maoxian,

                PcrData.jm_tansuo,
                PcrData.jm_tansuo_jingyan,
                PcrData.jm_tansuo_mana,
                PcrData.jm_dixiacheng,
                PcrData.jm_zhuxian,
                #  家园
                PcrData.jm_jiayuan
        ]
        self.pcr.list_InterFace_add(data)
        self.pcr.list_InterFace_list_add2()
        self.pcr.map_obj_list_add()

    def pcr_jm_path(self,nowdata:str,godata:str):
        temp1 = self.pcr.map_go_map_path(nowdata,godata)
        temp1 = temp1[1:]
        return temp1

    def jmqr_dqjm(self):
        for obj in PcrData.xunlu_jmqr:
            temp1 = self.pcr_find_word(obj[1])
            if temp1 == 1:
                print("当前界面："+obj[0])
                return obj[0]
        return -1

    def jmqr_jmtiaozhuan_path(self, data: str):
        temp1 = self.jmqr_dqjm()
        if temp1 != -1:
            temp2 = self.pcr_jm_path(temp1, data)
            return temp2
        else:
            return -1

    '''=============================================================================================================='''
