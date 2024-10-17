# -*- coding: utf-8 -*-
"""
Created on Mon Oct 14 20:00:14 2024

@author: zhouqi
"""
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 14 19:47:06 2024

@author: zhouqi
"""
#from pywebio import start_server




from pywebio.output import put_text, put_table, popup
from pywebio.input import TEXT, input_group
import random
import tkinter.messagebox
import math
import tkinter
import numpy as np
from pywebio.input import input, FLOAT, SELECT, NUMBER, radio
class Calculator:
    # 界面布局方法
    def __init__(self):
        # 创建主界面，并且保存到成员属性中
        self.root = tkinter.Tk()
        self.root.minsize(280, 450)
        self.root.maxsize(280, 470)
        self.root.title('软件工程对错错队作业.0')
        # 设置显式面板的变量
        self.result = tkinter.StringVar()
        self.result.set(0)
        # 设置一个全局变量  运算数字和f符号的列表
        self.lists = []
        # 添加一个用于判断是否按下运算符号的标志
        self.ispresssign = False
        # 界面布局
        self.menus()
        self.layout()
        self.root.mainloop()

    # 计算器菜单界面摆放
    def menus(self):
        # 添加菜单
        # 创建总菜单
        allmenu = tkinter.Menu(self.root)
        # 添加子菜单
        filemenu = tkinter.Menu(allmenu, tearoff=0)
        # 添加选项卡
        filemenu.add_command(
            label='标准型(T)            Alt+1', command=self.myfunc)
        filemenu.add_command(
            label='科学型(S)            Alt+2', command=self.myfunc)
        filemenu.add_command(
            label='程序员(P)            Alt+3', command=self.myfunc)
        filemenu.add_command(label='统计信息(A)        Alt+4', command=self.myfunc)
        # 添加分割线
        filemenu.add_separator()
        # 添加选项卡
        filemenu.add_command(label='历史记录(Y)      Ctrl+H', command=self.myfunc)
        filemenu.add_command(label='数字分组(I)', command=self.myfunc)
        # 添加分割线
        filemenu.add_separator()
        # 添加选项卡
        filemenu.add_command(
            label='基本(B)             Ctrl+F4', command=self.myfunc)
        filemenu.add_command(label='单位转换(U)      Ctrl+U', command=self.myfunc)
        filemenu.add_command(label='日期计算(D)      Ctrl+E', command=self.myfunc)
        menu1 = tkinter.Menu(filemenu, tearoff=0)
        menu1.add_command(label='抵押(M)', command=self.myfunc)
        menu1.add_command(label='汽车租赁(V)', command=self.myfunc)
        menu1.add_command(label='油耗(mpg)(F)', command=self.myfunc)
        menu1.add_command(label='油耗(l/100km)(U)', command=self.myfunc)
        filemenu.add_cascade(label='工作表(W)', menu=menu1)
        allmenu.add_cascade(label='查看(V)', menu=filemenu)

        # 添加子菜单2
        editmenu = tkinter.Menu(allmenu, tearoff=0)
        # 添加选项卡
        editmenu.add_command(label='复制(C)         Ctrl+C', command=self.myfunc)
        editmenu.add_command(label='粘贴(V)         Ctrl+V', command=self.myfunc)
        # 添加分割线
        editmenu.add_separator()
        # 添加选项卡
        menu2 = tkinter.Menu(filemenu, tearoff=0)
        menu2.add_command(label='复制历史记录(I)', command=self.myfunc)
        menu2.add_command(
            label='编辑(E)                      F2', command=self.myfunc)
        menu2.add_command(label='取消编辑(N)            Esc', command=self.myfunc)
        menu2.add_command(label='清除(L)    Ctrl+Shift+D', command=self.myfunc)
        editmenu.add_cascade(label='历史记录(H)', menu=menu2)
        allmenu.add_cascade(label='编辑(E)', menu=editmenu)

        # 添加子菜单3
        helpmenu = tkinter.Menu(allmenu, tearoff=0)
        # 添加选项卡
        helpmenu.add_command(label='查看帮助(V)       F1', command=self.myfunc)
        # 添加分割线
        helpmenu.add_separator()
        # 添加选项卡
        helpmenu.add_command(label='关于计算器(A)', command=self.myfunc)
        allmenu.add_cascade(label='帮助(H)', menu=helpmenu)

        self.root.config(menu=allmenu)

    # 计算器主界面摆放
    def layout(self):
        # 显示屏
        result = tkinter.StringVar()
        result.set(0)
        show_label = tkinter.Label(self.root, bd=3, bg='white', font=(
            '宋体', 30), anchor='e', textvariable=self.result)
        show_label.place(x=5, y=20, width=270, height=70)
        # 功能按钮MC
        button_mc = tkinter.Button(self.root, text='MC', command=self.wait)
        button_mc.place(x=5, y=95, width=50, height=50)
        # 功能按钮MR
        button_mr = tkinter.Button(self.root, text='MR', command=self.wait)
        button_mr.place(x=60, y=95, width=50, height=50)
        # 功能按钮MS
        button_ms = tkinter.Button(self.root, text='MS', command=self.wait)
        button_ms.place(x=115, y=95, width=50, height=50)
        # 功能按钮M+
        button_mjia = tkinter.Button(self.root, text='M+', command=self.wait)
        button_mjia.place(x=170, y=95, width=50, height=50)
        # 功能按钮M-
        button_mjian = tkinter.Button(self.root, text='M-', command=self.wait)
        button_mjian.place(x=225, y=95, width=50, height=50)
        # 功能按钮←
        button_zuo = tkinter.Button(self.root, text='←', command=self.dele_one)
        button_zuo.place(x=5, y=150, width=50, height=50)
        # 功能按钮CE
        button_ce = tkinter.Button(
            self.root, text='CE', command=lambda: self.result.set(0))
        button_ce.place(x=60, y=150, width=50, height=50)
        # 功能按钮C
        button_c = tkinter.Button(self.root, text='C', command=self.sweeppress)
        button_c.place(x=115, y=150, width=50, height=50)
        # 功能按钮+
        button_zf = tkinter.Button(self.root, text='<-', command=self.zf)
        button_zf.place(x=170, y=150, width=50, height=50)
        # 功能按钮√
        button_kpf = tkinter.Button(self.root, text='√', command=self.kpf)
        button_kpf.place(x=225, y=150, width=50, height=50)
        # 数字按钮7
        button_7 = tkinter.Button(
            self.root, text='7', command=lambda: self.pressnum('7'))
        button_7.place(x=5, y=205, width=50, height=50)
        # 数字按钮8
        button_8 = tkinter.Button(
            self.root, text='8', command=lambda: self.pressnum('8'))
        button_8.place(x=60, y=205, width=50, height=50)
        # 数字按钮9
        button_9 = tkinter.Button(
            self.root, text='9', command=lambda: self.pressnum('9'))
        button_9.place(x=115, y=205, width=50, height=50)
        # 功能按钮/
        button_division = tkinter.Button(
            self.root, text='/', command=lambda: self.presscalculate('/'))
        button_division.place(x=170, y=205, width=50, height=50)
        # 功能按钮%
        button_remainder = tkinter.Button(
            self.root, text='//', command=lambda: self.presscalculate('//'))
        button_remainder.place(x=225, y=205, width=50, height=50)
        # 数字按钮4
        button_4 = tkinter.Button(
            self.root, text='4', command=lambda: self.pressnum('4'))
        button_4.place(x=5, y=260, width=50, height=50)
        # 数字按钮5
        button_5 = tkinter.Button(
            self.root, text='5', command=lambda: self.pressnum('5'))
        button_5.place(x=60, y=260, width=50, height=50)
        # 数字按钮6
        button_6 = tkinter.Button(
            self.root, text='6', command=lambda: self.pressnum('6'))
        button_6.place(x=115, y=260, width=50, height=50)
        # 功能按钮*
        button_multiplication = tkinter.Button(
            self.root, text='*', command=lambda: self.presscalculate('*'))
        button_multiplication.place(x=170, y=260, width=50, height=50)
        # 功能按钮1/x
        button_reciprocal = tkinter.Button(
            self.root, text='1/x', command=self.ds)
        button_reciprocal.place(x=225, y=260, width=50, height=50)
        # 数字按钮1
        button_1 = tkinter.Button(
            self.root, text='1', command=lambda: self.pressnum('1'))
        button_1.place(x=5, y=315, width=50, height=50)
        # 数字按钮2
        button_2 = tkinter.Button(
            self.root, text='2', command=lambda: self.pressnum('2'))
        button_2.place(x=60, y=315, width=50, height=50)
        # 数字按钮3
        button_3 = tkinter.Button(
            self.root, text='3', command=lambda: self.pressnum('3'))
        button_3.place(x=115, y=315, width=50, height=50)
        # 功能按钮-
        button_subtraction = tkinter.Button(
            self.root, text='-', command=lambda: self.presscalculate('-'))
        button_subtraction.place(x=170, y=315, width=50, height=50)
        # 功能按钮=
        button_equal = tkinter.Button(
            self.root, text='=', command=lambda: self.pressequal())
        button_equal.place(x=225, y=315, width=50, height=105)
        # 数字按钮0
        button_0 = tkinter.Button(
            self.root, text='0', command=lambda: self.pressnum('0'))
        button_0.place(x=5, y=370, width=105, height=50)
        # 功能按钮.
        button_point = tkinter.Button(
            self.root, text='.', command=lambda: self.pressnum('.'))
        button_point.place(x=115, y=370, width=50, height=50)
        # 功能按钮+
        button_plus = tkinter.Button(
            self.root, text='+', command=lambda: self.presscalculate('+'))
        button_plus.place(x=170, y=370, width=50, height=50)

    # 计算器菜单功能
    def myfunc(self):
        tkinter.messagebox.showinfo('', '菜单只是装饰而已～')

    # 数字方法
    def pressnum(self, num):
        # 全局化变量
        # 判断是否按下了运算符号
        if self.ispresssign == False:
            pass
        else:
            self.result.set(0)
            # 重置运算符号的状态
            self.ispresssign = False
        if num == '.':
            num = '0.'
        # 获取面板中的原有数字
        oldnum = self.result.get()
        # 判断界面数字是否为0
        if oldnum == '0':
            self.result.set(num)
        else:
            # 连接上新按下的数字
            newnum = oldnum + num

            # 将按下的数字写到面板中
            self.result.set(newnum)

    # 运算函数
    def presscalculate(self, sign):
        # 保存已经按下的数字和运算符号
        # 获取界面数字
        num = self.result.get()
        self.lists.append(num)
        # 保存按下的操作符号
        self.lists.append(sign)
        # 设置运算符号为按下状态
        self.ispresssign = True

    # 获取运算结果
    def pressequal(self):
        # 获取所有的列表中的内容（之前的数字和操作）
        # 获取当前界面上的数字
        curnum = self.result.get()
        # 将当前界面的数字存入列表
        self.lists.append(curnum)
        # 将列表转化为字符串
        calculatestr = ''.join(self.lists)
        # 使用eval执行字符串中的运算即可
        endnum = eval(calculatestr)
        # 将运算结果显示在界面中
        self.result.set(str(endnum)[:10])
        if self.lists != 0:
            self.ispresssign = True
        # 清空运算列表
        self.lists.clear()

    # 暂未开发说明
    def wait(self):
        tkinter.messagebox.showinfo('', '版本的更新。。')

    # ←按键功能
    def dele_one(self):
        if self.result.get() == '' or self.result.get() == '0':
            self.result.set('0')
            return
        else:
            num = len(self.result.get())
            if num > 1:
                strnum = self.result.get()
                strnum = strnum[0:num - 1]
                self.result.set(strnum)
            else:
                self.result.set('0')

    # +-按键功能
    def zf(self):
        strnum = self.result.get()
        if strnum[0] == '-':
            self.result.set(strnum[1:])
        elif strnum[0] != '-' and strnum != '0':
            self.result.set('-' + strnum)

    # 1/x按键功能
    def ds(self):
        dsnum = 1 / int(self.result.get())
        self.result.set(str(dsnum)[:10])
        if self.lists != 0:
            self.ispresssign = True
        # 清空运算列表
        self.lists.clear()

    # C按键功能
    def sweeppress(self):
        self.lists.clear()
        self.result.set(0)

    # √按键功能
    def kpf(self):
        strnum = float(self.result.get())
        endnum = math.sqrt(strnum)
        if str(endnum)[-1] == '0':
            self.result.set(str(endnum)[:-2])
        else:
            self.result.set(str(endnum)[:10])
        if self.lists != 0:
            self.ispresssign = True
        # 清空运算列表
        self.lists.clear()


def bmi():
    height = input("请输入您的身高(cm)：", type=FLOAT)
    weight = input("请输入您的体重(kg)：", type=FLOAT)

    BMI = weight / (height / 100) ** 2

    top_status = [(14.9, '极瘦'), (18.4, '偏瘦'),
                  (22.9, '正常'), (27.5, '过重'),
                  (40.0, '肥胖'), (float('inf'), '非常肥胖')]

    for top, status in top_status:
        if BMI <= top:
            put_text('您的 BMI 值: %.1f，身体状态：%s' % (BMI, status))
            break


def stransg():
    lis = [['成绩', '学分', '绩点']]
    n = input("请输入您的科目数：", type=NUMBER)
    nown = 1
    scores = 0
    cres = 0
    while nown < n+1:
        s = input("请输入您的成绩：", type=FLOAT)
        c = input("请输入您的学分：", type=FLOAT)
        if s < 0 or s > 100:
            popup("Error!")
        elif s >= 0 and s < 60:
            g = 0
        elif s >= 60 and s <= 63:
            g = 1.0
        elif s >= 64 and s <= 67:
            g = 1.7
        elif s >= 68 and s <= 71:
            g = 2.0
        elif s >= 72 and s <= 74:
            g = 2.3
        elif s >= 75 and s <= 77:
            g = 2.7
        elif s >= 78 and s <= 81:
            g = 3.0
        elif s >= 82 and s <= 84:
            g = 3.3
        elif s >= 85 and s <= 89:
            g = 3.7
        elif s >= 90 and s <= 100:
            g = 4.0
        nown += 1
        put_text("你的课程成绩为：%.1f，学分为：%.1f，绩点为：%.1f" % (s, c, g))
        lis.append([s, c, g])
        scores += g*c
        cres += c
    # if __name__ == '__main__':
    #start_server(l, port=19003, auto_open_webbrowser=False)
    put_table(lis)


def gpa():
    lis = [['成绩', '学分', '绩点']]
    n = input("请输入您的科目数：", type=NUMBER)
    nown = 1
    scores = 0
    cres = 0
    while nown < n+1:
        s = input("请输入您的成绩：", type=FLOAT)
        c = input("请输入您的学分：", type=FLOAT)
        if s < 0 or s > 100:
            popup("Error!")
        elif s >= 0 and s < 60:
            g = 0
        elif s >= 60 and s <= 63:
            g = 1.0
        elif s >= 64 and s <= 67:
            g = 1.7
        elif s >= 68 and s <= 71:
            g = 2.0
        elif s >= 72 and s <= 74:
            g = 2.3
        elif s >= 75 and s <= 77:
            g = 2.7
        elif s >= 78 and s <= 81:
            g = 3.0
        elif s >= 82 and s <= 84:
            g = 3.3
        elif s >= 85 and s <= 89:
            g = 3.7
        elif s >= 90 and s <= 100:
            g = 4.0
        nown += 1
        put_text("你的课程成绩为：%.1f，学分为：%.1f，绩点为：%.1f" % (s, c, g))
        lis.append([s, c, g])
        scores += g*c
        cres += c
    # if __name__ == '__main__':
    #start_server(l, port=19003, auto_open_webbrowser=False)
    put_table(lis)
    gpa = scores/cres
    put_text("您的均绩为：%.2f" % (gpa))


def pe():
    a = input("请输入BMI成绩：", type=FLOAT)
    b = input("请输入50米跑成绩：", type=FLOAT)
    c = input("请输入耐力跑（男生1000/女生800）成绩：", type=FLOAT)
    d = input("请输入肺活量成绩：", type=FLOAT)
    e = input("请输入立定跳远成绩：", type=FLOAT)
    f = input("请输入坐位体前屈成绩：", type=FLOAT)
    g = input("请输入引体向上／仰卧起坐成绩：", type=FLOAT)
    weights = {'a': 0.15, 'b': 0.20, 'c': 0.20,
               'd': 0.15, 'e': 0.10, 'f': 0.10, 'g': 0.10}
    weighted_sum = a*weights['a']+b*weights['b']+c*weights['c'] + \
        d*weights['d']+e*weights['e']+f*weights['f']+g*weights['d']
    put_text('体育分数为： %.2f' % (weighted_sum))


def dressrecommendation():
    temp = input("请输入今日气温：", type=FLOAT)
    put_text("今日气温为：%.2f度" % temp)
    humidity = input("请输入今日湿度：", type=FLOAT)
    put_text("今日湿度为：%.2f" % humidity)
    weather = radio("请选择今日天气：", ['雨', '无雨'])
    put_text("今日天气为：%s" % weather)
    wind_speed = input("请输入今日风速：", type=FLOAT)
    put_text("今日风速为：%.2f" % wind_speed)
    if temp >= 30:
        put_text("今天非常热，建议穿短袖和短裤")
    elif temp >= 20 and temp < 30:
        if humidity >= 70:
            put_text("今天很潮湿，建议穿轻便的透气衣服和短裤")
        elif humidity >= 50 and humidity < 70:
            put_text("今天湿度适中，建议穿轻便的透气衣服和长裤")
        else:
            put_text("今天干燥，建议穿衬衫和长裤")
    elif temp >= 10 and temp < 20:
        if weather == '雨':
            put_text("今天有雨，建议穿防水外套和长裤")
        else:
            put_text("今天比较凉爽，建议穿长袖衬衫和长裤")
    else:
        put_text("今天非常冷，建议穿厚外套和长裤")
    if wind_speed >= 10:
        put_text("今天有大风，建议搭配围巾和帽子")
    else:
        put_text("今天风力适中，无需特别搭配")


def distance():
    list1 = [[10000, 780, 400], [780, 10000, 370], [400, 370, 10000], [160, 650, 270], [290, 460, 130], [340, 600, 360], [
        580, 540, 300], [690, 560, 380], [670, 470, 340], [570, 690, 420], [520, 410, 130], [570, 280, 150], [1000, 670, 630]]
    list2 = ['一、二教/国定梯教/教技', '武东梯教/三教', '科研大楼', '1号楼/2号楼/南三宿舍', '北3/南4/北4宿舍',
             '5号楼/6号楼宿舍', '7号楼/8号楼宿舍', '9-11号楼宿舍', '19号楼', '20号楼', '静思园宿舍', '宁远楼宿舍', '武川宿舍']
    list3 = ['一、二教/国定梯教/教技', '武东梯教/三教', '科研大楼']
    put_text("1（一、二教/国定梯教/教技）\n2（武东梯教/三教）\n3（科研大楼）\n4（1号楼/2号楼/南三宿舍）\n5（北3/南4/北4宿舍）\n6（5号楼/6号楼宿舍）\n7（7号楼/8号楼宿舍）\n8（9-11号楼宿舍）\n9（19号楼）\n10（20号楼）\n11（静思园宿舍）\n12（宁远楼宿舍）\n13（武川宿舍）")
    StartingPoint = radio(
        "请选择您的起点", [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13])
    put_text("您的起点为：%s" % (list2[StartingPoint-1]))
    EndingPoint = radio("请输入您的终点：", [1, 2, 3])
    put_text("您的终点为：%s" % (list3[EndingPoint-1]))
    put_text("您从起点到终点的距离为%d米" % (list1[StartingPoint-1][EndingPoint-1]))

def wayrecom():
    list1 = [[10000,780,400],[780,10000,370],[400,370,10000],[160,650,270],[290,460,130],[340,600,360],[580,540,300],[690,560,380],[670,470,340],[570,690,420],[520,410,130],[570,280,150],[1000,670,630]]
    list2 = ['一、二教/国定梯教/教技','武东梯教/三教','科研大楼','1号楼/2号楼/南三宿舍','北3/南4/北4宿舍','5号楼/6号楼宿舍','7号楼/8号楼宿舍','9-11号楼宿舍','19号楼','20号楼','静思园宿舍','宁远楼宿舍','武川宿舍']
    list3 = ['一、二教/国定梯教/教技','武东梯教/三教','科研大楼']
    put_text("1（一、二教/国定梯教/教技）\n2（武东梯教/三教）\n3（科研大楼）\n4（1号楼/2号楼/南三宿舍）\n5（北3/南4/北4宿舍）\n6（5号楼/6号楼宿舍）\n7（7号楼/8号楼宿舍）\n8（9-11号楼宿舍）\n9（19号楼）\n10（20号楼）\n11（静思园宿舍）\n12（宁远楼宿舍）\n13（武川宿舍）")
    StartingPoint = radio("请选择您的起点",[1,2,3,4,5,6,7,8,9,10,11,12,13])
    put_text("您的起点为：%s"%(list2[StartingPoint-1]))
    EndingPoint = radio("请输入您的终点：",[1,2,3])
    put_text("您的终点为：%s"%(list3[EndingPoint-1]))
    distance  = list1[StartingPoint-1][EndingPoint-1]
    put_text("您从起点到终点的距离为%d米"%(distance))
    time_rest = input("请输入您剩下的上课时间：（单位：分钟）",type = FLOAT)
    put_text("您还剩下%.2f分钟"%(time_rest))
    level1 = input("请输入您所在的楼层：",type = NUMBER)
    level2 = input("请输入您的上课楼层：",type = NUMBER)
    put_text("您从%d楼出发"%level1)
    put_text("您要去%d楼上课"%level2)
    start_time = (level1-1)*15
    v_onfoot = 1
    v_bybike = 2
    onfoottime1 = distance/v_onfoot
    bybiketime1 = distance/v_bybike
    elevatorway = random.normalvariate(12,1)
    walkway = 15*(level2-1)
    onfoot_elevatorway_time = (onfoottime1 + elevatorway +start_time)/60
    onfoot_walkway_time = (onfoottime1 + walkway + start_time)/60
    bybike_elevatorway_time = (bybiketime1 + elevatorway + start_time)/60
    bybike_walkway_time = (bybiketime1 + walkway + start_time)/60
    if onfoot_elevatorway_time < time_rest:
        if onfoot_walkway_time < time_rest:
            if bybike_elevatorway_time < time_rest:
                if bybike_walkway_time < time_rest:
                    put_text("时间充足，可自行选择出行方式~")
                else:
                    put_text("骑车/步行上课均可，建议不要乘坐电梯~")
            else:
                if bybike_walkway_time < time_rest:
                    put_text("骑车/步行上课均可，建议不要步行上楼~")
                else:
                    put_text("您走路太快了！骑车都赶不上~")
        else:
            put_text("建议骑车，如果步行，建议乘坐电梯上楼，否则可能会迟到~")
    else:
        if onfoot_walkway_time < time_rest:
            put_text("建议骑车，如果步行，建议步行上楼，否则可能会迟到哦~")
        else:
            if bybike_elevatorway_time < time_rest:
                if bybike_walkway_time < time_rest:
                    put_text("建议骑车，走路会迟到哦~")
                else:
                    put_text("建议骑车并且乘坐电梯上课，否则可能会迟到哦！")
            else:
                if bybike_walkway_time < time_rest:
                    put_text("建议骑车并且步行上楼，否则可能会迟到~")
                else:
                    put_text("放弃吧，无论怎么办你都会迟到。。。")
def trianglefunc():
    n = radio("请选择您需要计算的三角函数：",['sin','cos','tan','asin','acos','atan'])
    put_text("您所选择的函数类型为%s"%(n))
    x = input("请输入自变量x的值：",type = FLOAT)
    put_text("x的值为%.2f"%(x))
    if n == 'sin':
        put_text("sinx的值为%.2f"%(math.sin(x)))
    if n == 'cos':
        put_text("cosx的值为%.2f"%(math.cos(x)))
    if n == 'tan':
        put_text("tanx的值为%.2f"%(math.tan(x)))
    if n == 'asin':
        put_text("asinx的值为%.2f"%(math.ssin(x)))
    if n == 'acos':
        put_text("acosx的值为%.2f"%(math.acos(x)))
    if n == 'atan':
        put_text("atanx的值为%.2f"%(math.atan(x)))
def lg():
    x = input("请输入底数：",type = FLOAT)
    put_text("您输入的底数值为：%.2f"%(x))
    y = input("请输入真数：",type = FLOAT)
    put_text("您输入的真数值为：%.2f"%(y))
    put_text("您所需计算的对数值为:%.2f"%(math.log(y,x)))
def exp():
    x = input("请输入自变量：",type = FLOAT)
    put_text("您输入的自变量值为：%.2f"%(x))
    y = radio("请输入你所需要计算的函数：",['e的x次方',"普通指数函数"])
    put_text("您所需要计算的函数为：%s"%(y))
    if y == 'e的x次方':
        put_text("e的%.2f次方为%.2f"%(x,math.pow(x,y)))
    else:
        z = input("请输入底数：",type = FLOAT)
        put_text("您输入的底数值为：%.2f"%(z))
        put_text("%.2f的%.2f次方为%.2f"%(z,x,math.pow(z,x)))
def advancedfun():
    n = radio("请选择您需要计算的函数：",['三角函数','对数函数','指数函数'])
    if n == '三角函数':
        trianglefunc()
    if n == "对数函数":
        lg()
    if n == "指数函数":
        exp()
while 1:
    #f = input("请输入您需要的功能：",type = FLOAT)
    # popup("请输入您所需要的功能：\n输入1\n输入2\n输入3")
    f = radio("请输入您需要的功能：", ['基础计算器', '进阶函数计算（三角函数、对数函数、指数函数）','bmi值计算',
              '成绩转换为绩点', '绩点计算', '体测成绩计算', '上学穿搭推荐', '上课距离计算','上课出行方式推荐'])
    if f == '基础计算器':
        myCalculator = Calculator()
    if f == 'bmi值计算':
        bmi()
    if f == '绩点计算':
        gpa()
    if f == '体测成绩计算':
        pe()
    if f == '上学穿搭推荐':
        dressrecommendation()
    if f == '成绩转换为绩点':
        stransg()
    if f == '上课距离计算':
        distance()
    if f == '上课出行方式推荐':
        wayrecom()
    if f == '进阶函数计算（三角函数、对数函数、指数函数）':
        advancedfun()