from jichu.gnzh import *
from jichu.jichugn import *
from datetime import datetime
from time import sleep


class GongNengdy:
    xc_sum_data1 = 0
    lock = threading.Lock()

    def __init__(self, xm_data, pic_config, chuangkou_name, ziku_path: list):
        self.pic_config = pic_config
        self.sum_names = {}
        self.xm_data = xm_data
        self.chuangkou_name = chuangkou_name
        self.dqzk = -1
        self.ziku_path = ziku_path
        self.sum_names_list = []
        self.sum_names_key = []
        self.obj_add_list = []
        self.obj_list_sum = 0
        self.obj_list_name = []
        self.obj_key = []
        self.jiemian_dic = {}
        self.map_list = Map()
        self.lock = threading.Lock()
        self.obj_add()

    def obj_add(self):  # 生成执行对象
        self.obj_list_sum = self.obj_list_sum + 1
        temp1 = self.xm_data + str(self.obj_list_sum)
        # print("创建对象："+temp1)
        self.sum_names[temp1] = FindCol(self.pic_config)
        self.sum_names[temp1].leidianbang(self.chuangkou_name, self.xm_data)
        self.zikubd(self.ziku_path)
        self.dqziku(0)
        self.sum_names_list.append(temp1)
        self.sum_names_key.append(1)
        GongNengdy.xc_sum_data1 = GongNengdy.xc_sum_data1 + 1

    def obj_key_chaxun(self, data, name=None):  # 执行对象查询
        while True:
            for z in range(20):
                self.lock.acquire()
                if data == 1:
                    for x in range(len(self.sum_names_key)):
                        if self.sum_names_key[x] == 1:
                            self.sum_names_key[x] = 0
                            temp1 = self.sum_names_list[x]
                            # print('使用线程：'+str(temp1))
                            self.lock.release()
                            return temp1
                elif data == 2:
                    for x in range(len(self.sum_names_list)):
                        if self.sum_names_list[x] == name:
                            self.sum_names_key[x] = 1
                            # print('回收线程:'+str(self.sum_names_list[x]))
                            self.lock.release()
                            return True
                self.lock.release()
                sleep(0.1)
            self.lock.acquire()
            self.obj_add()
            self.lock.release()

    def obj_fenpei(self):  # 执行对象分配
        return self.obj_key_chaxun(1)

    def obj_shouhui(self, name):  # 执行对象收回
        return self.obj_key_chaxun(2, name)

    def ldbangding(self, data):  # 雷电模拟器多线程绑定
        for x in self.sum_names.keys():
            self.sum_names[x].leidianbang(data, self.xm_data)

    def ldjiebang(self):  # 雷电模拟器解绑
        self.sum_names[self.xm_data + str(1)].jiebang()

    def shujucl1(self, data):  # 数据处理1  格式为：[[第一个数据],[第二个数据]]
        xc_sum_temp = self.obj_fenpei()
        temp1 = self.sum_names[xc_sum_temp].shujuchuli1(data)
        self.obj_shouhui(xc_sum_temp)
        return temp1

    def shujucl2(self, data):  # 数据处理2 格式为：[第一个数据,第二个数据]
        xc_sum_temp = self.obj_fenpei()
        temp1 = self.sum_names[xc_sum_temp].shujuchuli2(data)
        self.obj_shouhui(xc_sum_temp)
        return temp1

    def dianji(self, data, min_time, max_time):  # 鼠标点击
        xc_sum_temp = self.obj_fenpei()
        self.sum_names[xc_sum_temp].random_time(min_time, max_time)
        temp1 = self.sum_names[xc_sum_temp].click(data)
        self.obj_shouhui(xc_sum_temp)
        return temp1

    '''==================================================================================================='''

    def find_pic(self, config, data):  # 找图
        xc_sum_temp = self.obj_fenpei()
        self.sum_names[xc_sum_temp].find_pic_data_shezhi(config, data)
        temp1 = self.sum_names[xc_sum_temp].find_pic()
        self.obj_shouhui(xc_sum_temp)
        return temp1

    def find_pic_ex(self, config, data):  # 找图扩展
        xc_sum_temp = self.obj_fenpei()
        self.sum_names[xc_sum_temp].find_pic_data_shezhi(config, data)
        temp1 = self.sum_names[xc_sum_temp].find_pic_ex()
        self.obj_shouhui(xc_sum_temp)
        return temp1

    def find_pic_click(self, config, data, click):  # 找图成功点击
        temp1 = self.find_pic(config, data)
        if temp1 == 1:
            self.dianji(click, 1, 2)
            return 1
        else:
            return 0

    def find_pic_click1(self, config, data, click):  # 找图失败点击
        temp1 = self.find_pic(config, data)
        if temp1 == 1:
            return 0
        else:
            self.dianji(click, 1, 2)
            return 1

    '''==================================================================================================='''

    def zikubd(self, data):  # 字库绑定
        for x in self.sum_names.keys():
            for y in range(len(data)):
                self.sum_names[x].lw.SetDict(y, data[y])

    def dqziku(self, data):  # 当前字库选择
        if self.dqzk != data:
            for x in self.sum_names.keys():
                self.sum_names[x].lw.UseDict(data)
            self.dqzk = data
            return 2
        else:
            return 1

    def find_word(self, data: list):  # 找字
        xc_sum_temp = self.obj_fenpei()
        self.sum_names[xc_sum_temp].find_data_shezhi(data)
        temp1 = self.sum_names[xc_sum_temp].find_word()
        self.obj_shouhui(xc_sum_temp)
        return temp1

    def find_word_click(self, data, click):  # 找字成功点击
        temp1 = self.find_word(data)
        if temp1 == 1:
            self.dianji(click, 1, 2)
            return 1
        else:
            return 0

    def find_word_click1(self, data, click):  # 找字失败点击
        temp1 = self.find_word(data)
        if temp1 == 1:
            return 0
        else:
            self.dianji(click, 1, 2)
            return 1

    def find_word_ex(self, data):  # 找字扩展
        xc_sum_temp = self.obj_fenpei()
        self.sum_names[xc_sum_temp].find_data_shezhi(data)
        temp1 = self.sum_names[xc_sum_temp].find_word_ex()
        self.obj_shouhui(xc_sum_temp)
        return temp1

    def find_word_ex1(self, data):  # 找字扩展1
        xc_sum_temp = self.obj_fenpei()
        self.sum_names[xc_sum_temp].find_data_shezhi(data)
        temp1 = self.sum_names[xc_sum_temp].find_word_ex1()
        self.obj_shouhui(xc_sum_temp)
        return temp1

    def find_word_ex1_shujucl2(self, data):  # 找字扩展1:数据处理2
        temp1 = self.find_word_ex1(data)
        if temp1[0] == 1:
            xc_sum_temp = self.obj_fenpei()
            temp2 = self.sum_names[xc_sum_temp].shujuchuli2(temp1[1])
            self.obj_shouhui(xc_sum_temp)
            return temp2
        else:
            return [0]

    '''---------------------------------------------------------------------------------------------------'''

    def find_word_sum(self, data, find_sum, dizhi, sim: int):  # 文字数字查找
        temp1 = []
        for x in range(len(data)):
            data[x][0] = dizhi
            data[x][3] = sim
            temp2 = self.find_word_ex1_shujucl2(data[x])
            if temp2[0] == 1:
                for x in range(len(temp2[1])):
                    temp2[1][x] = temp2[1][x].split(",")
                    temp2[1][x].append(find_sum)
                    temp1.append(temp2[1][x])
        if len(temp1) == 0:
            return [[-1]]
        else:
            return temp1

    def find_word_sum1(self, data, find_sum):  # 文字数字查找1
        temp1 = []
        for x in range(len(data)):
            temp2 = self.find_word_ex1_shujucl2(data[x])
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
        dxc_temp1 = [[self.find_word_sum, (data[0], 1, dizhi, sim[0])],
                     [self.find_word_sum, (data[1], 2, dizhi, sim[1])],
                     [self.find_word_sum, (data[2], 3, dizhi, sim[2])],
                     [self.find_word_sum, (data[3], 4, dizhi, sim[3])],
                     [self.find_word_sum, (data[4], 5, dizhi, sim[4])]]
        temp2 = self.duoxianc(dxc_temp1)
        # zifu1 = MyThread(self.find_word_sum, (tuple(data[0]), 1, tuple(dizhi), sim[0]))
        # zifu2 = MyThread(self.find_word_sum, (data[1], 2, dizhi, sim[1]))
        # zifu3 = MyThread(self.find_word_sum, (data[2], 3, dizhi, sim[2]))
        # zifu4 = MyThread(self.find_word_sum, (data[3], 4, dizhi, sim[3]))
        # zifu5 = MyThread(self.find_word_sum, (data[4], 5, dizhi, sim[4]))
        # zifu1.start()
        # zifu2.start()
        # zifu3.start()
        # zifu4.start()
        # zifu5.start()
        # zifu1.join()
        # zifu2.join()
        # zifu3.join()
        # zifu4.join()
        # zifu5.join()
        # temp2 = [zifu1.get_result(), zifu2.get_result(), zifu3.get_result(), zifu4.get_result(), zifu5.get_result()]
        for x in range(len(temp2)):
            if temp2[x][0][0] != -1:
                for y in range(len(temp2[x])):
                    temp1.append(temp2[x][y])
        # zifu1 = MyThread(self.find_word_sum, (data[5], 6, dizhi, sim[5]))
        # zifu2 = MyThread(self.find_word_sum, (data[6], 7, dizhi, sim[6]))
        # zifu3 = MyThread(self.find_word_sum, (data[7], 8, dizhi, sim[7]))
        # zifu4 = MyThread(self.find_word_sum, (data[8], 9, dizhi, sim[8]))
        # zifu5 = MyThread(self.find_word_sum, (data[9], 0, dizhi, sim[9]))
        # zifu1.start()
        # zifu2.start()
        # zifu3.start()
        # zifu4.start()
        # zifu5.start()
        # zifu1.join()
        # zifu2.join()
        # zifu3.join()
        # zifu4.join()
        # zifu5.join()
        # temp2 = [zifu1.get_result(), zifu2.get_result(), zifu3.get_result(), zifu4.get_result(), zifu5.get_result()]
        dxc_temp1 = [[self.find_word_sum, (data[5], 6, dizhi, sim[5])],
                     [self.find_word_sum, (data[6], 7, dizhi, sim[6])],
                     [self.find_word_sum, (data[7], 8, dizhi, sim[7])],
                     [self.find_word_sum, (data[8], 9, dizhi, sim[8])],
                     [self.find_word_sum, (data[9], 0, dizhi, sim[9])]]
        temp2 = self.duoxianc(dxc_temp1)
        for x in range(len(temp2)):
            if temp2[x][0][0] != -1:
                for y in range(len(temp2[x])):
                    temp1.append(temp2[x][y])
        if fangxian == 0:
            for x in range(len(temp1)):
                for y in range(len(temp1) - x - 1):
                    if int(temp1[y][0]) > int(temp1[y + 1][0]):
                        temp3 = temp1[y + 1]
                        temp1[y + 1] = temp1[y]
                        temp1[y] = temp3
        else:
            for x in range(len(temp1)):
                for y in range(len(temp1) - x - 1):
                    if int(temp1[y][1]) > int(temp1[y + 1][1]):
                        temp3 = temp1[y + 1]
                        temp1[y + 1] = temp1[y]
                        temp1[y] = temp3
        for x in range(len(temp1)):
            temp4 = temp4 + str(temp1[x][2])
        if temp4 != "":
            return int(temp4)
        else:
            return -1

    def find_word_sumzh1(self, data: list, fangxian: int):  # 文字数字整合查找1
        temp1 = []
        temp4 = ""
        # dxc_temp1 = [[self.find_word_sum1, (data[0], 1)],
        #              [self.find_word_sum1, (data[1], 2)],
        #              [self.find_word_sum1, (data[2], 3)],
        #              [self.find_word_sum1, (data[3], 4)],
        #              [self.find_word_sum1, (data[4], 5)]]
        # temp2 = self.duoxianc(dxc_temp1)
        # for x in range(len(temp2)):
        #     if temp2[x][0][0] != -1:
        #         for y in range(len(temp2[x])):
        #             temp1.append(temp2[x][y])
        dxc_temp1 = [[self.find_word_sum1, (data[0], 1)],
                     [self.find_word_sum1, (data[1], 2)],
                     [self.find_word_sum1, (data[2], 3)],
                     [self.find_word_sum1, (data[3], 4)],
                     [self.find_word_sum1, (data[4], 5)],
                     [self.find_word_sum1, (data[5], 6)],
                     [self.find_word_sum1, (data[6], 7)],
                     [self.find_word_sum1, (data[7], 8)],
                     [self.find_word_sum1, (data[8], 9)],
                     [self.find_word_sum1, (data[9], 0)]]
        temp2 = self.duoxianc(dxc_temp1)
        for x in range(len(temp2)):
            if temp2[x][0][0] != -1:
                for y in range(len(temp2[x])):
                    temp1.append(temp2[x][y])
        if fangxian == 0:
            for x in range(len(temp1)):
                for y in range(len(temp1) - x - 1):
                    if int(temp1[y][0]) > int(temp1[y + 1][0]):
                        temp3 = temp1[y + 1]
                        temp1[y + 1] = temp1[y]
                        temp1[y] = temp3
        else:
            for x in range(len(temp1)):
                for y in range(len(temp1) - x - 1):
                    if int(temp1[y][1]) > int(temp1[y + 1][1]):
                        temp3 = temp1[y + 1]
                        temp1[y + 1] = temp1[y]
                        temp1[y] = temp3
        for x in range(len(temp1)):
            temp4 = temp4 + str(temp1[x][2])
        if temp4 != "":
            return int(temp4)
        else:
            return -1

    '''==================================================================================================='''
    '''==================================================================================================='''

    def duoxianc(self, data: list):  # 多线程定义
        temp1 = DuoXianc()
        temp2 = temp1.duoxianc(data)
        return temp2

    '''==================================================================================================='''

    @staticmethod
    def rizhi_xieru(path: str, name: str, keyword: str, data: str, xieru_time: str):  # 日志写入
        temp1 = RiZhi1(path)
        temp2 = temp1.utf_8_duqu(name)
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
        temp1.utf_8_xieru(xieru_time, name, temp4)

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

    def InterFace(self, name: str, data: list, guanxi: list):  # 界面对象定义
        self.jiemian_dic[name] = InterFace(name, data, guanxi)

    def InterFace_list_add(self, name: str, guanxi, data):  # 此界面可去界面对象定义
        self.jiemian_dic[name].add(guanxi, data)

    def list_InterFace_list_add(self, name):
        for x in self.jiemian_dic[name].guanxi_list:
            self.InterFace_list_add(name, self.jiemian_dic[x], 0)

    def map_obj_add(self, name: str):  # 生成地图
        self.map_list.add_list(self.jiemian_dic[name])

    def map_path(self, nowdata, godata):  # 当前界面去其他界面路径查询
        return self.map_list.get_go_map_path(nowdata, godata)

    '''---------------------------------------------------------------------------------------------------'''

    def list_InterFace_add(self, name_data: list):  # 界面对象定义_列表方式定义
        for x in name_data:
            self.InterFace(x[0], x[1], x[2])

    def list_InterFace_list_add1(self, name: str, name_guanxi: list):  # 此界面可去界面对象定义_列表方式定义
        for x in name_guanxi:
            self.InterFace_list_add(name, self.jiemian_dic[x[0]], x[1])

    def list_InterFace_list_add2(self):
        for x in self.jiemian_dic.keys():
            self.list_InterFace_list_add(x)

    def map_obj_list_add(self):  # 地图结点添加
        for x in self.jiemian_dic.keys():
            self.map_obj_add(str(x))

    def map_go_map_path(self, nowmap, gomap):  # 返回此界面去另外界面的最短路径
        return self.map_list.present_go_target(nowmap, gomap)


class DuoXianc:
    def __init__(self):
        self.duoxianc1 = {}
        self.duoxianc2 = []
        self.duoxianc3 = []

    def duoxianc(self, data: list):
        for x in range(len(data)):
            self.duoxianc1["duoxc" + str(x)] = MyThread(data[x][0], args=data[x][1])
        for x in self.duoxianc1.keys():
            self.duoxianc1[x].start()
        for x in self.duoxianc1.keys():
            self.duoxianc1[x].join()
        for x in self.duoxianc1.keys():
            self.duoxianc3.append(self.duoxianc1[x].get_result())
        return self.duoxianc3
