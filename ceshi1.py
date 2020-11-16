from concurrent.futures import ThreadPoolExecutor
import threading
import time


# 定义一个准备作为线程任务的函数
def action(max1, yanchi):
    my_sum = 0
    for i in range(max1):
        print(threading.current_thread().name + '  ' + str(i))
        my_sum += i
    time.sleep(yanchi)
    return my_sum


# 创建一个包含2条线程的线程池
pool = ThreadPoolExecutor(max_workers=30)
# 向线程池提交一个task, 50会作为action()函数的参数
future1 = pool.submit(action, 50, 7)
# 向线程池再提交一个task, 100会作为action()函数的参数
future2 = pool.submit(action, 100, 1)
# 判断future1代表的任务是否结束
# print(future1.done())
time.sleep(3)
# 判断future2代表的任务是否结束
# print(future2.done())
# 查看future1代表的任务返回的结果
# print(future1.result())
# 查看future2代表的任务返回的结果
# print(future2.result())
a = [future1.result(), future2.result()]
print(a)
# 关闭线程池
pool.shutdown()
