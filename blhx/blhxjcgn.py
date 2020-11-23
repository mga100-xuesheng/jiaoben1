from jichu.gndy import *


class BlHx:
    def __init__(self, xm_data, pic_config, chuangkou_name, ziku_path: list):
        self.pcr = GongNengdy(xm_data, pic_config, chuangkou_name, ziku_path)
        self.pic_config = pic_config
