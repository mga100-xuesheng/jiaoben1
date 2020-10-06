import gongneng.jiben
import time
import random


class FindWord(gongneng.jiben.JiBen):
    def find_data_shezhi(self, data):
        self.find_word_data_coord = data[0]
        self.find_word_data_name = data[1]
        self.find_word_data_col = data[2]
        self.find_word_data_sim = data[3]
        self.find_word_data_back = data[4]
        self.find_word_data_time = data[5]
        self.find_word_data_x = -1
        self.find_word_data_y = -1

    def find_word(self,xc_sum):
        find_word_temp1 = 1
        time_process = 0
        while find_word_temp1 == 1:
            time_start = time.time()
            find_word_temp2 = self.sum_names[self.xm_data + str(xc_sum)].FindStr(self.find_word_data_coord[0],
                                                                                 self.find_word_data_coord[1],
                                                                                 self.find_word_data_coord[2],
                                                                                 self.find_word_data_coord[3],
                                                                                 self.find_word_data_name,
                                                                                 self.find_word_data_col,
                                                                                 self.find_word_data_sim,
                                                                                 self.find_word_data_back)
            if find_word_temp2 == 1:
                self.find_word_data_x = self.sum_names[self.xm_data + str(self.xc_sum)].x
                self.find_word_data_y = self.sum_names[self.xm_data + str(self.xc_sum)].y
                return 1
            else:
                time_end = time.time()
                time_process = time_process + time_end - time_start
                if time_process > self.find_word_data_time or time_process == self.find_word_data_time:
                    self.find_word_data_x = -1
                    self.find_word_data_y = -1
                    return 0

    def find_word_ex(self,xc_sum):
        find_word_ex_temp1 = 1
        ex_time_process = 0
        while find_word_ex_temp1 == 1:
            ex_time_start = time.time()
            find_word_ex_temp2 = self.sum_names[self.xm_data + str(xc_sum)].FindStrEx(self.find_word_data_coord[0],
                                                                                      self.find_word_data_coord[1],
                                                                                      self.find_word_data_coord[2],
                                                                                      self.find_word_data_coord[3],
                                                                                      self.find_word_data_name,
                                                                                      self.find_word_data_col,
                                                                                      self.find_word_data_sim,
                                                                                      self.find_word_data_back)
            if find_word_ex_temp2 is not None:
                find_word_ex_temp3 = find_word_ex_temp2.find("|")
            else:
                find_word_ex_temp3 = -1
            if find_word_ex_temp3 == -1 and find_word_ex_temp2 is not None:
                find_word_ex_temp2 = find_word_ex_temp2.split(",")
                return [1, find_word_ex_temp2]
            if find_word_ex_temp3 > -1:
                find_word_ex_temp2 = find_word_ex_temp2.split("|")
                for xx in range(len(find_word_ex_temp2)):
                    find_word_ex_temp2[xx] = find_word_ex_temp2[xx].split(",")
                return [1, find_word_ex_temp2]
            else:
                ex_time_end = time.time()
                ex_time_process = ex_time_process + ex_time_end - ex_time_start
                if ex_time_process == self.find_word_data_time or ex_time_process > self.find_word_data_time:
                    self.find_word_data_x = -1
                    self.find_word_data_y = -1
                    return [0]

    def find_word_ex1(self,xc_sum):
        find_word_ex_temp1 = 1
        ex_time_process = 0
        while find_word_ex_temp1 == 1:
            ex_time_start = time.time()
            find_word_ex_temp2 = self.sum_names[self.xm_data + str(xc_sum)].FindStrEx(self.find_word_data_coord[0],
                                                                                      self.find_word_data_coord[1],
                                                                                      self.find_word_data_coord[2],
                                                                                      self.find_word_data_coord[3],
                                                                                      self.find_word_data_name,
                                                                                      self.find_word_data_col,
                                                                                      self.find_word_data_sim,
                                                                                      self.find_word_data_back)
            if find_word_ex_temp2 is not None:
                return [1,find_word_ex_temp2]
            else:
                ex_time_end = time.time()
                ex_time_process = ex_time_process + ex_time_end - ex_time_start
                if ex_time_process == self.find_word_data_time or ex_time_process > self.find_word_data_time:
                    self.find_word_data_x = -1
                    self.find_word_data_y = -1
                    return [0]


class FindPic(FindWord):
    def find_pic_data_shezhi(self, config, data):
        self.find_pic_data_path = config[0]
        self.find_pic_data_format = config[1]
        self.find_pic_data_col_cast = config[2]
        if self.find_pic_data_path == "":
            self.find_pic_data_path = self.pic_path
        if self.find_pic_data_format == "":
            self.find_pic_data_format = self.pic_format
        if self.find_pic_data_col_cast == "":
            self.find_pic_data_col_cast = self.pic_col
        self.find_pic_data_coord = data[0]
        self.find_pic_data_name = data[1][0]
        self.find_pic_data_sum = data[1][1]
        self.find_pic_data_sim = data[2][0]
        self.find_pic_data_click = data[2][1]
        self.find_pic_data_x_cast = data[2][2]
        if isinstance(self.find_pic_data_x_cast, int) is True:
            self.find_pic_data_x_cast = int(
                random.randint(0 - self.find_pic_data_x_cast, self.find_pic_data_x_cast))
        if isinstance(self.find_pic_data_x_cast, str) is True:
            self.find_pic_data_x_cast_temp = self.find_pic_data_x_cast.split("q")
            self.find_pic_data_x_cast = int(
                random.randint(int(self.find_pic_data_x_cast_temp[0]), int(self.find_pic_data_x_cast_temp[1])))
        self.find_pic_data_y_cast = data[2][3]
        if isinstance(self.find_pic_data_y_cast, int) is True:
            self.find_pic_data_y_cast = int(
                random.randint(0 - self.find_pic_data_y_cast, self.find_pic_data_y_cast))
        if isinstance(self.find_pic_data_y_cast, str) is True:
            self.find_pic_data_y_cast_temp = self.find_pic_data_y_cast.split("q")
            self.find_pic_data_y_cast = int(
                random.randint(int(self.find_pic_data_y_cast_temp[0]), int(self.find_pic_data_y_cast_temp[1])))
        self.find_pic_data_time_out = data[3][0] * 1000
        self.find_pic_data_elay_time = data[3][1]
        self.find_pic_data_Delay_time = self.find_pic_data_Delay_time * 1000
        self.find_pic_data_x = -1
        self.find_pic_data_y = -1

    def find_pic(self,xc_sum):
        if xc_sum == "":
            xc_sum = 1
        find_pic_temp1 = 0
        for z in range(int(self.find_pic_data_sum)):
            find_pic_temp1 = self.sum_names[self.xm_data + str(xc_sum)].findpic(self.find_pic_data_coord[0],
                                                                                self.find_pic_data_coord[1],
                                                                                self.find_pic_data_coord[2],
                                                                                self.find_pic_data_coord[3],
                                                                                self.find_pic_data_path +
                                                                                self.find_pic_data_name +
                                                                                str(z + 1) +
                                                                                self.find_pic_data_format,
                                                                                self.find_pic_data_col_cast,
                                                                                self.find_pic_data_sim, 0,
                                                                                self.find_pic_data_time_out,
                                                                                self.find_pic_data_click,
                                                                                self.find_pic_data_x_cast,
                                                                                self.find_pic_data_y_cast,
                                                                                self.find_pic_data_Delay_time)
            if find_pic_temp1 == 1:
                self.find_pic_data_x = self.sum_names[self.xm_data + str(self.xc_sum)].x
                self.find_pic_data_y = self.sum_names[self.xm_data + str(self.xc_sum)].y
                return 1
        if find_pic_temp1 == 0:
            return 0

    def find_pic_ex(self,xc_sum):
        if xc_sum == "":
            xc_sum = 1
        find_pic_ex_temp1 = 0
        find_pic_ex_temp2 = ""
        for x in range(self.find_pic_data_sum):
            find_pic_ex_temp2 = find_pic_ex_temp2 + str(
                self.find_pic_data_path + self.find_pic_data_name + str(x + 1) + self.find_pic_data_format + "|")
        find_pic_ex_temp2 = find_pic_ex_temp2.strip('|')
        find_pic_ex_temp1 = self.sum_names[self.xm_data + str(xc_sum)].FindPicEx(self.find_pic_data_coord[0],
                                                                                 self.find_pic_data_coord[1],
                                                                                 self.find_pic_data_coord[2],
                                                                                 self.find_pic_data_coord[3],
                                                                                 find_pic_ex_temp2,
                                                                                 self.find_pic_data_col_cast,
                                                                                 self.find_pic_data_sim, 0,
                                                                                 self.find_pic_data_time_out,
                                                                                 self.find_pic_data_click,
                                                                                 self.find_pic_data_x_cast,
                                                                                 self.find_pic_data_y_cast,
                                                                                 self.find_pic_data_Delay_time)
        return find_pic_ex_temp1


class FindCol(FindPic):
    def find_col_data_chuli(self,data,time_out):
        self.find_col_data_coord = data[0]
        self.find_col_data_find_color = data[1]
        self.find_col_data_sim = data[2]
        self.find_col_data_dire = data[3]
        if len(data) > 4:
            self.find_col_data_offset_color = data[4]
        else:
            self.find_col_data_offset_color = ""
        self.find_col_data_time_out = int(time_out) * 1000
        self.find_col_data_x = -1
        self.find_col_data_y = -1

    def find_col1(self,xc_sum):
        if xc_sum == "":
            xc_sum = 1
        temp1 = self.sum_names[self.xm_data + str(xc_sum)].FindColor(self.find_col_data_coord[0],
                                                                     self.find_col_data_coord[1],
                                                                     self.find_col_data_coord[2]
                                                                     , self.find_col_data_coord[3],
                                                                     self.find_col_data_find_color,
                                                                     self.find_col_data_sim,
                                                                     self.find_col_data_dire,
                                                                     self.find_col_data_time_out)
        if temp1 == 1:
            return 1
        else:
            return 0

    def find_multi_color1(self, xc_sum):
        if xc_sum == "":
            xc_sum = 1
        temp1 = self.sum_names[self.xm_data + str(xc_sum)].FindMultiColor(self.find_col_data_coord[0],
                                                                          self.find_col_data_coord[1],
                                                                          self.find_col_data_coord[2]
                                                                          , self.find_col_data_coord[3],
                                                                          self.find_col_data_find_color,
                                                                          self.find_col_data_offset_color,
                                                                          self.find_col_data_sim,
                                                                          self.find_col_data_dire
                                                                          , self.find_col_data_time_out)
        if temp1 == 1:
            return 1
        else:
            return 0

    def find_col2(self, xc_sum):
        if xc_sum == "":
            xc_sum = 1
        temp1 = self.sum_names[self.xm_data + str(xc_sum)].FindColorEx(self.find_col_data_coord[0],
                                                                       self.find_col_data_coord[1],
                                                                       self.find_col_data_coord[2]
                                                                       , self.find_col_data_coord[3],
                                                                       self.find_col_data_find_color,
                                                                       self.find_col_data_sim,
                                                                       self.find_col_data_dire,
                                                                       self.find_col_data_time_out)
        return temp1

    def find_multi_color2(self,xc_sum):
        if xc_sum == "":
            xc_sum = 1
        temp1 = self.sum_names[self.xm_data + str(xc_sum)].FindMultiColor(self.find_col_data_coord[0],
                                                                          self.find_col_data_coord[1],
                                                                          self.find_col_data_coord[2]
                                                                          , self.find_col_data_coord[3],
                                                                          self.find_col_data_find_color,
                                                                          self.find_col_data_offset_color,
                                                                          self.find_col_data_sim,
                                                                          self.find_col_data_dire
                                                                          , self.find_col_data_time_out)
        return temp1
