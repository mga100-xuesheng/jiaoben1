import gongneng.gongnengzh
import gongneng.jiben


class GongNengdy:
    def __init__(self, mz_data, xm_data, xc_sum_data, pic_config):
        self.mz_data = mz_data
        self.xm_gn = gongneng.gongnengzh.FindCol(mz_data, xm_data, xc_sum_data, pic_config)

    def dxc_dingyi(self,data):  # 多线程对象直接定义
        self.xm_gn.sum_xiancheng1(data)

    def ldbangding(self):
        self.xm_gn.leidiandxcbd()

    def ldnamgding1(self,data):
        self.xm_gn.leidianbang(self.mz_data,data)

    def ldjiebang(self):
        self.xm_gn.jiebang("")

    def shujucl1(self,data):
        return self.xm_gn.shujuchuli1(data)

    def shujucl2(self,data):
        return self.xm_gn.shujuchuli2(data)

    def dianji(self,data,min_time,max_time,xc_sum):
        self.xm_gn.random_time(min_time,max_time)
        self.xm_gn.click(data,xc_sum)

    "--------------------------------------------------------------------"

    def find_pic(self,config,data,xc_sum):
        self.xm_gn.find_pic_data_shezhi(config,data)
        if xc_sum == "":
            xc_sum = 1
        return self.xm_gn.find_pic(xc_sum)

    def find_pic_ex(self,config,data,xc_sum):
        self.xm_gn.find_pic_data_shezhi(config, data)
        if xc_sum == "":
            xc_sum = 1
        return self.xm_gn.find_pic_ex(xc_sum)

    def find_pic_click(self,config,data,click,xc_sum):
        temp1 = self.find_pic(config,data,xc_sum)
        if temp1 == 1:
            self.xm_gn.random_time(1,2)
            self.xm_gn.click(click,xc_sum)
            return 1
        else:
            return -1

    def find_pic_click1(self,config,data,click,xc_sum):
        temp1 = self.find_pic(config,data,xc_sum)
        if temp1 == 1:
            return -1
        else:
            self.xm_gn.random_time(1,2)
            self.xm_gn.click(click,xc_sum)
            return 1

    "--------------------------------------------------------------------"

    def zikubd(self,data):
        for x in range(len(data)):
            for y in range(self.xm_gn.xc_data):
                self.xm_gn.sum_names[str(self.xm_gn.xm_data) + str(y + 1)].SetDict(x, data[x])

    def dqzifuku(self,data):
        if self.xm_gn.dqzifu_sum == data:
            return 1
        else:
            for x in range(self.xm_gn.xc_data):
                self.xm_gn.sum_names[str(self.xm_gn.xm_data) + str(x + 1)].UseDict(data)
            self.xm_gn.dqzifu_sum = data

    def find_word(self,data, xc_sum):
        self.xm_gn.find_data_shezhi(data)
        if xc_sum == "":
            xc_sum = 1
        return self.xm_gn.find_word(xc_sum)

    def find_word_click(self,data,click,xc_sum):
        temp1 = self.find_word(data,xc_sum)
        if temp1 == 1:
            self.xm_gn.random_time(1, 2)
            self.xm_gn.click(click, xc_sum)
            return 1
        else:
            return -1

    def find_word_click1(self,data,click,xc_sum):
        temp1 = self.find_word(data,xc_sum)
        if temp1 == 1:

            return -1
        else:
            self.xm_gn.random_time(1, 2)
            self.xm_gn.click(click, xc_sum)
            return 1

    def find_word_ex(self,data, xc_sum):
        self.xm_gn.find_data_shezhi(data)
        if xc_sum == "":
            xc_sum = 1
        return self.xm_gn.find_word_ex(xc_sum)

    def find_word_ex1(self,data, xc_sum):
        self.xm_gn.find_data_shezhi(data)
        if xc_sum == "":
            xc_sum = 1
        return self.xm_gn.find_word_ex1(xc_sum)

    def find_word_ex1_shujucl2(self,data, xc_sum):
        temp1 = self.find_word_ex1(data,xc_sum)
        if temp1[0] == 1:
            temp2 = self.xm_gn.shujuchuli2(temp1[1])
            return temp2
        else:
            return [0]

    def find_word_sum(self, data, find_sum, dizhi, sim: int, xc_sum):
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

    def find_word_sum1(self, data, find_sum, xc_sum):
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
        zifu1 = gongneng.jiben.MyThread(self.find_word_sum, (tuple(data[0]), 1, tuple(dizhi), sim[0], 1))
        zifu2 = gongneng.jiben.MyThread(self.find_word_sum, (data[1], 2, dizhi, sim[1], 2))
        zifu3 = gongneng.jiben.MyThread(self.find_word_sum, (data[2], 3, dizhi, sim[2], 3))
        zifu4 = gongneng.jiben.MyThread(self.find_word_sum, (data[3], 4, dizhi, sim[3], 4))
        zifu5 = gongneng.jiben.MyThread(self.find_word_sum, (data[4], 5, dizhi, sim[4], 5))
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
        zifu1 = gongneng.jiben.MyThread(self.find_word_sum, (data[5], 6, dizhi, sim[5], 1))
        zifu2 = gongneng.jiben.MyThread(self.find_word_sum, (data[6], 7, dizhi, sim[6], 2))
        zifu3 = gongneng.jiben.MyThread(self.find_word_sum, (data[7], 8, dizhi, sim[7], 3))
        zifu4 = gongneng.jiben.MyThread(self.find_word_sum, (data[8], 9, dizhi, sim[8], 4))
        zifu5 = gongneng.jiben.MyThread(self.find_word_sum, (data[9], 0, dizhi, sim[9], 5))
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
        zifu1 = gongneng.jiben.MyThread(self.find_word_sum1, (data[0], 1, 1))
        zifu2 = gongneng.jiben.MyThread(self.find_word_sum1, (data[1], 2, 2))
        zifu3 = gongneng.jiben.MyThread(self.find_word_sum1, (data[2], 3, 3))
        zifu4 = gongneng.jiben.MyThread(self.find_word_sum1, (data[3], 4, 4))
        zifu5 = gongneng.jiben.MyThread(self.find_word_sum1, (data[4], 5, 5))
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
        zifu1 = gongneng.jiben.MyThread(self.find_word_sum1, (data[5], 6, 1))
        zifu2 = gongneng.jiben.MyThread(self.find_word_sum1, (data[6], 7, 2))
        zifu3 = gongneng.jiben.MyThread(self.find_word_sum1, (data[7], 8, 3))
        zifu4 = gongneng.jiben.MyThread(self.find_word_sum1, (data[8], 9, 4))
        zifu5 = gongneng.jiben.MyThread(self.find_word_sum1, (data[9], 0, 5))
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

    "--------------------------------------------------------------------"
