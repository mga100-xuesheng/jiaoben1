class Journal:
    def __init__(self, path):
        self.path = path

    def utf_8_duqu(self, name):
        temp1 = open(self.path + name, "r", encoding='utf-8')
        temp2 = []
        temp1_data = temp1.readlines()
        for x in range(len(temp1_data)):
            temp1_data1 = temp1_data[x].strip('\n')
            temp2.append(temp1_data1)
        temp1.close()
        return temp2

    def utf_8_xieru(self, xieru_time: str, name, data):
        temp1 = [xieru_time + "\n"]
        # print(data)
        for x in range(len(data)):
            data[x] = str(data[x]) + "\n"
        temp1 = temp1 + data
        temp2 = open(self.path + name, "w", encoding='utf-8')
        temp2.writelines(temp1)
        temp2.close()
        return 1
