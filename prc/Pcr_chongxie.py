from jichu.gndy import GongNengdy
from zh_data import PcrData


temp1 = GongNengdy("pcr", ["C:\\Users\\29412\\Desktop\\prc\\", ".bmp", "252525"],6)
temp1.ldbangding("公主连结国服")
temp2 = temp1.duoxc_3(temp1.find_pic, (tuple(temp1.pic_config), tuple(PcrData.sdtg), 1),
                      temp1.find_pic, (tuple(temp1.pic_config), tuple(PcrData.sdtg), 2),
                      temp1.find_pic, (tuple(temp1.pic_config), tuple(PcrData.sdtg), 3))
print(temp2)
temp1.ldjiebang()