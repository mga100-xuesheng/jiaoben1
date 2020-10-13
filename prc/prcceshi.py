import gongneng.gongnengdy
import zh_data
from prc.Pcr import Pcr


class PcrCeshi:
    pcr = Pcr("公主连结国服", "pcr", 5, ["C:\\Users\\29412\\Desktop\\prc\\", ".bmp", "252525"])
    pcr.bangding()
    dizhi = "C:\\Users\\29412\\Desktop\\prc\\ziku1.txt"
    pcr.zikusz([dizhi])
    pcr.dqzikusz(0)
    pcr.zhuxian("2-4-1")
    # print(pcr.guanqia_sum())

    pcr.jiebang()