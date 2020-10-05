import gongneng.gongnengzh


class GongNengdy:
    def __init__(self, mz_data, xm_data, xc_sum_data, pic_comfig):
        self.xm_gn = gongneng.gongnengzh.FindCol(mz_data, xm_data, xc_sum_data, pic_comfig)

    def ldbangding(self, data, xc_sum):
        self.xm_gn.leidiandxcbd(data, xc_sum)

    def ldjiebang(self):
        self.xm_gn.jiebang("")

    def shujucl1(self,data):
        return self.xm_gn.shujuchuli1(data)

    def shujucl2(self,data):
        return self.xm_gn.shujuchuli2(data)

    "--------------------------------------------------------------------"

    def find_pic(self,config,data,xc_sum):
        self.xm_gn.find_pic_data_shezhi(config,data,xc_sum)
        return self.xm_gn.find_pic()

    def find_pic_ex(self,config,data,xc_sum):
        self.xm_gn.find_pic_data_shezhi(config, data, xc_sum)
        return self.xm_gn.find_pic_ex()

    "--------------------------------------------------------------------"

    def find_word(self,data, xc_sum):
        self.xm_gn.find_data_shezhi(data,xc_sum)
        return self.xm_gn.find_word()

    def find_word_ex(self,data, xc_sum):
        self.xm_gn.find_data_shezhi(data,xc_sum)
        return self.xm_gn.find_word_ex()

    "--------------------------------------------------------------------"