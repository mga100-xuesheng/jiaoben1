import time
import threading


def funA(fn):
    # 定义一个嵌套函数
    def say(*args, **kwargs):
        fn(*args, **kwargs)

    return say


@funA
def funB(arc):
    print("C语言中文网：", arc)


@funA
def other_funB(name, arc, ceshi):
    print(name, arc, ceshi)


# def bbbb():
#     print(3333)
#
#
# aaaa = {'a': 6, 'b': 7, 'c': 8, 'd': 7, 'e': bbbb}
# for x in aaaa.keys():
#     if x == "d":
#         print(aaaa[x])
#     elif x == "e":
#         aaaa[x]()
#     print(isinstance(x, str))

#
# def ceshi1(fn):
#     def ceshi2(*args, **kwargs):
#         fn(*args, **kwargs)
#         print(args)
#         print(kwargs)
#         ceshi3(args, kwargs)
#         print('98764')
#         print(kwargs)
#         return 1
#
#     def ceshi3(args, kwargs):
#         kwargs['c'] = 5
#         print(time.sleep(5))
#         print('ceshi3')
#         print(args)
#         return 2
#
#     return ceshi2


class cqw:
    def __init__(self):
        self.qwer = 'qwer'
        self.lock = threading.Lock()

    def ceshi1(fn):
        def ceshi2(self, *args, **kwargs):
            print(args)
            print(kwargs)
            ceshi3(args, kwargs)
            print('98764')
            print(kwargs)
            test = fn(*args, **kwargs)
            return test

        def ceshi3(args, kwargs):
            kwargs['c'] = 5
            # print(time.sleep(5))
            print('ceshi3')
            print(args)
            return 2

        return ceshi2

    @ceshi1
    def asd(self, aa=None, *args, **kwargs):
        print(self.qwer)
        self.lock.acquire()
        self.qwer = 'rewq'
        self.lock.release()
        print(self.qwer)
        time.sleep(5)
        print('aa:  ' + str(aa))
        print('kwargs:  ')
        print(kwargs)
        print('asd                                  asd')


a = cqw()
# b = threading.Thread(target=a.asd,args=(a,1),kwargs={'c':11})
# c = threading.Thread(target=a.asd,args=(a,1),kwargs={'c':11})
# b.start()
# c.start()
a.asd(a, aa='asdasd', cc=13)
