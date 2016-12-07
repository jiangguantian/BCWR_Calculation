# -*- coding: utf-8 -*-
"""
Created on Sat Dec 26 10:34:37 2015

@author: zhanggaoyang
"""
#所有数字均需写成浮点数，不能出现整数，出现整数会导致除法运算出错！为了保证在python2和python3中均可运行，需要保证除法均用带小数的数字！
import os
from breezypythongui import EasyFrame


class bcwr_input(EasyFrame):
    """Application window for the bcwr_input(桥上无缝线路检算输入程序)."""
 
    def __init__(self):
        """Sets up the window and the widgets."""
        EasyFrame.__init__(self, title = 'bcwr.IN')

        #定义起始的行号，方便改变界面控件
        hh = -6

        # 第二十九行
        # Label and field for the 挠曲力用等梁截面参数
        self.addLabel(text = "挠曲力用等梁截面参数(每组参数之间用空格隔开)",
                      row = hh+6, column = 0)
        self.jiemian = self.addTextArea("若为等截面梁，每一跨梁截面形心距离上下翼缘距离，单位m；每线上对水平轴的惯性矩，单位m^4，若为双线整体结构，则取为整体惯性矩的一半。\n1.04183,2.00817,5.51535	1.04183,2.00817,5.51535	1.04183,2.00817,5.51535	1.04183,2.00817,5.51535	1.04183,2.00817,5.51535	1.04183,2.00817,5.51535	1.04183,2.00817,5.51535	1.04183,2.00817,5.51535	1.04183,2.00817,5.51535	1.04183,2.00817,5.51535	3.805,3.889,159.067	4.010,4.217,191.495	4.010,4.217,191.495	4.010,4.217,191.495	3.805,3.889,159.067	1.04183,2.00817,5.51535	1.04183,2.00817,5.51535	1.04183,2.00817,5.51535	1.04183,2.00817,5.51535	1.04183,2.00817,5.51535	1.04183,2.00817,5.51535	1.04183,2.00817,5.51535	1.04183,2.00817,5.51535	1.04183,2.00817,5.51535	1.04183,2.00817,5.51535", 
                                    row = hh+6, column = 1,
                                    columnspan = 5,
                                    width = 140, height = 2)    
        # 第三十行
        # Label and field for the 迭代因子
        self.addLabel(text = "迭代因子",
                      row = hh+7, column = 0)
        self.diedai = self.addTextArea("一般取0.5，或其它不大于1，但大于0的数值。\n0.5", 
                                    row = hh+7, column = 1,
                                    columnspan = 5,
                                    width = 140, height = 2)  
        # 第三十一行
        # Label and field for the 初始计算跨数和桥梁编号
        self.addLabel(text = "初始计算跨数和桥梁编号",
                      row = hh+8, column = 0)
        self.jisuankuashu = self.addTextArea("为保证迭代收敛，可分为两部分进行，一般取桥梁位移或荷载变化量较大的几跨首先迭代，然后采用全桥参数进行迭代。\n25,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25", 
                                    row = hh+8, column = 1,
                                    columnspan = 5,
                                    width = 140, height = 2)                                     
        # 第三十二行
        # Label and field for the 迭代误差限
        self.addLabel(text = "迭代误差限",
                      row = hh+9, column = 0)
        self.wucha = self.addTextArea("一般取为1kN，为保证计算结果的准确性，可取为更小的数值。\n1.0", 
                                    row = hh+9, column = 1,
                                    columnspan = 5,
                                    width = 140, height = 2)                                     
        # 第三十三行
        # Label and field for the 迭代计算步数
        self.addLabel(text = "迭代计算步数",
                      row = hh+10, column = 0)
        self.bushu = self.addTextArea("一般取为50，在制动力、挠曲力计算中不收敛时，可取为更大的数值，计算结果pd.dat中将给出程序迭代是否收敛的判断。\n50", 
                                    row = hh+10, column = 1,
                                    columnspan = 5,
                                    width = 140, height = 2) 
        # 第三十四行
        # Label and field for the 刚构桥桥墩参数
        self.addLabel(text = "刚构桥桥墩参数",
                      row = hh+11, column = 0)
        self.ganggoudun = self.addTextArea("输入刚构梁每一固结墩处墩顶水平惯性矩（单位 ）、墩底水平惯性矩（单位 ）、墩高（单位:m）、墩所在处梁的截面面积（平均面积）、墩身混凝土弹性模量；若无刚构梁跨，则不输入。\n", 
                                    row = hh+11, column = 1,
                                    columnspan = 5,
                                    width = 140, height = 2) 
        # 第三十五行
        # Label and field for the 固定支座所在桥墩的纵向水平位移（m）
        self.addLabel(text = "固定支座所在桥墩的纵向水平位移（m）",
                      row = hh+12, column = 0)
        self.gudingzhizuo = self.addTextArea("因风力、列车荷载偏心所引起的固定支座处墩顶水平位移，单位：m。\n0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0", 
                                    row = hh+12, column = 1,
                                    columnspan = 5,
                                    width = 140, height = 2)   


        # 第三十六行
        # Label and field for the 菜单选项核对
        #self.addLabel(text = "菜单选项核对",
        #              row = hh+13, column = 0)
        #self.output = self.addTextArea("", 
        #                            row = hh+13, column = 1,
        #                            columnspan = 5,
        #                            width = 140, height = 2) 

        # The command button1
        self.addButton(text = "生成bcwr_4.txt", row = hh+14, column = 0,
                       command = self.bcwr_4)



        # The command button2
        self.addButton(text = "生成bcwr.IN", row = hh+14, column = 1,
                       command = self.bcwr)
                       

        # The command button3
        self.addButton(text = "生成所有工况的bcwr.IN", row = hh+14, column = 2,
                       command = self.bcwr_All)

                       
    # The event handler method for the button
    def bcwr_4(self):
        """在D:\\BCWR\\下生成bcwr_4.txt."""
        line1 = self.jiemian.getText()
        line1 = line1.replace('	','\n')         
        line2 = self.diedai.getText()
        line3 = self.jisuankuashu.getText() 
        line4 = self.wucha.getText()
        line5 = self.bushu.getText()
        line6 = self.ganggoudun.getText()
        line7 = self.gudingzhizuo.getText()
        bcwr = line1 + line2 + line3 + line4 + line5 + line6 + line7
        #self.output.setText(bcwr)
        f0 = open("D:\\BCWR\\bcwr0.txt",'w') 
        f0.write(bcwr)
        f0.close()
        f0 = open("D:\\BCWR\\bcwr0.txt",'r')
        f1 = open("D:\\BCWR\\bcwr4.txt",'w')    


        line = f0.readline()
        while line:
            if line.find('。') == -1 and line[:-1].strip() != "":
                f1.write(line)
            line = f0.readline()
        f0.close()  
        f1.close()              

    def bcwr(self):
        """在D:\\BCWR\\下生成bcwr.txt."""
        f1 = open("D:\\BCWR\\bcwr1.txt",'r') 
        f2 = open("D:\\BCWR\\bcwr2.txt",'r') 
        f3 = open("D:\\BCWR\\bcwr3.txt",'r') 
        f4 = open("D:\\BCWR\\bcwr4.txt",'r')
        f = open("D:\\BCWR\\bcwr.IN",'w') 
        
        line = f1.readline()
        while line:
            f.write(line)
            line = f1.readline() 
        f1.close()  

        line = f2.readline()
        while line:
            f.write(line)
            line = f2.readline() 
        f2.close()

        line = f3.readline()
        while line:
            f.write(line)
            line = f3.readline() 
        f3.close()

        line = f4.readline()
        while line:
            f.write(line)
            line = f4.readline() 
        f4.close() 

        f.close()           

        
    def bcwr_All(self):
        """在D:\\BCWR\\下生成bcwr.txt."""
        #生成伸缩力工况
        f0 = open("D:\\BCWR\\bcwr.IN",'r')
        A = f0.readlines()
        f0.close()
        if os.path.exists("D:\\BCWR\\SSL") == False:
            os.mkdir('D:\\BCWR\\SSL')
        f = open("D:\\BCWR\\SSL\\bcwr.IN",'w')
        A[0] = '1\n'
        for i in A:
            f.write(i)
        f.close()
        #在生成的每个文件夹中运行bcwr_1.exe
        os.chdir("D:\\BCWR\\SSL")
        os.startfile('D:\\BCWR\\bcwr\\bcwr_1.exe')        
        
        #生成挠曲力工况
        f0 = open("D:\\BCWR\\bcwr.IN",'r')
        A = f0.readlines()
        f0.close()        
        kuashu = int(A[1])
        #定义桥跨长度数组kc
        kc = []
        kuachang = A[kuashu+3].split(',')
        for i in kuachang:
            kc.append(float(i))
        #定义荷载入桥长度数组rqc
        rqc = []   
        a = 0         
        for i in range(kuashu):
            a += kc[i]
            rqc.append(a)
        #修改第一行数据，即计算类型
        A[0] = '2\n'
        #定义左入桥时的第n+37行数据，及荷载位置行数据,并写入相应txt文件
        for i in range(kuashu):
            A[kuashu+36] = '1,%s\n' % rqc[i]
            n = str(i+1)
            if os.path.exists("D:\\BCWR\\NQL1-%s" % n) == False:
                os.mkdir("D:\\BCWR\\NQL1-%s" % n)
            f = open("D:\\BCWR\\NQL1-%s\\bcwr.IN" % n,'w')
            for i in A:
                f.write(i)
            f.close()
            #在生成的每个文件夹中运行bcwr_1.exe
            os.chdir("D:\\BCWR\\NQL1-%s" % n)
            os.startfile('D:\\BCWR\\bcwr\\bcwr_1.exe')            
        #定义右入桥时的第n+37行数据，及荷载位置行数据,并写入相应txt文件
        for i in range(kuashu):
            A[kuashu+36] = '2,%s\n' % rqc[i]
            n = str(i+1)
            if os.path.exists("D:\\BCWR\\NQL2-%s" % n) == False:
                os.mkdir("D:\\BCWR\\NQL2-%s" % n)
            f = open("D:\\BCWR\\NQL2-%s\\bcwr.IN" % n,'w')
            for i in A:
                f.write(i)
            f.close()
            #在生成的每个文件夹中运行bcwr_1.exe
            os.chdir("D:\\BCWR\\NQL2-%s" % n)
            os.startfile('D:\\BCWR\\bcwr\\bcwr_1.exe')
            
            
            
            
        #生成制动力工况
        f0 = open("D:\\BCWR\\bcwr.IN",'r')
        A = f0.readlines()
        f0.close()        
        kuashu = int(A[1])
        #定义桥跨长度数组kc
        kc = []
        kuachang = A[kuashu+3].split(',')
        for i in kuachang:
            kc.append(float(i))
        #定义荷载入桥长度数组rqc
        rqc = []   
        a = 0         
        for i in range(kuashu):
            a += kc[i]
            rqc.append(a)
        #修改第一行数据，即计算类型
        A[0] = '4\n'
        #定义左入桥时的第n+37行数据，及荷载位置行数据,并写入相应txt文件
        for i in range(kuashu):
            A[kuashu+36] = '1,%s\n' % rqc[i]
            A[kuashu+39] = '2,1\n'
            A[kuashu+40] = '0.164,%s,400.8\n' % rqc[i]
            n = str(i+1)
            if os.path.exists("D:\\BCWR\\ZDL1-%s" % n) == False:
                os.mkdir("D:\\BCWR\\ZDL1-%s" % n)
            f = open("D:\\BCWR\\ZDL1-%s\\bcwr.IN" % n,'w')
            for i in A:
                f.write(i)
            f.close()
            #在生成的每个文件夹中运行bcwr_1.exe
            os.chdir("D:\\BCWR\\ZDL1-%s" % n)
            os.startfile('D:\\BCWR\\bcwr\\bcwr_1.exe')            
        #定义右入桥时的第n+37行数据，及荷载位置行数据,并写入相应txt文件
        for i in range(kuashu):
            A[kuashu+36] = '2,%s\n' % rqc[i]
            A[kuashu+39] = '2,2\n'
            A[kuashu+40] = '0.164,%s,400.8\n' % rqc[i]            
            n = str(i+1)        
            if os.path.exists("D:\\BCWR\\ZDL2-%s" % n) == False:
                os.mkdir("D:\\BCWR\\ZDL2-%s" % n)
            f = open("D:\\BCWR\\ZDL2-%s\\bcwr.IN" % n,'w')
            for i in A:
                f.write(i)
            f.close()
            #在生成的每个文件夹中运行bcwr_1.exe,生成ANSYS分析所需要的文件（有9个）
            os.chdir("D:\\BCWR\\ZDL2-%s" % n)
            os.startfile('D:\\BCWR\\bcwr\\bcwr_1.exe')

            
            
            
#import subprocess
#cmd = '"C:\\Program Files\\ANSYS Inc\\v121\\ANSYS\\bin\\winx64\\ansys121.exe"  -p ane3fl -dir "D:\\BCWR\\ZDL2-1" -j "file" -s read -l en-us -b -i "D:\\BCWR\\ZDL2-1\\bcwr_2.txt" -o "D:\\BCWR\\ZDL2-1\\file.out"'
#ps = subprocess.Popen(cmd);
#ps.wait();    #让程序阻塞
#os.system('"C:\\Program Files\\ANSYS Inc\\v121\\ANSYS\\bin\\winx64\\ansys121.exe"  -p ane3fl -dir "D:\\BCWR\\ZDL2-1" -j "file" -s read -l en-us -b -i "D:\\BCWR\\bcwr_ANSYS.txt" -o "D:\\BCWR\\ZDL2-1\\file.out"')

       
#Instantiate and pop up the window.
bcwr_input().mainloop()


