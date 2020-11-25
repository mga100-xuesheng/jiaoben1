import threading


class MyThread(threading.Thread):

    def __init__(self, name):
        super().__init__(name)
        self.result = None
        self.name = name
        self.func: object
        self.args = ()
        self.keyword = {}
        self.event = threading.Event()
        self.event.clear()
        self.state = False

    def mytask(self, func, args, keyword=None):
        self.func = func
        self.args = args
        self.keyword = keyword
        self.event.set()

    def on_state(self):
        self.state = True

    def off_state(self):
        self.state = False

    def Thread_name(self):
        return self.name

    def run(self):
        while True:
            self.event.wait()
            if self.keyword is None:
                self.result = self.func(*self.args)
            else:
                self.result = self.func(*self.args, **self.keyword)
            if self.state is False:
                self.event.clear()

    def get_result(self):
        try:
            return self.result
        except Exception:
            return None


class ListThread:
    def __init__(self, limit_state, limit_num_add, thread_num=5):
        self.limit_state = limit_state
        self.limit_num_add = limit_num_add
        self.thread_num = thread_num
