import gongneng.gongnengdy
import zh_data
from prc.Pcr import Pcr
from jichu.gndy import GongNengdy
from prc.Pcr_chongxie import PcR


class PcrCeshi:
    # pcr = Pcr("公主连结国服", "pcr", 6, ["C:\\Users\\29412\\Desktop\\prc\\", ".bmp", "252525"])
    # pcr.bangding()
    # dizhi = "C:\\Users\\29412\\Desktop\\prc\\ziku1.txt"
    # pcr.zikusz([dizhi])
    # pcr.dqzikusz(0)
    # # pcr.zhuxian("2-4-1")
    # # print(pcr.guanqia_sum())
    # pcr.tansuosd()
    # pcr.jiebang()
    pcr = PcR("pcr", ["C:\\Users\\29412\\Desktop\\prc\\", ".bmp", "252525"], 6)
    pcr.ldbangding("公主连结国服")
    dizhi = "C:\\Users\\29412\\Desktop\\prc\\ziku1.txt"
    pcr.zikusz([dizhi])
    pcr.dqziku(0)
    pcr.zhuxiangkxz("2-2-1")
    pcr.ldjiebang()
