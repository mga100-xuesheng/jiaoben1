from datetime import datetime
from random import shuffle
from time import sleep
from zh_data import PcrData
from prc.Pcr_chongxie import PcR


class PcrCeshi:
    pcr = PcR("pcr", ["C:\\Users\\29412\\Desktop\\prc\\", ".bmp", "252525"], "公主连结国服",
              ["C:\\Users\\29412\\Desktop\\prc\\ziku1.txt"])

    def juesesuipian(self, data1, data2):
        self.pcr.zhuxiangkxz(data1)
        self.pcr.kunnansd(data2)

    def richangjuesesd(self, data):
        self.pcr.jiemianxz("主线冒险")
        for x in range(len(data)):
            self.juesesuipian(data[x][0], data[x][1])

    @staticmethod
    def sd_shujuchuli(data, cz):
        for x in range(len(data)):
            if len(data[x]) == 2:
                continue
            else:
                data[x].append(cz)
        return data

    def suipiansd(self):
        kekeluo = self.sd_shujuchuli([["2-1-1"], ["2-4-1"], ["2-13-1"]], 0)
        peke = self.sd_shujuchuli([["2-3-1"], ["2-7-1"]], 0)
        kan = self.sd_shujuchuli([["2-5-3"], ["2-12-2"]], 0)
        ue = self.sd_shujuchuli([["2-2-2"], ["2-6-1"]], 0)
        hutao = self.sd_shujuchuli([["2-1-2"], ["2-5-1"]], 0)
        jiansheng = self.sd_shujuchuli([["2-2-1"], ["2-8-1"]], 0)
        bingjiao = self.sd_shujuchuli([["2-7-2"], ["2-11-2"]], 0)
        chongdianbao = self.sd_shujuchuli([["2-9-3"], ["2-2-3"]], 0)
        now_time = datetime.now().strftime('%H')
        if "18" > now_time > "06":
            suipian = hutao
            shuffle(suipian)
        else:
            suipian = jiansheng + kan
            shuffle(suipian)
        print(suipian)
        self.richangjuesesd(suipian)

    '''==================================================================================================='''

    def tansuodj(self):
        self.pcr.pcr_dianji([737, 155, 1087, 213], 2, 3)

    def tansuomana(self):
        self.pcr.jiemianxz("探索马娜")
        self.tansuodj()
        self.pcr.tansuosd()

    def tansuojingyan(self):
        self.pcr.jiemianxz("探索经验")
        self.tansuodj()
        self.pcr.tansuosd()

    def tansuo(self):
        if self.pcr.tansuo_qr() == 1:
            self.tansuomana()
            sleep(3)
            self.tansuojingyan()
            self.pcr.tansuo_xieru()

    '''==================================================================================================='''

    def ghzjcz(self):
        self.pcr.jiemianxz("家园")
        if self.pcr.pcr_find_pic(self.pcr.pcr.pic_config, PcrData.ghzjygx) == 1:
            self.pcr.pcr_find_pic(self.pcr.pcr.pic_config, PcrData.ghzjsq)
            sleep(1.5)
            self.pcr.pcr_find_pic(self.pcr.pcr.pic_config, PcrData.ghzjgb)
            sleep(1)

    def gonghuizhijiatili(self):
        if self.pcr.jy_tili() == 1:
            now_time = datetime.now().strftime('%H')
            if "18" < now_time or now_time < "06":
                self.ghzjcz()
                self.pcr.jy_xieru()

    '''==================================================================================================='''

    def renwucz(self):
        self.pcr.jiemianxz("任务")
        sleep(1.5)
        self.pcr.pcr_dianji(PcrData.renwushouqu, 2, 3)
        self.pcr.pcr_find_pic(self.pcr.pic_config, PcrData.renwugb)

    def renwu(self):
        if self.pcr.rw_tili() == 1:
            now_time = datetime.now().strftime('%H')
            if now_time > "18" or now_time == "18" or now_time < "06":
                self.renwucz()
                self.pcr.rw_xieru()

    '''==================================================================================================='''

    def dxc_jmjc(self, data):
        dxc_temp1 = [[self.pcr.pcr_find_word, (PcrData.jmqr_dixiacheng[1],)],
                     [self.pcr.pcr_find_word, (PcrData.jmqr_gutadxc[1],)]]
        dxc_temp2 = self.pcr.pcr.duoxianc(dxc_temp1)
        if dxc_temp2[0] == 1:
            if self.pcr.pcr_find_pic(self.pcr.pic_config, PcrData.dxcjc) == 1:
                if data == '孤塔':
                    self.pcr.pcr_find_pic_click(self.pcr.pic_config, PcrData.gtdxcjm, PcrData.gtdxcjmxz)
                self.pcr.pcr_dianji(PcrData.dxcqyxz, 3, 6)
                return 1
            return 0
        else:
            return 1

    def richangdxc(self):  # 暂时不能用
        if self.pcr.dxc_db() == 1:
            self.pcr.jiemianxz("地下城")
            sleep(2)
            if self.dxc_jmjc("孤塔") == 1:
                self.pcr.richangdxc_pdjs(PcrData.gtdxc, 4)
                self.pcr.dxc_xieru()


temp1 = PcrCeshi()
temp1.pcr.pcr_rizhi_update()
temp1.gonghuizhijiatili()
temp1.renwu()
temp1.suipiansd()
temp1.tansuo()
temp1.richangdxc()
temp1.pcr.ldjiebang()
