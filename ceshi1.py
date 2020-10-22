from jichu.jichu import RiZhi1
# a = "测试测试测试：成功"
# print(a.find("："))
# if a[a.index("：")+1:] == "成功":
#     print("成功")
# else:
#     print("失败")

# temp1 = RiZhi1("C:\\Users\\29412\\Desktop\\ceshiwenjian\\")
# # temp2 = temp1.utf_8_duqu("rizhi.txt")
# # print(temp2)
# # for x in range(len(temp2)):
# #     if x+2 > len(temp2):
# #         break
# #     else:
# #         x += 1
# #     if temp2[x][temp2[x].find("：")+1:] == "已做":
# #         print("成功")
# #     else:
# #         print("失败")
# #     if temp2[x].find("家园") != -1:
# #         if temp2[x][temp2[x].find("：") + 1:] == "已做":
# #             print("测试成功")
# #     if temp2[x].find("任务") != -1:
# #         if temp2[x][temp2[x].find("：") + 1:] == "未做":
# #             print("测试1")
# #         else:
# #             print('测试2')
# temp5 = []
# # aa = "家园领取体力：已做"
# # bb = '任务领取体力：已做'
# # cc = '探索：未做'
# # dd = '地下城：未做'
# # temp1.utf_8_xieru("rizhi.txt",[aa,bb,cc,dd])
# temp2 = temp1.utf_8_duqu("rizhi.txt")
# print(temp2)
# for x in temp2:
#     if x.find("：") != -1:
#         print(x[x.find('：')+1:])
#         temp3 = x[x.find('：')+1:]
#         temp4 = x[:x.find('：')+1] + "nihao1"
#         print(temp4)
#         temp5.append(temp4)
# temp1.utf_8_xieru("rizhi.txt",temp5)
# temp2 = temp1.utf_8_duqu("rizhi.txt")
# print(temp2)


def xiugai(dizhi:str,mingzi:str,xiangmu: str, data: str):
    temp1 = RiZhi1(dizhi)
    temp2 = temp1.utf_8_duqu(mingzi)
    print(temp2)
    temp4 = []
    temp5 = 0
    for x in temp2:
        if x.find(xiangmu) != -1:
            temp3 = x[:x.find('：') + 1] + data
            temp5 = 1
        else:
            temp3 = x
        if temp5 == 1:
            temp4.append(temp3)
            temp5 = 0
        else:
            if x.find("-") == -1:
                temp4.append(x)
    print(temp4)
    temp1.utf_8_xieru(mingzi,temp4)
    # print(temp4)


xiugai("C:\\Users\\29412\\Desktop\\ceshiwenjian\\","rizhi.txt","家园","已做")
