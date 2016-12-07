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
    from Tkinter import HORIZONTAL
else:
    from tkinter import HORIZONTAL


from breezypythongui import EasyFrame
from breezypythongui import DISABLED
import numpy as np


class bcwr_input(EasyFrame):
    """Application window for the bcwr_input(桥上无缝线路检算输入程序)."""
 
    def __init__(self):
        """Sets up the window and the widgets."""
        EasyFrame.__init__(self, title = 'bcwr.IN')


        # 第一行
        # Label and field for the 计算类型
        self.addLabel(text = "计算类型",
                      row = 0, column = 0, foreground = "red")
        # Add the menu bar for the menu
        # Add the button group
        self.cal_type = self.addRadiobuttonGroup(row = 0, column = 1,
                                              columnspan = 4,
                                              orient = HORIZONTAL)
 
        # Add the radio buttons to the group
        default_cal_type = self.cal_type.addRadiobutton("1-shensuo")
        self.cal_type.addRadiobutton("2-naoqu")
        self.cal_type.addRadiobutton("3-duangui")
        self.cal_type.addRadiobutton("4-zhidong")
        # Select one of the buttons in the group
        self.cal_type.setSelectedButton(default_cal_type)


        # 第二行
        # Label and field for the number of 桥梁跨数
        self.addLabel(text = "桥梁跨数N",
                      row = 1, column = 0)
        self.kuashu = self.addTextArea("跨数。\n25", 
                                    row = 1, column = 1,
                                    columnspan = 5,
                                    width = 140, height = 2) 


        # 第三行
        # Label and field for the 墩台纵向水平刚度（kN/m）
        self.addLabel(text = "墩台纵向水平刚度（kN/m）",
                      row = 2, column = 0)
        self.gangdu = self.addTextArea("每个墩台（1~N+1）的纵向水平刚度。\n245350,164700,96700,141250,60700,58500,57400,49500,57450,66100,339500,67150,317800,622600,467250,96550,47300,34300,34200,34100,35050,33700,34950,40100,40200,36050", 
                                    row = 2, column = 1,
                                    columnspan = 5,
                                    width = 140, height = 2)
                                    
        # 第四行
        # Label and field for the 桥梁跨长（m）
        self.addLabel(text = "桥梁跨长（m）",
                      row = 3, column = 0)
        self.kuachang = self.addTextArea("每一跨的跨长。\n32.0,32.0,32.0,32.0,32.0,32.0,32.0,32.0,32.0,32.0,40.0,64.0,64.0,64.0,40.0,32.0,32.0,32.0,32.0,32.0,32.0,32.0,32.0,32.0,32.0", 
                                    row = 3, column = 1,
                                    columnspan = 5,
                                    width = 140, height = 2)

        # 第五行
        # Label and field for the 桥梁类型
        self.addLabel(text = "桥梁类型",
                      row = 4, column = 0)
        self.qiaoshi = self.addTextArea("每一跨桥梁的类型：简支梁取1，连续梁取2，刚构取4，其它桥梁型式为3，数据个数为N。\n1,1,1,1,1,1,1,1,1,1,2,2,2,2,2,1,1,1,1,1,1,1,1,1,1", 
                                    row = 4, column = 1,
                                    columnspan = 5,
                                    width = 140, height = 2)                                   


        # 第六行
        # Label and field for the 桥梁材料类型
        self.addLabel(text = "桥梁材料类型",
                      row = 5, column = 0)
        self.cailiao = self.addTextArea("每一跨梁材料类型：混凝土梁取1，钢梁取2，组合梁取2，数据个数为N。\n1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1", 
                                    row = 5, column = 1,
                                    columnspan = 5,
                                    width = 140, height = 2) 
                                    
        # 第七行
        # Label and field for the 桥梁截面类型
        self.addLabel(text = "桥梁截面类型",
                      row = 6, column = 0)
        self.jiemian = self.addTextArea("每一跨梁截面类型；等截面梁取1，变截面梁取2，数据个数为N。\n1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1", 
                                    row = 6, column = 1,
                                    columnspan = 5,
                                    width = 140, height = 2) 

        # 第八行
        # Label and field for the 桥梁接缝类型
        self.addLabel(text = "桥梁接缝类型",
                      row = 7, column = 0)
        self.jiefeng = self.addTextArea("每一跨梁左端是否断开，若断开取1，否则取0，数据个数为N。\n1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,1,1,1,1,1,1,1,1,1,1", 
                                    row = 7, column = 1,
                                    columnspan = 5,
                                    width = 140, height = 2) 

        # 第九行
        # Label and field for the 桥梁支座类型
        self.addLabel(text = "桥梁支座类型",
                      row = 8, column = 0)
        self.zhizuo = self.addTextArea("每一跨梁左右支座支承类型，固定支座取1，活动支座取0，数据个数为2N。\n1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,0,0,0,1,1,0,0,0,0,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0", 
                                    row = 8, column = 1,
                                    columnspan = 5,
                                    width = 140, height = 2) 

        # 第十行                                   
        # Label and field for the 桥梁有限单元长度（m）
        self.addLabel(text = "桥梁有限单元长度（m）",
                      row = 9, column = 0)
        self.danyuan = self.addTextArea("划分的有限单元长度。\n1.0", 
                                    row = 9, column = 1,
                                    columnspan = 5,
                                    width = 140, height = 2)

        # 第十一行                                   
        # Label and field for the 钢轨参数
        self.addLabel(text = "钢轨参数",
                      row = 10, column = 0)
        self.ganggui = self.addTextArea("钢轨弹性模量：单位；钢轨截面积：单位；轨枕间距：单位m；钢轨钢的线膨胀系数：单位：/℃；混凝土梁的线膨胀系数：单位：/℃。\n2.06e8,7.75e-3,0.6,1.18e-5,1.00e-5", 
                                    row = 10, column = 1,
                                    columnspan = 5,
                                    width = 140, height = 2)        


        # 第十二行
        # Label and field for the 菜单选项核对
        #self.addLabel(text = "菜单选项核对",
        #              row = 11, column = 0)
        #self.output = self.addTextArea("", 
        #                            row = 11, column = 1,
        #                            columnspan = 5,
        #                            width = 140, height = 2)  


        # The command button1
        self.addButton(text = "生成bcwr_1.txt", row = 11, column = 0,
                       command = self.bcwr_1)


    # The event handler method for the button
    def bcwr_1(self):
        """在D:\\BCWR\\下生成bcwr_1.txt."""
        if self.cal_type.getSelectedButton()["value"] == "1-shensuo":
            line1 = '1\n' 
        if self.cal_type.getSelectedButton()["value"] == "2-naoqu":
            line1 = '2\n'
        if self.cal_type.getSelectedButton()["value"] == "3-duangui":
            line1 = '3\n'
        if self.cal_type.getSelectedButton()["value"] == "4-zhidong":
            line1 = '4\n'
        line2 = self.kuashu.getText()
        line3 = self.gangdu.getText()
        line3 = line3.replace(',','\n')
        line4 = self.kuachang.getText()
        line5 = self.qiaoshi.getText() 
        line6 = self.cailiao.getText()
        line7 = self.jiemian.getText()
        line8 = self.jiefeng.getText()
        line9 = self.zhizuo.getText()
        line10 = self.danyuan.getText()
        line11 = self.ganggui.getText()
        bcwr = line1 + line2 + line3 + line4 + line5 + line6 + line7 + line8 + line9 + line10 + line11 
        #self.output.setText(bcwr)
        #写入bcwr1.txt,其中bcwr0是临时文件
        f0 = open("D:\\BCWR\\bcwr0.txt",'w') 
        f0.write(bcwr)
        f0.close()
        f0 = open("D:\\BCWR\\bcwr0.txt",'r')
        f1 = open("D:\\BCWR\\bcwr1.txt",'w')    
        line = f0.readline()
        while line:
            if line.find('。') == -1:
                f1.write(line)
            line = f0.readline()
        f0.close()  
        f1.close()   

    
#Instantiate and pop up the window.
bcwr_input().mainloop()
