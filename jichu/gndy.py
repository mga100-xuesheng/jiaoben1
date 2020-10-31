from jichu.gnzh import *
from jichu.jichugn import *
from datetime import datetime


class GongNengdy:
    def __init__(self, xm_data, pic_config, xc_sum_data):
        self.pic_config = pic_config
        self.sum_names = locals()
        self.xm_data = xm_data
        if xc_sum_data < 5:
            self.xc_sum_data = 5
        elif xc_sum_data > 5 or xc_sum_data == 5:
            self.xc_sum_data = xc_sum_data
        self.dqzk = -1
        for x in range(xc_sum_data):
            self.sum_names[self.xm_data + str(x)] = FindCol(pic_config)
        self.jiemian_dic = {}
        self.map_list = Map()

    def ldbangding(self, data):  # 雷电模拟器多线程绑定
        for x in range(self.xc_sum_data):
            self.sum_names[self.xm_data + str(x)].leidianbang(data, self.xm_data)

    def ldjiebang(self):  # 雷电模拟器解绑
        self.sum_names[self.xm_data + str(1)].jiebang()

    def shujucl1(self, data, xc_sum):  # 数据处理1  格式为：[[第一个数据],[第二个数据]]
        if xc_sum == "":
            xc_sum = 1
        return self.sum_names[self.xm_data + str(xc_sum)].shujuchuli11(data)

    def shujucl2(self, data, xc_sum):  # 数据处理2 格式为：[第一个数据,第二个数据]
        return self.sum_names[self.xm_data + str(xc_sum)].shujuchuli12(data)

    def dianji(self, data, min_time, max_time, xc_sum):  # 鼠标点击
        if xc_sum == "":
            xc_sum = 1
        self.sum_names[self.xm_data + str(xc_sum)].random_time(min_time, max_time)
        return self.sum_names[self.xm_data + str(xc_sum)].click(data)

    '''==================================================================================================='''

    def find_pic(self, config, data, xc_sum):  # 找图
        if xc_sum == "":
            xc_sum = 1
        self.sum_names[self.xm_data + str(xc_sum)].find_pic_data_shezhi(config, data)
        return self.sum_names[self.xm_data + str(xc_sum)].find_pic()

    def find_pic_ex(self, config, data, xc_sum):  # 找图扩展
        if xc_sum == "":
            xc_sum = 1
        self.sum_names[self.xm_data + str(xc_sum)].find_pic_data_shezhi(config, data)
        return self.sum_names[self.xm_data + str(xc_sum)].find_pic_ex()

    def find_pic_click(self, config, data, click, xc_sum):  # 找图成功点击
        temp1 = self.find_pic(config, data, xc_sum)
        if temp1 == 1:
            self.dianji(click, 1, 2, xc_sum)
            return 1
        else:
            return 0

    def find_pic_click1(self, config, data, click, xc_sum):  # 找图失败点击
        temp1 = self.find_pic(config, data, xc_sum)
        if temp1 == 1:
            return 0
        else:
            self.dianji(click, 1, 2, xc_sum)
            return 1

    '''==================================================================================================='''

    def zikubd(self, data):  # 字库绑定
        for x in range(self.xc_sum_data):
            for y in range(len(data)):
                self.sum_names[self.xm_data + str(x)].lw.SetDict(y, data[y])

    def dqziku(self, data):  # 当前字库选择
        if self.dqzk != data:
            for x in range(self.xc_sum_data):
                self.sum_names[self.xm_data + str(x)].lw.UseDict(data)
            self.dqzk = data
            return 2
        else:
            return 1

    def find_word(self, data, xc_sum):  # 找字
        if xc_sum == "":
            xc_sum = 1
        self.sum_names[self.xm_data + str(xc_sum)].find_data_shezhi(data)
        return self.sum_names[self.xm_data + str(xc_sum)].find_word()

    def find_word_click(self, data, click, xc_sum):  # 找字成功点击
        temp1 = self.find_word(data, xc_sum)
        if temp1 == 1:
            self.dianji(click, 1, 2, xc_sum)
            return 1
        else:
            return 0

    def find_word_click1(self, data, click, xc_sum):  # 找字失败点击
        temp1 = self.find_word(data, xc_sum)
        if temp1 == 1:
            return 0
        else:
            self.dianji(click, 1, 2, xc_sum)
            return 1

    def find_word_ex(self, data, xc_sum):  # 找字扩展
        if xc_sum == "":
            xc_sum = 1
        self.sum_names[self.xm_data + str(xc_sum)].find_data_shezhi(data)
        return self.sum_names[self.xm_data + str(xc_sum)].find_word_ex()

    def find_word_ex1(self, data, xc_sum):  # 找字扩展1
        if xc_sum == "":
            xc_sum = 1
        self.sum_names[self.xm_data + str(xc_sum)].find_data_shezhi(data)
        return self.sum_names[self.xm_data + str(xc_sum)].find_word_ex1()

    def find_word_ex1_shujucl2(self, data, xc_sum):  # 找字扩展1:数据处理2
        self.sum_names[self.xm_data + str(xc_sum)].find_data_shezhi(data)
        temp1 = self.find_word_ex1(data, xc_sum)
        if temp1[0] == 1:
            temp2 = self.sum_names[self.xm_data + str(xc_sum)].shujuchuli2(temp1[1])
            return temp2
        else:
            return [0]

    '''---------------------------------------------------------------------------------------------------'''

    def find_word_sum(self, data, find_sum, dizhi, sim: int, xc_sum):  # 文字数字查找
        temp1 = []
        for x in range(len(data)):
            data[x][0] = dizhi
            data[x][3] = sim
            temp2 = self.find_word_ex1_shujucl2(data[x], xc_sum)
            if temp2[0] == 1:
                for x in range(len(temp2[1])):
                    temp2[1][x] = temp2[1][x].split(",")
                    temp2[1][x].append(find_sum)
                    temp1.append(temp2[1][x])
        if len(temp1) == 0:
            return [[-1]]
        else:
            return temp1

    def find_word_sum1(self, data, find_sum, xc_sum):  # 文字数字查找1
        temp1 = []
        for x in range(len(data)):
            temp2 = self.find_word_ex1_shujucl2(data[x], xc_sum)
            if temp2[0] == 1:
                for x in range(len(temp2[1])):
                    temp2[1][x] = temp2[1][x].split(",")
                    temp2[1][x].append(find_sum)
                    temp1.append(temp2[1][x])
        if len(temp1) == 0:
            return [[-1]]
        else:
            return temp1

    def find_word_sumzh(self, data: list, dizhi: list, sim: list, fangxian: int):  # 文字数字整合查找
        temp1 = []
        temp4 = ""
        zifu1 = MyThread(self.find_word_sum, (tuple(data[0]), 1, tuple(dizhi), sim[0], 1))
        zifu2 = MyThread(self.find_word_sum, (data[1], 2, dizhi, sim[1], 2))
        zifu3 = MyThread(self.find_word_sum, (data[2], 3, dizhi, sim[2], 3))
        zifu4 = MyThread(self.find_word_sum, (data[3], 4, dizhi, sim[3], 4))
        zifu5 = MyThread(self.find_word_sum, (data[4], 5, dizhi, sim[4], 5))
        zifu1.start()
        zifu2.start()
        zifu3.start()
        zifu4.start()
        zifu5.start()
        zifu1.join()
        zifu2.join()
        zifu3.join()
        zifu4.join()
        zifu5.join()
        temp2 = [zifu1.get_result(), zifu2.get_result(), zifu3.get_result(), zifu4.get_result(), zifu5.get_result()]
        for x in range(len(temp2)):
            if temp2[x][0][0] != -1:
                for y in range(len(temp2[x])):
                    temp1.append(temp2[x][y])
        zifu1 = MyThread(self.find_word_sum, (data[5], 6, dizhi, sim[5], 1))
        zifu2 = MyThread(self.find_word_sum, (data[6], 7, dizhi, sim[6], 2))
        zifu3 = MyThread(self.find_word_sum, (data[7], 8, dizhi, sim[7], 3))
        zifu4 = MyThread(self.find_word_sum, (data[8], 9, dizhi, sim[8], 4))
        zifu5 = MyThread(self.find_word_sum, (data[9], 0, dizhi, sim[9], 5))
        zifu1.start()
        zifu2.start()
        zifu3.start()
        zifu4.start()
        zifu5.start()
        zifu1.join()
        zifu2.join()
        zifu3.join()
        zifu4.join()
        zifu5.join()
        temp2 = [zifu1.get_result(), zifu2.get_result(), zifu3.get_result(), zifu4.get_result(), zifu5.get_result()]
        for x in range(len(temp2)):
            if temp2[x][0][0] != -1:
                for y in range(len(temp2[x])):
                    temp1.append(temp2[x][y])
        if fangxian == 0:
            for x in range(len(temp1)):
                for y in range(len(temp1) - x - 1):
                    if int(temp1[y][0]) > int(temp1[y + 1][0]):
                        temp3 = temp1[y]
                        temp1[y + 1] = temp1[y]
                        temp1[y + 1] = temp3
        else:
            for x in range(len(temp1)):
                for y in range(len(temp1) - x - 1):
                    if int(temp1[y][1]) > int(temp1[y + 1][1]):
                        temp3 = temp1[y]
                        temp1[y + 1] = temp1[y]
                        temp1[y + 1] = temp3
        for x in range(len(temp1)):
            temp4 = temp4 + str(temp1[x][2])
        if temp4 != "":
            return int(temp4)
        else:
            return -1

    def find_word_sumzh1(self, data: list, fangxian: int):  # 文字数字整合查找1
        temp1 = []
        temp4 = ""
        zifu1 = MyThread(self.find_word_sum1, (data[0], 1, 1))
        zifu2 = MyThread(self.find_word_sum1, (data[1], 2, 2))
        zifu3 = MyThread(self.find_word_sum1, (data[2], 3, 3))
        zifu4 = MyThread(self.find_word_sum1, (data[3], 4, 4))
        zifu5 = MyThread(self.find_word_sum1, (data[4], 5, 5))
        zifu1.start()
        zifu2.start()
        zifu3.start()
        zifu4.start()
        zifu5.start()
        zifu1.join()
        zifu2.join()
        zifu3.join()
        zifu4.join()
        zifu5.join()
        temp2 = [zifu1.get_result(), zifu2.get_result(), zifu3.get_result(), zifu4.get_result(), zifu5.get_result()]
        for x in range(len(temp2)):
            if temp2[x][0][0] != -1:
                for y in range(len(temp2[x])):
                    temp1.append(temp2[x][y])
        zifu1 = MyThread(self.find_word_sum1, (data[5], 6, 1))
        zifu2 = MyThread(self.find_word_sum1, (data[6], 7, 2))
        zifu3 = MyThread(self.find_word_sum1, (data[7], 8, 3))
        zifu4 = MyThread(self.find_word_sum1, (data[8], 9, 4))
        zifu5 = MyThread(self.find_word_sum1, (data[9], 0, 5))
        zifu1.start()
        zifu2.start()
        zifu3.start()
        zifu4.start()
        zifu5.start()
        zifu1.join()
        zifu2.join()
        zifu3.join()
        zifu4.join()
        zifu5.join()
        temp2 = [zifu1.get_result(), zifu2.get_result(), zifu3.get_result(), zifu4.get_result(), zifu5.get_result()]
        for x in range(len(temp2)):
            if temp2[x][0][0] != -1:
                for y in range(len(temp2[x])):
                    temp1.append(temp2[x][y])
        if fangxian == 0:
            for x in range(len(temp1)):
                for y in range(len(temp1) - x - 1):
                    if int(temp1[y][0]) > int(temp1[y + 1][0]):
                        temp3 = temp1[y]
                        temp1[y + 1] = temp1[y]
                        temp1[y + 1] = temp3
        else:
            for x in range(len(temp1)):
                for y in range(len(temp1) - x - 1):
                    if int(temp1[y][1]) > int(temp1[y + 1][1]):
                        temp3 = temp1[y]
                        temp1[y + 1] = temp1[y]
                        temp1[y + 1] = temp3
        for x in range(len(temp1)):
            temp4 = temp4 + str(temp1[x][2])
        if temp4 != "":
            return int(temp4)
        else:
            return -1

    '''==================================================================================================='''
    '''==================================================================================================='''

    def duoxianc(self, data: list):  # 多线程定义
        if len(data) > self.xc_sum_data:
            return [-1]
        temp1 = locals()
        temp2 = []
        for x in range(len(data)):
            temp1["duoxc" + str(x)] = MyThread(data[x][0], data[x][1])
        for x in range(len(data)):
            temp1["duoxc" + str(x)].start()
        for x in range(len(data)):
            temp1["duoxc" + str(x)].join()
        for x in range(len(data)):
            temp2.append(temp1["duoxc" + str(x)].get_result())
        return temp2

    '''==================================================================================================='''

    @staticmethod
    def rizhi_xieru(path: str, name: str, keyword: str, data: str, xieru_time: str):  # 日志写入
        temp1 = RiZhi1(path)
        temp2 = temp1.utf_8_duqu(name)
        print(temp2)
        temp4 = []
        temp5 = 0
        for x in temp2:
            if x.find(keyword) != -1:
                temp3 = x[:x.find('：') + 1] + data
                temp5 = 1
            else:
                temp3 = x
            if temp5 == 1:
                temp4.append(temp3)
                temp5 = 0
            else:
                if x.find("-") == -1:
                    temp4.append(x)
        print(temp4)
        temp1.utf_8_xieru(name, temp4, xieru_time)

    @staticmethod
    def rizhi_duqu(path: str, name: str, keyword: str):  # 日志读取
        temp1 = RiZhi1(path)
        temp2 = temp1.utf_8_duqu(name)
        for x in temp2:
            if x.find(keyword) != -1:
                return x[x.find('：') + 1:]

    @staticmethod
    def time_db(data1, data2):  # 时间对比
        d1 = datetime.strptime(data1, '%Y-%m-%d-%H')
        d2 = datetime.strptime(data2, '%Y-%m-%d-%H')
        d3 = str(d2 - d1)
        if d3.find(',') != -1:
            d4 = d3.split(',')
            d4[0] = d4[0][:d4[0].find('d')]
            d4[0] = d4[0][:d4[0].find(' ')]
            d7 = int(d4[0]) * 24
            d4[1] = d4[1][1:]
            d5 = d4[1].split(':')
            d6 = int(d5[0]) + int(d7)
        else:
            d5 = d3.split(':')
            d6 = d5[0]
        return int(d6)

    '''==================================================================================================='''

    def InterFace(self, name: str, data: list):  # 界面对象定义
        self.jiemian_dic[name] = InterFace(name, data)

    def InterFace_list_add(self, name: str, guanxi, data):  # 此界面可去界面对象定义
        self.jiemian_dic[name].add(guanxi, data)

    def map_obj_add(self, name: str):  # 生成地图
        self.map_list.add_list(self.jiemian_dic[name])

    def map_path(self, nowdata, godata):  # 当前界面去其他界面路径查询
        return self.map_list.get_go_map_path(nowdata, godata)

    '''---------------------------------------------------------------------------------------------------'''

    def list_InterFace_add(self, name_data: list):  # 界面对象定义_列表方式定义
        for x in name_data:
            self.InterFace(x[0], x[1])

    def list_InterFace_list_add(self, name: str, name_guanxi: list):  # 此界面可去界面对象定义_列表方式定义
        for x in name_guanxi:
            self.InterFace_list_add(name, x[0], x[1])

    def map_obj_list_add(self):  # 地图结点添加
        for x in self.jiemian_dic.keys():
            self.map_obj_add(str(x))

    def map_go_map_path(self, nowmap, gomap):  # 返回此界面去另外界面的最短路径
        return self.map_list.present_go_target(nowmap, gomap)
