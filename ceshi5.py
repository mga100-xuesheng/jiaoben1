# def serialize_json(name):
#     data = 'user_name=123123&password=412412&power_id=0&user_name=214124&password=1241241&power_id=0'
#     data = data.split('&')
#     # print(data)
#     for x in range(len(data)):
#         data[x] = data[x].split('=')
#     # print(data)
#     data_temp1 = []
#     data_temp2 = []
#     for x in range(len(data)):
#         data_temp2.append(data[x])
#         if data[x][0] == name:
#             data_temp1.append(data_temp2)
#             data_temp2 = []
#     data = data_temp1
#     data_temp1 = []
#     data_temp2 = []
#     data_temp3 = []
#     for x in range(len(data)):
#         for y in range(len(data[x])):
#             data_temp1.append(data[x][y][0])
#             data_temp2.append(data[x][y][1])
#             if data[x][y][0] == name:
#                 data_temp3.append(zip(data_temp1, data_temp2))
#                 data_temp1 = []
#                 data_temp2 = []
#     data = []
#     for x in range(len(data_temp3)):
#         data.append(dict(data_temp3[x]))
#     return data
#
#
# # data = [{'ceshi': 0, 'ceshi1': 1}, {'1ceshi': 0, '1ceshi1': 1}]
# #
# # print(data[0]['ceshi'])
#
# # print(serialize_json('power_id'))
# # \d 匹配一个数字字符。等价于 [0-9]
# # \D 匹配一个非数字字符。等价于 [^0-9]
#
# def is_chinese(string):
#     """
#     检查整个字符串是否包含中文
#     :param string: 需要检查的字符串
#     :return: bool
#     """
#     for ch in string:
#         if u'\u4e00' <= ch <= u'\u9fff':
#             return True
#
#     return False
#
#
# # ret1 = is_chinese("测试数据")
# # print(ret1)
# #
# # ret2 = is_chinese("mga123")
# # print(ret2)
#
#
# def ceshi(fn):
#     def ceshi1(guolv):
#         print('ceshi1')
#         fn(guolv)
#         return 123
#
#     return ceshi1
#
#
# def ceshi5(fcm):
#     def ceshi3(fn):
#         def ceshi4(quest):
#             if fcm == 123:
#                 print('fcm:' + str(fcm))
#             else:
#                 print('fcm:' + str(98756431))
#             print('fn:' + str(fn))
#             print('quest:' + str(quest))
#             fn(quest)
#
#         return ceshi4
#
#     return ceshi3
#
#
# @ceshi5('2')
# def ceshi2(ceshi21):
#     print('ceshi')
#     print(ceshi21)
#
#
# import hashlib
# import base64
#
# str = "123"
# md5 = hashlib.md5()
# password = str.encode(encoding='utf-8')
# md5.update(password)
# sta_md5 = md5.hexdigest()
#
#
# def encryption_base64(data: str):
#     return base64.b64encode(data.encode('utf-8'))
#
#
# # print('nihao')
# # print(encryption_base64('nihao'))
# # print(encryption_base64('nihao'))
# aaa = encryption_base64('nihao')
# aaa = aaa.decode('utf-8')
# # print(aaa)
#
# bbb = '456'
# ccc = [['1223'], ['456'], ['123123'], ['3424234']]
# print(bbb in ccc)
# font = xlwt.Font()
# 为样式创建字体
# 字体类型：比如宋体、仿宋也可以是汉仪瘦金书繁 font.name = name
# 设置字体颜色 font.colour_index = color
# 字体大小 font.height = height
# 定义格式 style.font = font return style if __name__ == '__main__':
# 创建工作簿,并指定写入的格式 f = xlwt.Workbook(encoding='utf8') # 创建工作簿
# 创建sheet，并指定可以重复写入数据的情况.设置行高度 sheet1 = f.add_sheet(u'colour', cell_overwrite_ok=False)
# 控制行的位置 column = 0; row = 0
# 生成第一行 for i in range(0, 100):
# 参数对应：行，列，值，字体样式(可以没有) sheet1.write(column, row, i, setStyle('Times New Roman', 400, i, False))
# 这里主要为了控制输入每行十个内容。为了查看 row = row + 1 if row % 10 ==0: column = column + 1 row = 0
# f.save(r'E:\xlwtExCEL.xls') # 保存文档
#
# import time
#
# time_process = 0
# for x in range(5):
#     time_start = time.time()
#     time.sleep(2)
#     time_end = time.time()
#     time_process = time_process + time_end - time_start
#     print(time_process)
# print(time_process > 10)
import os

print(os.path.join(os.path.dirname(__file__), 'ceshi1.py'))
