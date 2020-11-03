import gongneng.gongnengdy
import zh_data
from prc.Pcr import Pcr
from jichu.gndy import GongNengdy
from prc.Pcr_chongxie import PcR


class PcrCeshi:
    pcr = PcR("pcr", ["C:\\Users\\29412\\Desktop\\prc\\", ".bmp", "252525"], 6)
    pcr.ldbangding("公主连结国服")
    dizhi = "C:\\Users\\29412\\Desktop\\prc\\ziku1.txt"
    pcr.zikusz([dizhi])
    pcr.dqziku(0)
    # pcr.jiemianxz("主线冒险")
    # pcr.zhuxiangkxz("2-2-1")
    # pcr.kunnansd(0,1)
    # print(pcr.jmqr_dqjm())
    # pcr.jiemianxz("主线冒险")
    # pcr.zhuxiangkxz("2-6-3")
    pcr.kunnansd(0)
    pcr.ldjiebang()
