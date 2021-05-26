import json
import pythoncom
from comtypes import client
import win32gui
import random
import time
import threading
import sys
import queue


class lw_obj:
    def __init__(self):
        pythoncom.CoInitialize()
        self.lw = client.CreateObject('lw.lwsoft3')
        self.hwnd = -1
        self.state = 0
        self.word_path_num = 0
        self.x = -1
        self.y = -1

    # 雷电模拟器绑定
    def leidianbang(self, data, mingzi=""):
        hwnd = win32gui.FindWindow("LDPlayerMainFrame", data)
        ch_hwnd = win32gui.FindWindowEx(hwnd, 0, "RenderWindow", "TheRender")
        self.hwnd = ch_hwnd
        print('句柄为：' + str(ch_hwnd))
        leidianbang_temp = self.lw.BindWindow(ch_hwnd, 5, 4, 4, 1, 0)
        if leidianbang_temp == 1:
            print(mingzi + "绑定成功")
            return 1
        else:
            print(mingzi + "绑定失败")
            return 0

    # 雷电模拟器解绑
    def jiebang(self):
        self.lw.ForceUnBindWindow(self.hwnd)

    # 鼠标后台点击
    def click(self, click_x, click_y, cast_x: str, cast_y: str):
        cast_x_temp = cast_x.find('|')
        cast_y_temp = cast_y.find('|')
        click_temp = 0
        try:
            if cast_x_temp == -1:
                cast_x_click = random.randint(int(click_x), int(click_x) + int(cast_x))
            else:
                cast_temp = cast_x.split('|')
                cast_x_click = random.randint(int(click_x) + int(cast_temp[0]), int(click_x) + int(cast_temp[1]))
        except:
            cast_x_click = 0
        try:
            if cast_y_temp == -1:
                cast_y_click = random.randint(int(click_y), int(click_y) + int(cast_y))
            else:
                cast_temp = cast_y.split('|')
                cast_y_click = random.randint(int(click_y) + int(cast_temp[0]), int(click_y) + int(cast_temp[1]))
        except:
            cast_y_click = 0
        if cast_x_click > 0 and cast_y_click > 0:
            self.lw.MoveTo(cast_x_click, cast_y_click)
            click_temp = self.lw.LeftClick()
        if click_temp > 0:
            return 1
        else:
            return 0

    '------------------------------------------------------------------------------------------------------------------'
    '找字'

    # 字库设置
    def setdict(self, data):
        for x in range(len(data)):
            self.lw.SetDict(x, data[x])

    # 选择字库
    def usedict(self, data: int):
        if self.word_path_num != data:
            self.word_path_num = data
            self.lw.UseDict(data)

    # 普通找字
    def find_word(self, coord: list, name, col, sim, back, time_out):
        time_process = 0
        while True:
            time_start = time.time()
            temp = self.lw.FindStr(coord[0], coord[1], coord[2], coord[3],
                                   name, col, sim, back)
            if temp == 1:
                self.x = self.lw.x
                self.y = self.lw.y
                return 1
            else:
                time_end = time.time()
                time_process = time_process + time_end - time_start
                if time_process > time_out or time_process == time_out:
                    self.x = -1
                    self.y = -1
                    return 0

    # 高级找字
    def find_wordex(self, coord: list, name, col, sim, back, time_out):
        time_process = 0
        while True:
            time_start = time.time()
            temp = self.lw.FindStrEx(coord[0], coord[1], coord[2], coord[3],
                                     name, col, sim, back)
            if len(temp) == 0:
                time_end = time.time()
                time_process = time_process + time_end - time_start
                if time_process > time_out or time_process == time_out:
                    self.x = -1
                    self.y = -1
                    return ""
            else:
                self.x = -1
                self.y = -1
                return temp

    '------------------------------------------------------------------------------------------------------------------'
    '找图'

    # 普通找图
    def find_pic(self, col_cast, coord: list, data, sim, time_out, click, x_cast, y_cast, delay_time):
        temp = self.lw.findpic(coord[0],
                               coord[1],
                               coord[2],
                               coord[3],
                               data,
                               col_cast, sim, 0, time_out, click, x_cast, y_cast,
                               delay_time)
        if temp == 1:
            self.x = self.lw.x
            self.y = self.lw.y
            return 1
        else:
            self.x = -1
            self.y = -1
            return 0

    # 高级找图
    def find_picex(self, col_cast, coord: list, data, sim, time_out, click, x_cast, y_cast, delay_time):
        temp = self.lw.findpic(coord[0],
                               coord[1],
                               coord[2],
                               coord[3],
                               data,
                               col_cast, sim, 0, time_out, click, x_cast, y_cast,
                               delay_time)
        if len(temp) == 0:
            self.x = -1
            self.y = -1
            return ""
        else:
            self.x = -1
            self.y = -1
            return temp

    '------------------------------------------------------------------------------------------------------------------'
    '找色'

    # 普通找色
    def find_col(self, coord: list, col, sim, dire, time_out):
        temp = self.lw.FindColor(coord[0], coord[1], coord[2], coord[3],
                                 col,
                                 sim,
                                 dire,
                                 time_out)
        return temp


class worker:
    def __init__(self, pic_path, pic_format, pic_col):
        self.skill = lw_obj()
        self.data = {"coord": [],
                     "word_name": '',
                     "pic_data": "",
                     "find_col": "",
                     "cast_col": "000000",
                     "sim": 1,
                     "time_out": 0,
                     "pic_click": 0,
                     "x_cast": 0,
                     "y_cast": 0,
                     "delay_time": 0,
                     "pic_path": pic_path,
                     "pic_format": pic_format,
                     "pic_col": pic_col,
                     "word_data_sum": 0,
                     "word_back": 0}
        #  状态变量
        self.state = 0
        self.x = -1
        self.y = -1
        self.ret_data = []
        self.ex_ret_data = {}

    # 窗口绑定
    def bangding(self, win_name, win_type):
        temp = 0
        if self.skill.hwnd != -1:
            temp = 1
            pass
        elif win_type == "leidian":
            temp = self.skill.leidianbang(win_name)
        return temp

    # 窗口解绑
    def jiebang(self):
        self.skill.jiebang()

    # 输入数据处理
    def data_handle_input(self, data: dict):
        for x in self.data.keys():
            if x == "pic_path" or x == "pic_format" or x == "pic_col":
                continue
            try:
                if x == "pic_data":
                    if data["pic_path"] != "" and data["pic_format"] != "":
                        self.data[str(x)] = str(data["pic_path"]) + str(data[str(x)]) + str(data["pic_format"])
                    elif data["pic_path"] != "":
                        self.data[str(x)] = str(data["pic_path"]) + str(data[str(x)]) + str(self.data["pic_format"])
                    elif data["pic_format"] != "":
                        self.data[str(x)] = str(self.data["pic_path"]) + str(data[str(x)]) + str(data["pic_format"])
                    else:
                        self.data[str(x)] = str(self.data["pic_path"]) + str(data[str(x)]) + str(
                            self.data["pic_format"])
                else:
                    self.data[str(x)] = data[str(x)]
            except:
                if str(x) == "coord":
                    self.data[str(x)] = []
                elif str(x) == "word_name":
                    self.data[str(x)] = ""
                elif str(x) == "pic_data":
                    self.data[str(x)] = ""
                elif str(x) == "find_col":
                    self.data[str(x)] = ""
                elif str(x) == "sim":
                    self.data[str(x)] = 1
                elif str(x) == "time_out":
                    self.data[str(x)] = 0
                elif str(x) == "pic_click":
                    self.data[str(x)] = 0
                elif str(x) == "x_cast":
                    self.data[str(x)] = 0
                elif str(x) == "y_cast":
                    self.data[str(x)] = 0
                elif str(x) == "delay_time":
                    self.data[str(x)] = 0
                elif str(x) == "word_data_sum":
                    self.data[str(x)] = 0
                elif str(x) == "cast_col":
                    self.data[str(x)] = "000000"

    # 输出数据处理
    def data_handle_output(self, data):
        if not isinstance(data, str):
            self.ret_data = []
            self.ex_ret_data = {}
        else:
            if len(data) == 0:
                self.ret_data = []
                self.ex_ret_data = {}
            else:
                if data.find("|") == -1:
                    temp = data.split(",")
                    self.ret_data.append(str(temp[1]) + "," + str(temp[2]))
                    self.ex_ret_data[str(temp[0])] = [str(temp[1]) + "," + str(temp[2])]
                else:
                    temp = data.split("|")
                    temp_sum = 0
                    for x in range(len(temp)):
                        temp_temp = temp[x].split(",")
                        if int(temp_temp[0]) != temp_sum:
                            temp_sum = int(temp_temp[0])
                            self.ret_data.append(str(temp_temp[1]) + "," + str(temp_temp[2]))
                            self.ex_ret_data[str(temp_temp[0])] = [str(temp_temp[1]) + "," + str(temp_temp[2])]
                        else:
                            self.ret_data.append(str(temp_temp[1]) + "," + str(temp_temp[2]))
                            self.ex_ret_data[str(temp_temp[0])].append(str(temp_temp[1]) + "," + str(temp_temp[2]))

    '''=============================================================================================================='''
    """找字功能"""

    # 字库绑定
    def setdict(self, data: list):
        self.skill.setdict(data)

    # 普通找字
    def find_word(self, data: dict):
        self.data_handle_input(data)
        self.skill.usedict(self.data["word_data_sum"])
        try:
            temp = self.skill.find_word(self.data["coord"], self.data["word_name"], self.data["cast_col"],
                                        self.data["sim"], self.data["word_back"], self.data["time_out"])
        except:
            temp = 0
            print("")
            print("===================================================================================================")
            print(self.data["word_data_sum"])
            print(self.data["coord"])
            print(self.data["word_name"])
            print(self.data["cast_col"])
            print(self.data["sim"])
            print(self.data["word_back"])
            print(self.data["time_out"])
            print("===================================================================================================")
            print("")
        if temp == 0:
            self.x = -1
            self.y = -1
            return 0
        else:
            self.x = self.skill.x
            self.y = self.skill.y
            return 1

    # 高级找字
    def find_wordex(self, data: dict):
        self.data_handle_input(data)
        self.skill.usedict(self.data["word_data_sum"])
        try:
            temp = self.skill.find_wordex(self.data["coord"], self.data["word_name"], self.data["cast_col"],
                                          self.data["sim"], self.data["word_back"], self.data["time_out"])
        except:
            temp = ""
            print("")
            print("===================================================================================================")
            print(self.data["word_data_sum"])
            print(self.data["coord"])
            print(self.data["word_name"])
            print(self.data["cast_col"])
            print(self.data["sim"])
            print(self.data["word_back"])
            print(self.data["time_out"])
            print("===================================================================================================")
            print("")
        self.data_handle_output(temp)
        if len(self.ret_data) == 0:
            return 0
        else:
            return 1

    '''=============================================================================================================='''
    """找图功能"""

    # 普通找图
    def find_pic(self, data: dict):
        self.data_handle_input(data)
        try:
            temp = self.skill.find_pic(self.data["pic_col"], self.data["coord"], self.data["pic_data"],
                                       self.data["sim"],
                                       self.data["time_out"], self.data["pic_click"], self.data["x_cast"],
                                       self.data["y_cast"], self.data["delay_time"])
        except:
            temp = 0
            print("")
            print("===================================================================================================")
            print(self.data["pic_col"])
            print(self.data["coord"])
            print(self.data["pic_data"])
            print(self.data["sim"])
            print(self.data["time_out"])
            print(self.data["pic_click"])
            print(self.data["x_cast"])
            print(self.data["y_cast"])
            print(self.data["delay_time"])
            print("===================================================================================================")
            print("")
        if temp == 1:
            self.x = self.skill.x
            self.y = self.skill.y
            return 1
        else:
            self.x = -1
            self.y = -1
            return 0

    # 高级找图
    def find_picex(self, data: dict):
        self.data_handle_input(data)
        try:
            temp = self.skill.find_picex(self.data["pic_col"], self.data["coord"], self.data["pic_data"],
                                         self.data["sim"],
                                         self.data["time_out"], self.data["pic_click"], self.data["x_cast"],
                                         self.data["y_cast"], self.data["delay_time"])
        except:
            temp = ""
            print("")
            print("===================================================================================================")
            print(self.data["pic_col"])
            print(self.data["coord"])
            print(self.data["pic_data"])
            print(self.data["sim"])
            print(self.data["time_out"])
            print(self.data["pic_click"])
            print(self.data["x_cast"])
            print(self.data["y_cast"])
            print(self.data["delay_time"])
            print("===================================================================================================")
            print("")
        self.data_handle_output(temp)
        if len(self.ret_data) == 0:
            return 0
        else:
            return 1


class Assign_tasks:
    def __init__(self, pic_path, pic_format, pic_col, word_path: list, worker_name):
        self.pic_path = pic_path
        self.pic_format = pic_format
        self.pic_col = pic_col
        self.word_path = word_path
        # 属性设置
        self.worker = {}
        self.worker_name = worker_name
        self.worker_sum = 0
        self.lock = threading.Lock()

    # 对象生成
    def worker_add(self, add_sum):
        for x in range(add_sum):
            self.worker[str(self.worker_name) + str(self.worker_sum) + str(x) + "1"] = worker(self.pic_path,
                                                                                              self.pic_format,
                                                                                              self.pic_col)
            self.worker[str(self.worker_name) + str(self.worker_sum) + str(x) + "1"].setdict(self.word_path)
        self.worker_sum = self.worker_sum + add_sum

    # 窗口绑定
    def worker_bangding(self, win_name, win_type):
        for x in self.worker.keys():
            if self.worker[str(x)].state == 0:
                temp = self.worker[str(x)].bangding(win_name, win_type)
                if temp == 0:
                    self.worker_jiebang()
                    sys.exit()

    # 窗口解绑
    def worker_jiebang(self):
        for x in self.worker.keys():
            temp = self.worker[str(x)].jiebang()

    # 乐玩对象状态查找更改
    def obj_find(self, data_type, obj_sum=0, obj_data=None, win_name=None, win_type=None):
        if obj_data is None:
            obj_data = []
        obj = []
        while True:
            self.lock.acquire()
            if data_type == "获取对象":
                for x in self.worker.keys():
                    if self.worker[str(x)].state == 0:
                        self.worker[str(x)].state = 1
                        obj.append(self.worker[str(x)])
                        if len(obj) == obj_sum:
                            self.lock.release()
                            return obj
            elif data_type == "回收对象":
                for x in obj_data:
                    x.state = 0
                self.lock.release()
                return True
            elif data_type == "新建对象":
                self.worker_add(obj_sum)
                self.worker_bangding(win_name, win_type)
                self.lock.release()
                return True
            elif data_type == "获取限量对象":
                for x in self.worker.keys():
                    if self.worker[str(x)].state == 0:
                        self.worker[str(x)].state = 1
                        obj.append(self.worker[str(x)])
                        if len(obj) == obj_sum:
                            self.lock.release()
                            return obj
                self.lock.release()
                return obj
            self.lock.release()
            while True:
                for x in self.worker.keys():
                    if self.worker[str(x)].state == 0:
                        break

    # 获取运行对象
    def obtain_obj(self, obj_sum):
        return self.obj_find("获取对象", obj_sum=obj_sum)

    # 获取限量运行对象
    def obtain_limit_obj(self, obj_sum):
        return self.obj_find("获取限量对象", obj_sum=obj_sum)

    # 回收运行对象
    def recovery_obj(self, obj_data: list):
        return self.obj_find("回收对象", obj_data=obj_data)

    # 新建运行对象
    def add_obj(self, obj_sum, win_name, win_type):
        return self.obj_find("新建对象", obj_sum=obj_sum, win_name=win_name, win_type=win_type)


class MyThread(threading.Thread):

    def __init__(self):
        super().__init__()
        self.result = None
        self.run_result = False
        self.func = None
        self.args = None
        self.kwargs = None
        self.run_state = 0
        self.bug = False
        self.stop = False
        self.event = threading.Event()  # 控制线程等待对象

    def mytask(self, fun, *args, **kwargs):
        self.func = fun
        self.args = args
        self.kwargs = kwargs
        self.event.set()  # 线程开始运行

    def Thread_stop(self):
        self.stop = True

    def run(self):
        self.event.clear()
        while True:
            self.event.wait()  # 阻塞运行
            if self.stop:
                break
            self.bug = False
            self.run_result = False
            try:
                self.result = self.func(*self.args, **self.kwargs)
                self.run_result = True
            except:
                self.bug = True
            self.event.clear()

    def get_result(self):
        try:
            for x in range(100):
                if self.run_result:
                    return self.result
                if self.bug:
                    print("出现bug了")
                    return None
                time.sleep(0.2)
            return None
        except Exception:
            return None


class ListThread:

    def __init__(self):
        self.thread = {}
        self.thread_sum = 0
        self.lock = threading.Lock()

    def add_thread(self, add_sum: int):
        for x in range(add_sum):
            self.thread[str(x + self.thread_sum + 1)] = MyThread()
            self.thread[str(x + self.thread_sum + 1)].run()
        self.thread_sum = self.thread_sum + add_sum

    def find_thread(self, data_tape, obj_sum=0, thread_obj=None):
        obj_data = []
        while True:
            self.lock.acquire()
            if data_tape == "获取对象":
                for x in self.thread.keys():
                    if self.thread[str(x)].run_state == 0:
                        self.thread[str(x)].run_state = 1
                        obj_data.append(self.thread[str(x)])
                        if len(obj_data) == obj_sum:
                            self.lock.release()
                            return obj_data
            if data_tape == "回收对象":
                for x in thread_obj:
                    x.run_state = 0
                self.lock.release()
                return True
            if data_tape == "新建对象":
                self.add_thread(obj_sum)
                self.lock.release()
                return True
            if data_tape == "获取限量对象":
                for x in self.thread.keys():
                    if self.thread[str(x)].run_state == 0:
                        self.thread[str(x)].run_state = 1
                        obj_data.append(self.thread[str(x)])
                        if len(obj_data) == obj_sum:
                            self.lock.release()
                            return obj_data
                self.lock.release()
                return obj_data
            while True:
                for x in self.thread.keys():
                    if self.thread[str(x)].run_state == 0:
                        break
                    time.sleep(0.2)

    # 获取运行对象
    def obtain_obj(self, obj_sum):
        return self.find_thread("获取对象", obj_sum=obj_sum)

    # 获取限量运行对象
    def obtain_limit_obj(self, obj_sum):
        return self.find_thread("获取限量对象", obj_sum=obj_sum)

    # 回收运行对象
    def recovery_obj(self, obj_data: list):
        return self.find_thread("回收对象", obj_data=obj_data)

    # 新建运行对象
    def add_obj(self, obj_sum):
        return self.find_thread("新建对象", obj_sum=obj_sum)


class RunPool:
    def __init__(self, in_data: dict, obj_sum, win_name, win_type):
        self.worker = Assign_tasks(in_data["pic_path"],
                                   in_data["pic_format"],
                                   in_data["pic_col"],
                                   in_data["word_path"],
                                   in_data["worker_name"])
        self.listthread = ListThread()
        self.woker_equi = ListThread()
        self.obj_add(obj_sum, win_name, win_type)

    def obj_add(self, add_sum, win_name, win_type):
        self.worker.add_obj(obj_sum=add_sum, win_name=win_name, win_type=win_type)
        self.woker_equi.add_obj(add_sum)
        if add_sum > 3:
            self.listthread(int(3))
        else:
            self.listthread(int(add_sum / 3))

    def worker_run(self, fun, args):
        res_temp = []
        fun_sum = len(args)
        fun_sum1 = 0
        while True:
            worker_obj = self.worker.obtain_limit_obj(fun_sum)
            worker_equi_obj = self.woker_equi.obtain_limit_obj(fun_sum)
            if len(worker_obj) > len(worker_equi_obj) != 0:
                for x in range(len(worker_equi_obj)):
                    worker_equi_obj[x].mytask(fun, worker_obj[x], args[fun_sum1])
                    fun_sum1 = fun_sum1 + 1
            elif len(worker_equi_obj) > len(worker_obj) != 0:
                for x in range(len(worker_obj)):
                    worker_equi_obj[x].mytask(fun, worker_obj[x], args[fun_sum1])
                    fun_sum1 = fun_sum1 + 1
            worker_equi_obj_temp = 0
            if len(worker_equi_obj) != 0 and len(worker_obj) != 0:
                while True:
                    if len(worker_equi_obj) > len(worker_obj):
                        if worker_equi_obj_temp == len(worker_equi_obj):
                            break
                        if worker_equi_obj[worker_equi_obj_temp].run_result:
                            if worker_equi_obj[worker_equi_obj_temp].get_result() is None:
                                temp = {"result": 0,
                                        "ret_data": worker_obj[worker_equi_obj_temp].ret_data,
                                        "ex_ret_data": worker_obj[worker_equi_obj_temp].ex_ret_data}
                            else:
                                temp = {"result": worker_equi_obj[worker_equi_obj_temp].get_result(),
                                        "ret_data": worker_obj[worker_equi_obj_temp].ret_data,
                                        "ex_ret_data": worker_obj[worker_equi_obj_temp].ex_ret_data}
                            res_temp.append(temp)
                            worker_equi_obj_temp = worker_equi_obj_temp + 1
                    else:
                        if worker_equi_obj_temp == len(worker_obj):
                            break
                        if worker_equi_obj[worker_equi_obj_temp].run_result:
                            if worker_equi_obj[worker_equi_obj_temp].get_result() is None:
                                temp = {"result": 0,
                                        "ret_data": worker_obj[worker_equi_obj_temp].ret_data,
                                        "ex_ret_data": worker_obj[worker_equi_obj_temp].ex_ret_data}
                            else:
                                temp = {"result": worker_equi_obj[worker_equi_obj_temp].get_result(),
                                        "ret_data": worker_obj[worker_equi_obj_temp].ret_data,
                                        "ex_ret_data": worker_obj[worker_equi_obj_temp].ex_ret_data}
                            res_temp.append(temp)
                            worker_equi_obj_temp = worker_equi_obj_temp + 1
            self.worker.recovery_obj(worker_obj)
            self.woker_equi.recovery_obj(worker_equi_obj)
            if len(res_temp) == fun_sum:
                return res_temp
   