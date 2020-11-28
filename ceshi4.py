import threading
from time import *


class MyThreadEx(threading.Thread):

    def __init__(self, name1):
        super().__init__()
        self.result = None
        self.name1 = name1
        self.func: object
        self.args = ()
        self.keyword = {}
        self.event = threading.Event()
        self.result_state_wait = threading.Event()  # 返回等待
        self.event.clear()
        self.state = False  # 线程是否循环执行任务（默认非循环执行任务）
        self.run_state = False  # 线程任务是否在运行（默认没有运行）
        self.run_whether_state = False  # 线程是否就绪（默认非就绪）
        self.stop = False  # 是否停止线程（默认不停止）
        self.result_state = False  # 线程是否发送返回值
        self.subscribe = False  # 线程是否无任务

    def on_theard_subscribe(self):
        self.subscribe = True

    def on_join(self):
        while True:
            if self.result_state is True:
                break

    def mytask(self, func, args, keyword=None):
        self.func = func
        self.args = args
        self.keyword = keyword
        self.event.set()

    def on_state(self):
        self.state = True

    def off_state(self):
        self.state = False

    def Thread_stop(self):
        self.stop = True
        self.result_state_wait.set()
        self.event.set()

    def run(self):
        self.run_whether_state = True
        while True:
            self.event.wait()
            if self.state is False:
                self.event.clear()
            if self.stop is True:
                break
            self.run_state = True
            self.result_state_wait.clear()
            self.result_state = False
            if self.keyword is None:
                temp1 = self.func(*self.args)
            else:
                temp1 = self.func(*self.args, **self.keyword)
            self.result_state = True
            self.result = temp1
            self.result_state_wait.wait()
            if self.state is False:
                self.run_state = False
        self.run_whether_state = False

    def get_result(self):
        try:
            self.result_state = None
            self.result_state_wait.set()
            self.subscribe = False
            return self.result
        except Exception:
            return None


class ListThread:
    def __init__(self, limit_state: bool, limit_num_add: int, thread_name: str, thread_num=5):
        self.limit_state = limit_state
        self.limit_num_add = limit_num_add
        self.thread_num = thread_num
        self.thread_now_num = 0
        self.thread_name = thread_name
        self.thread_list_obj = {}
        self.lock = threading.Lock()
        self.batch_listthread_add(thread_num)

    def batch_listthread_add(self, num):
        for x in range(num):
            self.thread_now_num = self.thread_now_num + 1
            self.thread_list_obj[str(self.thread_name) + str(self.thread_now_num)] = MyThreadEx(
                str(self.thread_name) + str(self.thread_now_num))
            self.thread_list_obj[str(self.thread_name) + str(self.thread_now_num)].start()

    def Theard_start_testing(self):
        for x in range(self.thread_now_num):
            if not self.thread_list_obj[str(self.thread_name) + str(x + 1)].run_whether_state:
                self.thread_list_obj[str(self.thread_name) + str(x + 1)].start()

    @staticmethod
    def task_state_set(data):
        temp = []
        for x in range(len(data)):
            temp.append([data[x], 0])
        return temp

    @staticmethod
    def task_tate_detection(data):
        for x in range(len(data)):
            if data[x][1] == 0:
                data[x][1] = 1
                return data[x]
        return False

    def findtheard(self):
        self.lock.acquire()
        for x in range(self.thread_now_num):
            if not self.thread_list_obj[str(self.thread_name) + str(x + 1)].subscribe:
                self.thread_list_obj[str(self.thread_name) + str(x + 1)].on_theard_subscribe()
                self.lock.release()
                return str(self.thread_name) + str(x + 1)
        if self.limit_state == True and self.thread_now_num < self.thread_num + self.limit_num_add:
            self.batch_listthread_add(1)
        self.lock.release()
        return False

    def findtheard_state(self):
        temp = 0
        for x in range(self.thread_now_num):
            if not self.thread_list_obj[str(self.thread_name) + str(x + 1)].subscribe:
                temp = temp + 1
        return temp

    def many_task(self, data):
        temp1 = self.task_state_set(data)
        temp2 = []
        while True:
            temp3 = []
            while True:
                temp4 = self.findtheard()
                if temp4 is not False:
                    temp5 = self.task_tate_detection(temp1)
                    if temp5 is False:
                        break
                    temp3.append(temp4)
                    if len(temp5[0]) == 2:
                        self.thread_list_obj[temp4].mytask(temp5[0][0], temp5[0][1])
                    else:
                        self.thread_list_obj[temp4].mytask(temp5[0][0], temp5[0][1], temp5[0][2])
                else:
                    break
            for x in range(len(temp3)):
                temp6 = self.theard_name_get_result(temp3[x])
                temp2.append(temp6)
                if len(temp2) == len(temp1):
                    return temp2

    def sing_task(self, data):
        while True:
            temp1 = self.findtheard()
            if temp1 is not False:
                if len(data[0]) == 2:
                    self.thread_list_obj[temp1].mytask(data[0][0], data[0][1])
                else:
                    self.thread_list_obj[temp1].mytask(data[0][0], data[0][1], data[0][2])
            return self.theard_name_get_result(temp1)

    def theard_name_join(self, name):
        self.thread_list_obj[name].on_join()

    def theard_name_get_result(self, name):
        self.theard_name_join(name)
        return self.thread_list_obj[name].get_result()

    def task_run(self, data):
        temp1 = self.findtheard()
        if len(data) == 1:
            self.thread_list_obj[temp1].mytask(self.sing_task, (data,))
        else:
            self.thread_list_obj[temp1].mytask(self.many_task, (data,))
        return temp1

    def stop(self):
        for x in range(self.thread_now_num):
            self.thread_list_obj[str(self.thread_name) + str(x + 1)].Thread_stop()


temp11 = ListThread(True, 10, 'ceshi')


def aaa():
    for x in range(10):
        print('aaa')
        print(x + 1)
        sleep(1)
    return 666


def bbb():
    for x in range(20):
        print("bbb")
        print(x + 1)
        sleep(1)
    return 777


def ccc(data):
    for x in range(10):
        print('ccc:' + str(x))
    return data


def ddd():
    for x in range(10):
        print('ddd:' + str(x))


# temp12 = [[aaa, ()], [bbb, ()], [ddd, ()]]
# temp13 = temp11.task_run(temp12)
# temp14 = [[aaa, ()], [ccc, ('ceshiyixia',)], [ddd, ()]]
# temp15 = temp11.task_run(temp14)
# print(temp11.theard_name_get_result(temp15))
# print(temp11.theard_name_get_result(temp13))
temp12 = [[aaa, ()]]
temp13 = temp11.task_run(temp12)
print(temp11.theard_name_get_result(temp13))
print(temp11.thread_now_num)
temp11.stop()
