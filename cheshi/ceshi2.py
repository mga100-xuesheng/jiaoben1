import win32gui


def leidianbang(data, mingzi=""):  # 雷电模拟器绑定
    hwnd = win32gui.FindWindow("Qt5QWindowIcon", data)
    print(hwnd)
    ch_hwnd = win32gui.FindWindowEx(hwnd, 0, "Qt5QWindowIcon", "MainWindowWindow")
    print(ch_hwnd)
    ch_hwnd1 = win32gui.FindWindowEx(ch_hwnd, 0, "Qt5QWindowIcon", "CenterWidgetWindow")
    print(ch_hwnd1)
    ch_hwnd2 = win32gui.FindWindowEx(ch_hwnd1, 0, "Qt5QWindowIcon", "RenderWindowWindow")
    print(ch_hwnd2)
    print('句柄为：' + str(ch_hwnd2))


def get_child_windows(parent):
    """
    获得parent的所有子窗口句柄
     返回子窗口句柄列表
     """
    if not parent:
        return
    hwndChildList = []
    win32gui.EnumChildWindows(parent, lambda hwnd, param: param.append(hwnd), hwndChildList)
    return hwndChildList


def find_Windows(father_litle, father_clsname, title, clsname=''):
    hwnd = win32gui.FindWindow(father_clsname, father_litle)
    if hwnd != 0:
        temp1 = get_child_windows(hwnd)
        for x in range(len(temp1)):
            temp1_title = win32gui.GetWindowText(temp1[x])
            if clsname != '':
                temp1_clsname = win32gui.GetClassName(temp1[x])
                if temp1_title == title and temp1_clsname == clsname:
                    return temp1[x]
            else:
                if temp1_title == title:
                    return temp1[x]

    return 0


# aaa = find_Windows('四叶草', 'Qt5QWindowIcon', 'RenderWindowWindow')
# print('句柄是:  ' + str(aaa))
#
# aaa = find_Windows('公主连结国服', 'LDPlayerMainFrame', 'TheRender')
# print('句柄是:  ' + str(aaa))


def bangding(father_litle):
    temp1 = find_Windows(father_litle, 'Qt5QWindowIcon', 'RenderWindowWindow')
    if temp1 != 0:
        return temp1
    temp1 = find_Windows(father_litle, 'LDPlayerMainFrame', 'TheRender')
    if temp1 != 0:
        return temp1
    return -1


print(bangding('公主连结国服'))
