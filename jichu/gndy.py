from jichu.gnzh import FindCol
from jichu.jichu import MyThread


class GongNengdy:
    def __init__(self, xm_data, pic_comfig, xc_sum_data):
        self.pic_config = pic_comfig
        self.sum_names = locals()
        self.xm_data = xm_data
        if xc_sum_data < 5:
            self.xc_sum_data = 5
        elif xc_sum_data > 5 or xc_sum_data == 5:
            self.xc_sum_data = xc_sum_data
        self.dqzk = -1
        for x in range(xc_sum_data):
            self.sum_names[self.xm_data + str(x)] = FindCol(pic_comfig)

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

    def dianji(self,data,min_time,max_time,xc_sum):  # 鼠标点击
        if xc_sum == "":
            xc_sum = 1
        self.sum_names[self.xm_data + str(xc_sum)].random_time(min_time,max_time)
        return self.sum_names[self.xm_data + str(xc_sum)].click(data)

    '''==================================================================================================='''

    def find_pic(self,config,data,xc_sum):  # 找图
        if xc_sum == "":
            xc_sum = 1
        self.sum_names[self.xm_data + str(xc_sum)].find_pic_data_shezhi(config,data)
        return self.sum_names[self.xm_data + str(xc_sum)].find_pic()

    def find_pic_ex(self,config,data,xc_sum):  # 找图扩展
        if xc_sum == "":
            xc_sum = 1
        self.sum_names[self.xm_data + str(xc_sum)].find_pic_data_shezhi(config,data)
        return self.sum_names[self.xm_data + str(xc_sum)].find_pic_ex()

    def find_pic_click(self,config,data,click,xc_sum):  # 找图成功点击
        temp1 = self.find_pic(config,data,xc_sum)
        if temp1 == 1:
            self.dianji(click,1,2,xc_sum)
            return 1
        else:
            return 0

    def find_pic_click1(self,config,data,click,xc_sum):  # 找图失败点击
        temp1 = self.find_pic(config,data,xc_sum)
        if temp1 == 1:
            return 0
        else:
            self.dianji(click,1,2,xc_sum)
            return 1

    '''==================================================================================================='''

    def zikubd(self,data):  # 字库绑定
        for x in range(self.xc_sum_data):
            self.sum_names[self.xm_data + str(x)].SetDict(x,data[x])

    def dqziku(self,data):  # 当前字库选择
        if self.dqzk != data:
            for x in range(self.xc_sum_data):
                self.sum_names[self.xm_data + str(x)].UseDict(data)
            self.dqzk = data
            return 2
        else:
            return 1

    def find_word(self,data,xc_sum):  # 找字
        self.sum_names[self.xm_data + str(xc_sum)].find_data_shezhi(data)
        return self.sum_names[self.xm_data + str(xc_sum)].find_word()

    def find_word_click(self,data,click,xc_sum):  # 找字成功点击
        temp1 = self.find_word(data,xc_sum)
        if temp1 == 1:
            self.dianji(click, 1, 2, xc_sum)
            return 1
        else:
            return 0

    def find_word_click1(self,data,click,xc_sum):  # 找字失败点击
        temp1 = self.find_word(data,xc_sum)
        if temp1 == 1:
            return 0
        else:
            self.dianji(click, 1, 2, xc_sum)
            return 1

    def find_word_ex(self,data,xc_sum):  # 找字扩展
        self.sum_names[self.xm_data + str(xc_sum)].find_data_shezhi(data)
        return self.sum_names[self.xm_data + str(xc_sum)].find_word_ex()

    def find_word_ex1(self,data,xc_sum):  # 找字扩展1
        self.sum_names[self.xm_data + str(xc_sum)].find_data_shezhi(data)
        return self.sum_names[self.xm_data + str(xc_sum)].find_word_ex()

    def find_word_ex1_shujucl2(self,data,xc_sum):  # 找字扩展1:数据处理2
        self.sum_names[self.xm_data + str(xc_sum)].find_data_shezhi(data)
        temp1 = self.find_word_ex1(data,xc_sum)
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

    def find_word_sumzh(self, data: list, dizhi: list, sim: list, fangxian: int):
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

    def find_word_sumzh1(self, data: list, fangxian: int):
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
    def duoxianc(self,data):
        temp1 = locals()
        temp2 = []
        for x in range(len(data)):
            temp1["duoxc"+str(x)] = MyThread(data[x][0],data[x][1])
        for x in range(len(data)):
            temp1["duoxc"+str(x)].start()
        for x in range(len(data)):
            temp1["duoxc"+str(x)].join()
        for x in range(len(data)):
            temp2.append(temp1["duoxc"+str(x)].get_result())
        return temp2

    def duoxc_2(self,fun1,data1,fun2,data2):
        temp1 = MyThread(fun1,data1)
        temp2 = MyThread(fun2,data2)
        temp1.start()
        temp2.start()
        temp1.join()
        temp2.join()
        temp3 = [temp1.get_result(),temp2.get_result()]
        return temp3

    def duoxc_3(self,fun1,data1,fun2,data2,fun3,data3):
        temp1 = MyThread(fun1,data1)
        temp2 = MyThread(fun2,data2)
        temp3 = MyThread(fun3, data3)
        temp1.start()
        temp2.start()
        temp3.start()
        temp1.join()
        temp2.join()
        temp3.join()
        temp4 = [temp1.get_result(),temp2.get_result(),temp3.get_result()]
        return temp4

