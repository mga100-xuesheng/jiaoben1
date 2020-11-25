import threading
from time import *


class MyThread(threading.Thread):

    def __init__(self, name):
        super().__init__(name)
        self.result = None
        self.name = name
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
        self.run()

    def mytask(self, func, args, keyword=None):
        self.func = func
        self.args = args
        self.keyword = keyword
        self.event.set()

    def on_state(self):
        self.state = True

    def off_state(self):
        self.state = False

    def Thread_run_state(self):
        return self.run_state

    def Thread_name(self):
        return self.name

    def Thread_stop(self):
        self.stop = True
        self.event.set()

    def run(self):
        self.run_whether_state = True
        while True:
            self.event.wait()
            if self.stop:
                break
            self.run_state = True
            if self.keyword is None:
                self.result_state_wait.clear()
                self.result_state = False
                temp1 = self.func(*self.args)
                self.result_state = True
                self.result_state_wait.wait()
                sleep(0.2)
                self.result = temp1
            else:
                self.result_state_wait.clear()
                self.result_state = False
                temp1 = self.func(*self.args, **self.keyword)
                self.result_state = True
                self.result_state_wait.wait()
                sleep(0.2)
                self.result = temp1
            if self.state is False:
                self.event.clear()
                self.run_state = False
        self.run_whether_state = False

    def get_result(self):
        try:
            self.result_state = None
            self.result_state_wait.set()
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

    def find_thread(self, find_num):
        self.lock.acquire()
        while True:
            for x in range(self.thread_now_num):
                if not self.thread_list_obj[str(self.thread_name) + str(x)].run_state():
                    self.lock.release()
                    return str(self.thread_name) + str(x)

    def stop(self):
        for x in range(self.thread_num):
            self.thread_list_obj[str(self.thread_name) + str(x + 1)].Thread_stop()
