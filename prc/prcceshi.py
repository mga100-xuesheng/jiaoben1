import gongneng.gongnengdy
import zh_data
from prc.Pcr import Pcr
from jichu.gndy import GongNengdy
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

    def richangsd(self):
        print(1)

    # pcr.ldbangding("公主连结国服")
    # dizhi = "C:\\Users\\29412\\Desktop\\prc\\ziku1.txt"
    # pcr.zikusz([dizhi])
    # pcr.dqziku(0)
    # pcr.jiemianxz("主线冒险")
    # pcr.zhuxiangkxz("2-2-1")
    # pcr.kunnansd(0,1)
    # print(pcr.jmqr_dqjm())
    # pcr.jiemianxz("主线冒险")
    # pcr.zhuxiangkxz("2-1-2")
    # print(pcr.kunnansd(1))
    pcr.pcr_rizhi_update()
    print(pcr.pcr_rizhiduqu("体力"))
    print(pcr.rw_tili())

    # print(pcr.tili_sum())
    pcr.ldjiebang()
