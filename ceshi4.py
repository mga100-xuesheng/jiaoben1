import threading
from time import *


class MyThread(threading.Thread):

    def ceshi(self, data):
        print(data)

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
        self.result_state = False
        self.subscribe = False

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
            if self.stop is True:
                break
            self.event.wait()
            if self.state is False:
                self.event.clear()
            if self.stop is True:
                break
            self.run_state = True
            self.result_state_wait.clear()
            if self.keyword is None:
                self.result_state = False
                temp1 = self.func(*self.args)
                self.result_state = True
                self.result = temp1
            else:
                self.result_state = False
                temp1 = self.func(*self.args, **self.keyword)
                self.result_state = True
                sleep(0.2)
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
        for x in range(self.thread_num):
            self.listthread_add(x + 1)

    def listthread_add(self, thread_name_num):
        self.thread_list_obj[str(self.thread_name) + str(thread_name_num)] = MyThread(
            str(self.thread_name) + str(thread_name_num))
        self.thread_now_num = self.thread_now_num + 1

    def Theard_start_testing(self):
        for x in range(self.thread_now_num):
            if not self.thread_list_obj[str(self.thread_name) + str(x + 1)].run_whether_state:
                self.thread_list_obj[str(self.thread_name) + str(x + 1)].start()

    def findtheard(self):
        for x in range(self.thread_now_num):
            if not self.thread_list_obj[str(self.thread_name) + str(x + 1)].subscribe:
                self.thread_list_obj[str(self.thread_name) + str(x + 1)].on_theard_subscribe()
                return str(self.thread_name) + str(x + 1)

    # def task_allocation(self,data):

    def task_run(self, theard_run_data, run_data):
        self.Theard_start_testing()
        temp1 = []
        for x in range(len(run_data)):
            self.thread_list_obj[theard_run_data[x]].mytask(run_data[x][0], args=run_data[x][1])
        while True:
            for x in range(len(theard_run_data)):
                if self.thread_list_obj[theard_run_data[x]].result_state:
                    temp1.append(self.thread_list_obj[theard_run_data[x]].get_result())
                if len(temp1) == len(theard_run_data):
                    break

    def stop(self):
        for x in range(self.thread_num):
            self.thread_list_obj[str(self.thread_name) + str(x + 1)].Thread_stop()


temp11 = MyThread('1')
temp12 = MyThread('2')


def aaa(data):
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


temp11.start()
temp12.start()
temp11.mytask(aaa, args=(1,))
temp12.mytask(bbb, args=())
# temp1.on_state()
temp11.on_join()
temp12.on_join()
print(temp11.get_result())
print(temp12.get_result())
temp11.mytask(bbb, args=())
temp12.mytask(aaa, args=(1,))
temp11.on_join()
print(temp11.get_result())
print(temp12.get_result())
temp11.Thread_stop()
temp12.Thread_stop()
