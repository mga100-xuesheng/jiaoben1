from jichu.gndy import *
from zh_data import BlhxData


class BlHx:
    def __init__(self, xm_data, chuangkou_name, ziku_path=None, blhx_config=None):
        if ziku_path is None:
            ziku_path = BlhxData.ziku_path
        if ziku_path is None:
            blhx_config = BlhxData.blhx_find_pic_config
        self.blhx = GongNengdy(xm_data, blhx_config, chuangkou_name, ziku_path)
        self.blhx_config = blhx_config

    '''--------------------------------------------------------------------------------------------------------------'''

    def blhx_find_pic(self, data, config=None):
        if config is None:
            config = BlhxData.blhx_find_pic_config
        temp1 = self.blhx.find_pic(config, data)
        return temp1

    def blhx_find_pic_click(self, data, click, config=None):
        if config is None:
            config = BlhxData.blhx_find_pic_config
        temp1 = self.blhx.find_pic_click(config, data, click)
        return temp1

    def blhx_find_pic_click1(self, data, click, config=None):
        if config is None:
            config = BlhxData.blhx_find_pic_config
        temp1 = self.blhx.find_pic_click1(config, data, click)
        return temp1

    '''--------------------------------------------------------------------------------------------------------------'''

    def blhx_find_word(self, data):
        temp1 = self.blhx.find_word(data)
        return temp1

    def blhx_find_word_click(self, data, click):
        temp1 = self.blhx.find_word_click(data, click)
        return temp1

    def blhx_find_word_click1(self, data, click):
        temp1 = self.blhx.find_word_click1(data, click)
        return temp1

    '''--------------------------------------------------------------------------------------------------------------'''

    def blhx_dianji(self, data, min_time, max_time):
        self.blhx.dianji(data, min_time, max_time)

    '''=============================================================================================================='''
