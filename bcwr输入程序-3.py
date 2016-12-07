# -*- coding: utf-8 -*-
"""
Created on Sat Dec 26 10:34:37 2015

@author: zhanggaoyang
"""
#所有数字均需写成浮点数，不能出现整数，出现整数会导致除法运算出错！为了保证在python2和python3中均可运行，需要保证除法均用带小数的数字！
import sys
versionNumber = sys.version_info.major
if versionNumber == 2:
    import sys                          # 1
    reload(sys)                         # 2
    sys.setdefaultencoding('utf-8')     # 3，用于防止编码写入文件出错

from breezypythongui import EasyFrame
from breezypythongui import DISABLED
import numpy as np


class bcwr_input(EasyFrame):
    """Application window for the bcwr_input(桥上无缝线路检算输入程序)."""
 
    def __init__(self):
        """Sets up the window and the widgets."""
        EasyFrame.__init__(self, title = 'bcwr.IN')

        #定义起始的行号，方便改变界面控件
        hh = 0
        # 第二十三行
        # Label and field for the 荷载类型
        self.addLabel(text = "荷载类型",
                      row = hh, column = 0)
        self.hezai_1 = self.addTextArea("1为中活载，2为ZK活载，3为其它类型的活载；每线上荷载分布大小，单位：kN/m及不同荷载分布作用长度：单位m。\n2,125.0,6.4,64.0,394.4,0.0,0.0", 
                                    row = hh, column = 1,
                                    columnspan = 5,
                                    width = 140, height = 2)
        # 第二十四行
        # Label and field for the 荷载入桥类型
        self.addLabel(text = "荷载入桥类型",
                      row = hh+1, column = 0, foreground = "red")
        self.hezai_2 = self.addTextArea("1为从左入桥，2为从右入桥。\n1,320.0", 
                                    row = hh+1, column = 1,
                                    columnspan = 5,
                                    width = 140, height = 2)
        # 第二十五行
        # Label and field for the 断轨参数
        self.addLabel(text = "断轨参数",
                      row = hh+2, column = 0)
        self.duangui = self.addTextArea("断轨类型，1为断轨，0为不断轨；断轨位置，断缝距离左桥台距离，单位：m。断轨位置一般取在附加温度拉力（降温时）的峰值处，即附加温度拉力极值处。\n0,0.0", 
                                    row = hh+2, column = 1,
                                    columnspan = 5,
                                    width = 140, height = 2)
        # 第二十六行
        # Label and field for the 缓冲区接头阻力
        self.addLabel(text = "缓冲区接头阻力",
                      row = hh+3, column = 0)
        self.jietou = self.addTextArea("长轨条上设置缓冲区时的接头阻力，取为常量，单位：kN。无缓冲区时可以输入0.0。\n0.0", 
                                    row = hh+3, column = 1,
                                    columnspan = 5,
                                    width = 140, height = 2)
        # 第二十七行
        # Label and field for the 制动力参数
        self.addLabel(text = "制动力参数",
                      row = hh+4, column = 0, foreground = "red")
        self.zhidong_1 = self.addTextArea("制动力的类型，输入1表示以轨面制动力集度计算制动力，输入2表示以轨面摩擦系数乘以竖向荷载计算制动力，输入0表示无制动力作用；制动力作用方向，1表示从左至右，2表示从右至左，制动力作用方向应与列车荷载入桥方向一致，计算启动力时则作用方向与列车荷载入桥方向相反。\n2,1", 
                                    row = hh+4, column = 1,
                                    columnspan = 5,
                                    width = 140, height = 2)

        # 第二十八行
        # Label and field for the 制动力大小、起始及距离
        self.addLabel(text = "制动力大小、起始及距离",
                      row = hh+5, column = 0, foreground = "red")
        self.zhidong_2 = self.addTextArea("制动力大小，当制动力类型为1时，输入轨面制动力集度，单位：kN/m，当制动力类型为2时输入轨面摩擦系数，参考UIC标准及《暂规》，一般取0.164；制动力作用起始位置，当制动力方向与列车荷载入桥方向一致时，为列车头部距左桥台距离，单位：m，反之为列车尾部距离左桥台距离；制动力作用长度，单位：m。\n0.164,320.0,400.8", 
                                    row = hh+5, column = 1,
                                    columnspan = 5,
                                    width = 140, height = 2)  

        # 第二十九行
        # Label and field for the 菜单选项核对
        #self.addLabel(text = "菜单选项核对",
        #              row = hh+6, column = 0)
        #self.output = self.addTextArea("", 
        #                           row = hh+6, column = 1,
        #                           columnspan = 5,
        #                            width = 140, height = 2) 

        # The command button1
        self.addButton(text = "生成bcwr_3.txt", row = hh+6, column = 0,
                       command = self.bcwr_3)


    # The event handler method for the button
    def bcwr_3(self):
        """在D:\\BCWR\\下生成bcwr_3.txt."""
        line1 = self.hezai_1.getText()         
        line2 = self.hezai_2.getText()
        line3 = self.duangui.getText() 
        line4 = self.jietou.getText()
        line5 = self.zhidong_1.getText()
        line6 = self.zhidong_2.getText()
        bcwr = line1 + line2 + line3 + line4 + line5 + line6
        #self.output.setText(bcwr)
        f0 = open("D:\\BCWR\\bcwr0.txt",'w') 
        f0.write(bcwr)
        f0.close()
        f0 = open("D:\\BCWR\\bcwr0.txt",'r')
        f1 = open("D:\\BCWR\\bcwr3.txt",'w')    


        line = f0.readline()
        while line:
            if line.find('。') == -1:
                f1.write(line)
            line = f0.readline()
        f0.close()  
        f1.close()        

#Instantiate and pop up the window.
bcwr_input().mainloop()
