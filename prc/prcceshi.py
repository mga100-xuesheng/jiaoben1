import gongneng.gongnengdy
import zh_data


class Prc:
    prc = gongneng.gongnengdy.GongNengdy("公主连结国服","prc",5,["C:\\Users\\29412\\Desktop\\prc\\",".bmp","252525"])
    prc.ldbangding()
    dizhi = "C:\\Users\\29412\\Desktop\\prc\\ziku1.txt"
    prc.zikubd([dizhi])
    prc.dqzifuku(0)
    shuzi = [zh_data.PrcData.zifu1,
             zh_data.PrcData.zifu2,
             zh_data.PrcData.zifu3,
             zh_data.PrcData.zifu4,
             zh_data.PrcData.zifu5,
             zh_data.PrcData.zifu6,
             zh_data.PrcData.zifu7,
             zh_data.PrcData.zifu8,
             zh_data.PrcData.zifu9,
             zh_data.PrcData.zifu0]
    sim = [1,1,1,1,1,1,1,1,1,1]
    t1 = prc.find_word_sumzh(zh_data.PrcData.gklist,[502,85,587,128],sim,0)
    print(t1)
    prc.ldjiebang()