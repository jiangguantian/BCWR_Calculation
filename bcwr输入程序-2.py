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
        #定义起始的行号，方便改变界面控件
        hh = 0

        # 第十二行                                   
        # Label and field for the 轨道温升温降最大幅度（℃）
        self.addLabel(text = "轨道温升温降最大幅度（℃）",
                      row = hh, column = 0, foreground = "red")
        self.guiwen = self.addTextArea("轨温变化幅度。\n0", 
                                    row = hh, column = 1,
                                    columnspan = 5,
                                    width = 140, height = 2)                                              

        # 第十三行
        # Label and field for the 桥上钢轨类型
        self.addLabel(text = "桥上钢轨类型",
                      row = hh+1, column = 0)
        # Add the menu bar for the menu
        # Add the button group
        self.qiaogui_type = self.addRadiobuttonGroup(row = hh+1, column = 1,
                                              columnspan = 4,
                                              orient = HORIZONTAL)
 
        # Add the radio buttons to the group
        default_qiaogui_type = self.qiaogui_type.addRadiobutton("guding")
        self.qiaogui_type.addRadiobutton("shensuoqi")
        self.qiaogui_type.addRadiobutton("huanchongqu")
        # Select one of the buttons in the group
        self.qiaogui_type.setSelectedButton(default_qiaogui_type)


        hh = 1
        # 第十四行
        # Label and field for the 两端路基轨条区段类型
        self.addLabel(text = "两端路基轨条区段类型",
                      row = hh+1, column = 0)
        # Add the menu bar for the menu
        # Add the button group
        self.lugui_type = self.addRadiobuttonGroup(row = hh+1, column = 1,
                                              columnspan = 4,
                                              orient = HORIZONTAL)
 
        # Add the radio buttons to the group
        default_lugui_type = self.lugui_type.addRadiobutton("guding")
        self.lugui_type.addRadiobutton("huanchongqu")
        # Select one of the buttons in the group
        self.lugui_type.setSelectedButton(default_lugui_type)


        # 第十三行
        # Add the menu bar for the menu
        #menuBar = self.addMenuBar(row = hh+1, column = 0, columnspan = 2)
        
        # Add the 桥上钢条区段类型 menu
        #qiaoduanMenu = menuBar.addMenu("桥上钢轨类型")
        # Add the command options for the 桥上钢条区段类型 menu
        #qiaoduanMenu.addMenuItem("全固定区",  self.guding_q)
        #qiaoduanMenu.addMenuItem("设伸缩调节器", self.tiaojieqi_q)
        #qiaoduanMenu.addMenuItem("设缓冲区", self.huanchong_q)                                              


        # Add the 两端路基轨条区段类型 menu
        #qiaoduanMenu = menuBar.addMenu("两端路基上钢轨类型")
        # Add the command options for the 两端路基轨条区段类型 menu
        #qiaoduanMenu.addMenuItem("全固定区",  self.guding_l)
        #qiaoduanMenu.addMenuItem("设缓冲区", self.huanchong_l)   

                                              
        # 第十四行
        # Label and field for the 桥上轨条结构参数
        self.addLabel(text = "桥上轨条结构参数",
                      row = hh+2, column = 0)
        self.guitiao_q = self.addTextArea("若桥梁上长轨条设置伸缩调节器、缓冲区时，接头数量，及每一个接头距左桥台的距离，单位：m；左端路基上设有伸缩调节器时，输入负值，右端路基上设有伸缩器时，输入大于全桥长度的数值。\n0,0.0", 
                                    row = hh+2, column = 1,
                                    columnspan = 5,
                                    width = 140, height = 2) 
                                    
        # 第十五行
        # Label and field for the 路基上轨条结构参数
        self.addLabel(text = "路基上轨条结构参数",
                      row = hh+3, column = 0)
        self.guitiao_l = self.addTextArea("若路基上长轨条设置缓冲区时，缓冲区数量、左缓冲区距离左桥台距离、右缓冲区距离左桥台距离，输入绝对值单位：m；若为固定区，左右距离均输入为0.0。\n0,0.0,0.0", 
                                    row = hh+3, column = 1,
                                    columnspan = 5,
                                    width = 140, height = 2)                                     

        # 第十六行
        # Label and field for the 路基上钢轨计算长度
        self.addLabel(text = "路基上钢轨计算长度",
                      row = hh+4, column = 0)
        self.lujichang = self.addTextArea("桥梁左右两端钢轨计算长度，单位：m；输入绝对值，一般取为桥梁边跨长度+80m，且不小于100m。\n112.0,112.0", 
                                    row = hh+4, column = 1,
                                    columnspan = 5,
                                    width = 140, height = 2)                                      

        # 第十七行
        # Label and field for the 小阻力扣件参数
        self.addLabel(text = "小阻力扣件参数",
                      row = hh+5, column = 0)
        self.xiaozuli = self.addTextArea("桥上小阻力扣件段数，每段始终点距左桥台距离，单位：m；路基上设有小阻力扣件时，也按距离左桥台位置输入其代数值。\n1,552.0,656.0", 
                                    row = hh+5, column = 1,
                                    columnspan = 5,
                                    width = 140, height = 2) 

        # 第十八行
        # Label and field for the 线路阻力参数集
        self.addLabel(text = "线路阻力参数集",
                      row = hh+6, column = 0)
        self.zuli = self.addTextArea("阻力参数。\n5,2,23.2,0.002\n5,2,15.0,0.002\n5,2,8.0,0.0005\n5,2,23.2,0.002\n5,2,12.4,0.0005\n5,2,15.0,0.002\n5,2,8.0,0.0005\n5,2,15.0,0.002\n5,2,8.0,0.0005\n5,2,23.2,0.002\n5,2,8.0,0.0005\n5,2,23.2,0.002\n5,2,8.0,0.0005", 
                                    row = hh+6, column = 1,
                                    columnspan = 5,
                                    width = 140, height = 2) 

        # 第十九行
        # Label and field for the 桥梁弹性模量（kN/m²）
        self.addLabel(text = "桥梁弹性模量（kN/m²）",
                      row = hh+7, column = 0)
        self.tanmo = self.addTextArea("每跨梁弹性模量，单位kPa。\n3.55e07,3.55e07,3.55e07,3.55e07,3.55e07,3.55e07,3.55e07,3.55e07,3.55e07,3.55e07,3.55e07,3.55e07,3.55e07,3.55e07,3.55e07,3.55e07,3.55e07,3.55e07,3.55e07,3.55e07,3.55e07,3.55e07,3.55e07,3.55e07,3.55e07", 
                                    row = hh+7, column = 1,
                                    columnspan = 5,
                                    width = 140, height = 2) 

        # 第二十行
        # Label and field for the 梁上有无道砟
        self.addLabel(text = "梁上有无道砟",
                      row = hh+8, column = 0)
        self.daozha = self.addTextArea("有碴梁为1，无碴梁为2。\n1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1", 
                                    row = hh+8, column = 1,
                                    columnspan = 5,
                                    width = 140, height = 2) 

        # 第二十一行
        # Label and field for the 桥梁日温差（℃）
        self.addLabel(text = "桥梁日温差（℃）",
                      row = hh+9, column = 0)
        self.wencha = self.addTextArea("混凝土有碴梁、无碴混凝土梁、钢梁的日温差，单位：/℃。\n15.0,30.0,25.0", 
                                    row = hh+9, column = 1,
                                    columnspan = 5,
                                    width = 140, height = 2) 

        # 第二十二行
        # Label and field for the 特殊梁跨上翼缘单元位移
        self.addLabel(text = "特殊梁跨上翼缘单元位移",
                      row = hh+10, column = 0)
        self.shangyiyuan = self.addTextArea("若无特殊梁跨，输入0，0，0；若有特殊形式的梁跨，输入其单元节点数量（单元节点数量=梁跨长/有限单元长度+1）、每一单元节点位置（距左桥台距离，单位m ）、每一单元节点上翼缘位移（对钢桁梁为支承桥枕的纵梁），单位m，指向右桥台为，反之为负。\n0,0.0,0.0", 
                                    row = hh+10, column = 1,
                                    columnspan = 5,
                                    width = 140, height = 2)

        # 第三十六行
        # Label and field for the 菜单选项核对
        #self.addLabel(text = "菜单选项核对",
        #              row = hh+11, column = 0)
        #self.output = self.addTextArea("", 
        #                            row = hh+11, column = 1,
        #                            columnspan = 5,
        #                            width = 140, height = 2)        
        # The command button1
        self.addButton(text = "生成bcwr_2.txt", row = hh+11, column = 0,
                       command = self.bcwr_2)


    # The event handler method for the button
    def bcwr_2(self):
        """在D:\\BCWR\\下生成bcwr_2.txt."""
        if self.qiaogui_type.getSelectedButton()["value"] == "guding":
            line2 = '1\n' 
        if self.qiaogui_type.getSelectedButton()["value"] == "shensuoqi":
            line2 = '2\n'
        if self.qiaogui_type.getSelectedButton()["value"] == "huangchongqu":
            line2 = '3\n'
        if self.qiaogui_type.getSelectedButton()["value"] == "guding":
            line3 = '1\n'
        if self.qiaogui_type.getSelectedButton()["value"] == "huangchongqu":
            line3 = '2\n'
        line1 = self.guiwen.getText()         
        line4 = self.guitiao_q.getText()
        line5 = self.guitiao_l.getText() 
        line6 = self.lujichang.getText()
        line7 = self.xiaozuli.getText()
        line8 = self.zuli.getText()
        line9 = self.tanmo.getText()
        line10 = self.daozha.getText()
        line11 = self.wencha.getText()
        line12 = self.shangyiyuan.getText()
        bcwr = line1 + line2 + line3 + line4 + line5 + line6 + line7 + line8 + line9 + line10 + line11 + line12
        #self.output.setText(bcwr)
        f0 = open("D:\\BCWR\\bcwr0.txt",'w') 
        f0.write(bcwr)
        f0.close()
        f0 = open("D:\\BCWR\\bcwr0.txt",'r')
        f1 = open("D:\\BCWR\\bcwr2.txt",'w')    


        line = f0.readline()
        while line:
            if line.find('。') == -1:
                f1.write(line)
            line = f0.readline()
        f0.close()  
        f1.close()   

       
#Instantiate and pop up the window.
bcwr_input().mainloop()
