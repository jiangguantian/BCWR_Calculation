# -*- coding: utf-8 -*-
"""
Created on Fri Oct 14 08:35:58 2016

@author: zhanggaoyang
"""

#所有数字均需写成浮点数，不能出现整数，出现整数会导致除法运算出错！为了保证在python2和python3中均可运行，需要保证除法均用带小数的数字！
import subprocess
import os
from breezypythongui import EasyFrame
import numpy as np
from matplotlib import pyplot as plt
from matplotlib.font_manager import FontProperties
font = FontProperties(fname=r"c:\windows\fonts\simsun.ttc", size=14)
import sys
versionNumber = sys.version_info.major
if versionNumber == 3:
    import tkinter
    import tkinter.simpledialog
    Tkinter = tkinter
    tkSimpleDialog = tkinter.simpledialog
else:
    import Tkinter

N = Tkinter.N
S = Tkinter.S
E = Tkinter.E
W = Tkinter.W
CENTER = Tkinter.CENTER


class bcwr_ansys(EasyFrame):
    """Application window for the bcwr_input(桥上无缝线路检算输入程序)."""
 
    def __init__(self):
        """Sets up the window and the widgets."""
        EasyFrame.__init__(self, title = 'ANSYS分析及结果展示')

        
        # Label and field for the 钢轨最大纵向力及其位置（m,kN）及其所在工况
        self.addLabel(text = "钢轨最大纵向力（kN）、荷载所在位置（m）、所在工况",
                      row = 0, column = 1, foreground = "red",)

        # Label and field for the 钢轨最大纵向力及其位置（m,kN）及其所在工况
        self.addLabel(text = "钢轨最小纵向力（kN）、荷载所在位置（m）、所在工况",
                      row = 0, column = 2, foreground = "red")
        
        
        
        # Label and field for the 伸缩力产生的钢轨最大、最小纵向力及其位置（m,kN）及其所在工况
        self.addLabel(text = "伸缩力",
                      row = 1, column = 0)
        self.SSL_max = self.addTextArea("", 
                                    row = 1, column = 1,
                                    columnspan = 2,
                                    width = 20, height = 2)        
 
        self.SSL_min = self.addTextArea("", 
                                    row = 1, column = 2,
                                    columnspan = 2,
                                    width = 20, height = 2) 

        # Label and field for the 挠曲力产生的钢轨最大、最小纵向力及其位置（m,kN）及其所在工况
        self.addLabel(text = "挠曲力",
                      row = 2, column = 0)
        self.NQL_max = self.addTextArea("", 
                                    row = 2, column = 1,
                                    columnspan = 2,
                                    width = 20, height = 2)        
 
        self.NQL_min = self.addTextArea("", 
                                    row = 2, column = 2,
                                    columnspan = 2,
                                    width = 20, height = 2)        
        
        
        
        # Label and field for the 制动力产生的钢轨最大、最小纵向力及其位置（m,kN）及其所在工况
        self.addLabel(text = "制动力",
                      row = 3, column = 0)
        self.ZDL_max = self.addTextArea("", 
                                    row = 3, column = 1,
                                    columnspan = 2,
                                    width = 20, height = 2)        
 
        self.ZDL_min = self.addTextArea("", 
                                    row = 3, column = 2,
                                    columnspan = 2,
                                    width = 20, height = 2) 
       
        
        
        
        
        # The command button1
        self.addButton(text = "ANSYS分析", row = 4, column = 0,
                       command = self.ANSYS)



        # The command button2
        self.addButton(text = "生成结果文件", row = 4, column = 1,
                       command = self.result_file_display)

        
        
        # The command button4
        self.addButton(text = "求解各种附加力的最不利值", row = 4, column = 2,
                       command = self.result_worst)
        
        
        # The command button3
        self.addButton(text = "生成所有结果图片", row = 4, column = 3,
                       command = self.result_picture_display)         
        
        
    # The event handler method for the button
    def ANSYS(self):
        """进行所有工况的ANSYS分析"""
        #修改bcwr_ANSYS.txt
        f0 = open("D:\\BCWR\\bcwr.IN",'r')
        A = f0.readlines()
        f0.close()
        kuashu = A[1]
        #        #打开一次bcwr_ANSYS.txt读取数据存储到B便于后续更改                
        #        f = open("D:\\BCWR\\bcwr\\bcwr_ANSYS.txt",'r')
        #        B = f.readlines()
        #        f.close()
        #        B[2] = 'N=%s!桥梁跨数，只需要改这个\n' % kuashu
        #        #再打开一次bcwr_ANSYS.txt写入改后的B 
        #        f = open("D:\\BCWR\\bcwr\\bcwr_ANSYS.txt",'w')
        #        for i in B:
        #            f.write(i)
        #        f.close()
        
        
        #在所有工况下循环运行ANSYS求解
        for i in range(int(kuashu)):
            n = str(i+1)
            cmd = '"C:\\Program Files\\ANSYS Inc\\v121\\ANSYS\\bin\\winx64\\ansys121.exe"  -p ane3fl -dir "D:\\BCWR\\NQL1-%s" -j "file" -s read -l en-us -b -i "D:\\BCWR\\bcwr\\bcwr_2.txt" -o "D:\\BCWR\\NQL1-%s\\file.out"' % (n,n)
            ps = subprocess.Popen(cmd);
            ps.wait();    #让程序阻塞
            
            
        for i in range(int(kuashu)):
            n = str(i+1)
            cmd = '"C:\\Program Files\\ANSYS Inc\\v121\\ANSYS\\bin\\winx64\\ansys121.exe"  -p ane3fl -dir "D:\\BCWR\\NQL2-%s" -j "file" -s read -l en-us -b -i "D:\\BCWR\\bcwr\\bcwr_2.txt" -o "D:\\BCWR\\NQL2-%s\\file.out"' % (n,n)
            ps = subprocess.Popen(cmd);
            ps.wait();    #让程序阻塞
            

        for i in range(int(kuashu)):
            n = str(i+1)
            cmd = '"C:\\Program Files\\ANSYS Inc\\v121\\ANSYS\\bin\\winx64\\ansys121.exe"  -p ane3fl -dir "D:\\BCWR\\ZDL1-%s" -j "file" -s read -l en-us -b -i "D:\\BCWR\\bcwr\\bcwr_2.txt" -o "D:\\BCWR\\ZDL1-%s\\file.out"' % (n,n)
            ps = subprocess.Popen(cmd);
            ps.wait();    #让程序阻塞

        for i in range(int(kuashu)):
            n = str(i+1)
            cmd = '"C:\\Program Files\\ANSYS Inc\\v121\\ANSYS\\bin\\winx64\\ansys121.exe"  -p ane3fl -dir "D:\\BCWR\\ZDL2-%s" -j "file" -s read -l en-us -b -i "D:\\BCWR\\bcwr\\bcwr_2.txt" -o "D:\\BCWR\\ZDL2-%s\\file.out"' % (n,n)
            ps = subprocess.Popen(cmd);
            ps.wait();    #让程序阻塞


        cmd = '"C:\\Program Files\\ANSYS Inc\\v121\\ANSYS\\bin\\winx64\\ansys121.exe"  -p ane3fl -dir "D:\\BCWR\\SSL" -j "file" -s read -l en-us -b -i "D:\\BCWR\\bcwr\\bcwr_2.txt" -o "D:\\BCWR\\SSL\\file.out"'
        ps = subprocess.Popen(cmd);
        ps.wait();    #让程序阻塞



        for i in range(int(kuashu)):
            n = str(i+1)            
            for rt, dirs, files in os.walk("D:\\BCWR\\SSL"):
                for file in files:
                    if file.find('.dat')==-1 and file.find('.DAT')==-1 and file.find('.IN')==-1:
                        os.remove(rt+'\\'+file)           

            for rt, dirs, files in os.walk("D:\\BCWR\\NQL1-%s" % n):
                for file in files:
                    if file.find('.dat')==-1 and file.find('.DAT')==-1 and file.find('.IN')==-1:
                        os.remove(rt+'\\'+file)                         
                        
            for rt, dirs, files in os.walk("D:\\BCWR\\NQL2-%s" % n):
                for file in files:
                    if file.find('.dat')==-1 and file.find('.DAT')==-1 and file.find('.IN')==-1:
                        os.remove(rt+'\\'+file) 

            for rt, dirs, files in os.walk("D:\\BCWR\\ZDL1-%s" % n):
                for file in files:
                    if file.find('.dat')==-1 and file.find('.DAT')==-1 and file.find('.IN')==-1:
                        os.remove(rt+'\\'+file) 


            for rt, dirs, files in os.walk("D:\\BCWR\\ZDL2-%s" % n):
                for file in files:
                    if file.find('.dat')==-1 and file.find('.DAT')==-1 and file.find('.IN')==-1:
                        os.remove(rt+'\\'+file)                         
                        
            for rt, dirs, files in os.walk("D:\\BCWR\\SSL"):
                for file in files:
                    if file.find('.dat')==-1 and file.find('.DAT')==-1 and file.find('.IN')==-1:
                        os.remove(rt+'\\'+file) 

            

       
    def result_file_display(self):
        """绘制结果"""
        f0 = open("D:\\BCWR\\bcwr.IN",'r')
        A = f0.readlines()
        f0.close()
        kuashu = A[1]
        lujing = []
        #钢轨纵向力的最大值和最小值数组
        SSL_rail_force_max = []
        SSL_rail_force_min = []
        NQL1_rail_force_max = []
        NQL1_rail_force_min = []
        NQL2_rail_force_max = []
        NQL2_rail_force_min = []
        ZDL1_rail_force_max = []
        ZDL1_rail_force_min = []
        ZDL2_rail_force_max = []
        ZDL2_rail_force_min = []
             
        #在所有工况的图片保存路径
        for i in range(int(kuashu)):
            n = str(i+1)
            lujing.append("D:\\BCWR\\SSL")
            lujing.append("D:\\BCWR\\NQL1-%s" % n)
            lujing.append("D:\\BCWR\\NQL2-%s" % n)
            lujing.append("D:\\BCWR\\ZDL1-%s" % n)
            lujing.append("D:\\BCWR\\ZDL2-%s" % n)
        #生成所有工况下的图片 
        for lj in lujing:
            #读取钢轨纵向力和距离左桥台距离数组
            f = open(lj + "\\pr.dat") 
            line = f.readline()
            rail_juli = np.array([])#长轨条各单元距左台距离，向右为正，单位：m；
            rail_force = np.array([])#长轨条各单元节点纵向力，向右为正，单位：mm;
            while line:
                juli = float(line[0:12])
                rail_juli = np.append(rail_juli, juli)
                force = float(line[12:24])
                rail_force = np.append(rail_force, force)    
                line = f.readline()
            f.close()


            #找出该工况下钢轨纵向力的最大值和最小值及其对应的距左桥台的距离及其所在工况
            if lj.find('SSL')!=-1:
                SSL_rail_force_max.append((np.round(np.max(rail_force),decimals=3),rail_juli[np.argmax(rail_force)],lj[8:]))
                SSL_rail_force_min.append((np.round(np.min(rail_force),decimals=3),rail_juli[np.argmin(rail_force)],lj[8:]))
            if lj.find('NQL1')!=-1:
                NQL1_rail_force_max.append((np.round(np.max(rail_force),decimals=3),rail_juli[np.argmax(rail_force)],lj[8:]))
                NQL1_rail_force_min.append((np.round(np.min(rail_force),decimals=3),rail_juli[np.argmin(rail_force)],lj[8:]))
            if lj.find('NQL2')!=-1:
                NQL2_rail_force_max.append((np.round(np.max(rail_force),decimals=3),rail_juli[np.argmax(rail_force)],lj[8:]))
                NQL2_rail_force_min.append((np.round(np.min(rail_force),decimals=3),rail_juli[np.argmin(rail_force)],lj[8:]))               
            if lj.find('ZDL1')!=-1:
                ZDL1_rail_force_max.append((np.round(np.max(rail_force),decimals=3),rail_juli[np.argmax(rail_force)],lj[8:]))
                ZDL1_rail_force_min.append((np.round(np.min(rail_force),decimals=3),rail_juli[np.argmin(rail_force)],lj[8:]))
            if lj.find('ZDL2')!=-1:
                ZDL2_rail_force_max.append((np.round(np.max(rail_force),decimals=3),rail_juli[np.argmax(rail_force)],lj[8:]))
                ZDL2_rail_force_min.append((np.round(np.min(rail_force),decimals=3),rail_juli[np.argmin(rail_force)],lj[8:]))

            
        #保存所有工况下的钢轨纵向力的最大值，最小值及其对应的位置和所在的工况
        f = open("D:\\BCWR\\SSL_rail_force_max.txt",'w')
        for i in SSL_rail_force_max:
            a,b,c = i
            a = '{:<12.3f}'.format(a)
            b = '{:<12.1f}'.format(b)
            c = '{:<12}'.format(c)
            f.write(a + b + c + '\n')
        f.close()    
            
        f = open("D:\\BCWR\\SSL_rail_force_min.txt",'w')            
        for i in SSL_rail_force_min:
            a,b,c = i
            a = '{:<12.3f}'.format(a)
            b = '{:<12.1f}'.format(b)
            c = '{:<12}'.format(c)
            f.write(a + b + c + '\n')           
        f.close()


        f = open("D:\\BCWR\\NQL_rail_force_max.txt",'w')
        for i in NQL1_rail_force_max:
            a,b,c = i
            a = '{:<12.3f}'.format(a)
            b = '{:<12.1f}'.format(b)
            c = '{:<12}'.format(c)
            f.write(a + b + c + '\n')
        for i in NQL2_rail_force_max:
            a,b,c = i
            a = '{:<12.3f}'.format(a)
            b = '{:<12.1f}'.format(b)
            c = '{:<12}'.format(c)
            f.write(a + b + c + '\n')            
        f.close()

        f = open("D:\\BCWR\\NQL_rail_force_min.txt",'w')
        for i in NQL1_rail_force_min:
            a,b,c = i
            a = '{:<12.3f}'.format(a)
            b = '{:<12.1f}'.format(b)
            c = '{:<12}'.format(c)
            f.write(a + b + c + '\n')
        for i in NQL2_rail_force_min:
            a,b,c = i
            a = '{:<12.3f}'.format(a)
            b = '{:<12.1f}'.format(b)
            c = '{:<12}'.format(c)
            f.write(a + b + c + '\n')           
        f.close()

        
        f = open("D:\\BCWR\\ZDL_rail_force_max.txt",'w')
        for i in ZDL1_rail_force_max:
            a,b,c = i
            a = '{:<12.3f}'.format(a)
            b = '{:<12.1f}'.format(b)
            c = '{:<12}'.format(c)
            f.write(a + b + c + '\n')
        for i in ZDL2_rail_force_max:
            a,b,c = i
            a = '{:<12.3f}'.format(a)
            b = '{:<12.1f}'.format(b)
            c = '{:<12}'.format(c)
            f.write(a + b + c + '\n')           
        f.close()        
        

        f = open("D:\\BCWR\\ZDL_rail_force_min.txt",'w')
        for i in ZDL1_rail_force_min:
            a,b,c = i
            a = '{:<12.3f}'.format(a)
            b = '{:<12.1f}'.format(b)
            c = '{:<12}'.format(c)
            f.write(a + b + c + '\n')
        for i in ZDL2_rail_force_min:
            a,b,c = i
            a = '{:<12.3f}'.format(a)
            b = '{:<12.1f}'.format(b)
            c = '{:<12}'.format(c)
            f.write(a + b + c + '\n')            
        f.close()           
        

        
        
        
        
    def result_picture_display(self):
        """绘制结果"""
        f0 = open("D:\\BCWR\\bcwr.IN",'r')
        A = f0.readlines()
        f0.close()
        kuashu = A[1]
        lujing = []

            
        #在所有工况的图片保存路径
        for i in range(int(kuashu)):
            n = str(i+1)
            lujing.append("D:\\BCWR\\SSL")
            lujing.append("D:\\BCWR\\NQL1-%s" % n)
            lujing.append("D:\\BCWR\\NQL2-%s" % n)
            lujing.append("D:\\BCWR\\ZDL1-%s" % n)
            lujing.append("D:\\BCWR\\ZDL2-%s" % n)

        #生成所有工况下的图片 
        for lj in lujing:
            #读取钢轨纵向力和距离左桥台距离数组
            f = open(lj + "\\pr.dat") 
            line = f.readline()
            rail_juli = np.array([])#长轨条各单元距左台距离，向右为正，单位：m；
            rail_force = np.array([])#长轨条各单元节点纵向力，向右为正，单位：mm;
            while line:
                juli = float(line[0:12])
                rail_juli = np.append(rail_juli, juli)
                force = float(line[12:24])
                rail_force = np.append(rail_force, force)    
                line = f.readline()
            f.close()
            
            #绘制钢轨纵向力随距左桥台距离的变化图
            plt.title(u'钢轨力', fontproperties=font)
            plt.xlabel(u'L(m)', fontproperties=font)
            plt.ylabel(u'钢轨力(kN)', fontproperties=font)
            A = 100.0#X坐标的刻度间隔
            X = rail_juli
            plt.xticks(np.arange(np.min(X//A)*A,np.max(X//A)*A+0.2*A,A))
            plt.plot(rail_juli, rail_force, 'r-', linewidth=1)
            plt.grid(b=True, which='major', axis='both')
            #plt.show()
            plt.savefig(lj[0:8] + "pr" + "-" + lj[8:], dpi=800)
            plt.close('all')

           
            
            
            
            #读取固定支座墩台力及其对应的纵向位移和纵向力数组
            f = open(lj + "\\pd.dat") 
            line = f.readline()
            zhizuo_n = np.array([])#桥梁固定支座编号，从计算模型左台开始，依次自动编号输出；
            zhizuo_weiyi = np.array([])#对应墩台顶固定支座纵向位移，向右为正，单位：mm;
            zhizuo_force = np.array([])#对应墩台顶固定支座纵向力，向右为正，单位：kN;
            while line:
                n = float(line[0:12])
                zhizuo_n = np.append(zhizuo_n, n)
                weiyi = float(line[12:24])
                zhizuo_weiyi = np.append(zhizuo_weiyi, weiyi)
                force = float(line[24:36])
                zhizuo_force = np.append(zhizuo_force, force)      
                line = f.readline()
            f.close()
 
            
            #绘制固定支座纵向力柱状图
            X = zhizuo_n
            Y = zhizuo_force
            plt.bar(X,Y,width = 1.0,facecolor = 'lightskyblue',edgecolor = 'white',align = 'center')
            #给图加text
            for x,y in zip(X,Y):
                plt.text(x, y+0.12, '%.0f' % y, ha='center', va= 'bottom')
            plt.title(u'墩台力', fontproperties=font)
            plt.xlabel(u'墩台编号', fontproperties=font)
            plt.ylabel(u'墩台力(kN)', fontproperties=font)
            plt.xlim(0,len(X)+1)
            plt.ylim(np.min(Y),np.max(Y)+100)
            plt.xticks(np.arange(len(X)+1))
            A = 100.0#y坐标的刻度间隔为100.0
            plt.yticks(np.arange(np.min(Y//A)*A,np.max(Y//A)*A+0.2*A,A))
            plt.grid(b=True, which='major', axis='both')
            #plt.show()
            plt.savefig(lj[0:8] + "pd-force" + "-" + lj[8:], dpi=800)            
            plt.close('all')
            
            
            
            
            #绘制固定支座及其对应的纵向位移柱状图
            #X是固定支座所在墩的编号
            X = zhizuo_n
            Y = zhizuo_weiyi
            plt.bar(X,Y,width = 1.0,facecolor = 'lightskyblue',edgecolor = 'white',align = 'center')
            #给图加text
            for x,y in zip(X,Y):
                plt.text(x, y+0.05, '%.1f' % y, ha='center', va= 'bottom')
            plt.title(u'墩台位移', fontproperties=font)
            plt.xlabel(u'墩台编号', fontproperties=font)
            plt.ylabel(u'墩台位移(mm)', fontproperties=font)
            plt.xlim(0,len(X)+1)
            plt.ylim(np.min(Y),np.max(Y)+1)
            plt.xticks(np.arange(len(X)+1))
            A = 1.0#y坐标的刻度间隔为1.0
            plt.yticks(np.arange(np.min(Y//A)*A,np.max(Y//A)*A+0.2*A,A))
            plt.grid(b=True, which='major', axis='both')
            #plt.show()
            plt.savefig(lj[0:8] + "pd-weiyi" + "-" + lj[8:], dpi=800)            
            plt.close('all')
            

            
            
            
            
            #读取对应桥梁梁体单元节点距左桥台距离、梁体单元节点与长轨条的纵向相对位移数组
            f = open(lj + "\\bru.dat") 
            line = f.readline()
            bridge_juli = np.array([])#桥梁梁体单元节点距左桥台距离，向右为正，单位：m；
            bridge_jdweiyi = np.array([])#桥梁梁体单元节点绝对纵向位移，向右为正，单位：mm；
            bridge_xdweiyi = np.array([])#梁体单元节点与长轨条的纵向相对位移，向右为正，单位：mm;
            while line:
                juli = float(line[0:12])
                bridge_juli = np.append(bridge_juli, juli)
                jdweiyi = float(line[12:24])
                bridge_jdweiyi = np.append(bridge_jdweiyi, jdweiyi)
                xdweiyi = float(line[24:36])
                bridge_xdweiyi = np.append(bridge_xdweiyi, xdweiyi)    
                line = f.readline()
            f.close()
            
            #绘制梁体单元节点位移随梁体节点距左桥台距离的变化图
            plt.title(u'梁单元上翼缘纵向位移', fontproperties=font)
            plt.xlabel(u'L(m)', fontproperties=font)
            plt.ylabel(u'梁单元上翼缘纵向位移(mm)', fontproperties=font)
            A = 100.0#X坐标的刻度间隔
            X = bridge_juli
            plt.xticks(np.arange(np.min(X//A)*A,np.max(X//A)*A+0.2*A,A))
            plt.plot(bridge_juli, bridge_jdweiyi, 'r-', linewidth=1)
            plt.grid(b=True, which='major', axis='both')
            #plt.show()
            plt.savefig(lj[0:8] + "bridge_jdweiyi" + "-" + lj[8:], dpi=800)
            plt.close('all')
            
            #绘制梁体单元节点与长轨条的纵向相对位移随梁体节点距左桥台距离的变化图
            plt.title(u'梁轨相对位移', fontproperties=font)
            plt.xlabel(u'L(m)', fontproperties=font)
            plt.ylabel(u'梁轨相对位移(mm)', fontproperties=font)
            A = 100.0#X坐标的刻度间隔
            X = bridge_juli
            plt.xticks(np.arange(np.min(X//A)*A,np.max(X//A)*A+0.2*A,A))
            plt.plot(bridge_juli, bridge_xdweiyi, 'r-', linewidth=1)
            plt.grid(b=True, which='major', axis='both')
            #plt.show()
            plt.savefig(lj[0:8] + "bridge_xdweiyi" + "-" + lj[8:], dpi=800)
            plt.close('all')
            
            
            
            
            #读取长轨条各单元距左台距离、长轨条各单元节点纵向位移数组
            f = open(lj + "\\ru.dat") 
            line = f.readline()
            rail_juli = np.array([])#长轨条各单元距左台距离，向右为正，单位：m；
            rail_jdweiyi = np.array([])#长轨条各单元节点纵向位移，向右为正，单位：mm；
            while line:
                juli = float(line[0:12])
                rail_juli = np.append(rail_juli, juli)
                jdweiyi = float(line[12:24])
                rail_jdweiyi = np.append(rail_jdweiyi, jdweiyi) 
                line = f.readline()
            f.close()
            
            #绘制梁体单元节点与长轨条的纵向相对位移随梁体节点距左桥台距离的变化图
            plt.title(u'钢轨纵向位移', fontproperties=font)
            plt.xlabel(u'L(m)', fontproperties=font)
            plt.ylabel(u'钢轨纵向位移(mm)', fontproperties=font)
            A = 100.0#X坐标的刻度间隔
            X = rail_juli
            plt.xticks(np.arange(np.min(X//A)*A,np.max(X//A)*A+0.2*A,A))
            plt.plot(rail_juli, rail_jdweiyi, 'r-', linewidth=1)
            plt.grid(b=True, which='major', axis='both')
            #plt.show()
            plt.savefig(lj[0:8] + "rail_jdweiyi" + "-" + lj[8:], dpi=800)
            plt.close('all')
 
        
        
        
        


    def result_worst(self):
        """找到最不利结果"""
        f = open("D:\\BCWR\\SSL_rail_force_max.txt",'r') 
        line = f.readline()
        SSL_rail_force_max = np.array([])#
        while line:
            ZDL_min = float(line[0:12])
            SSL_rail_force_max = np.append(SSL_rail_force_max, ZDL_min)   
            line = f.readline()
        f.close()      
        f0 = open("D:\\BCWR\\SSL_rail_force_max.txt",'r')
        A = f0.readlines()
        f0.close()
        SSLmax = A[np.argmax(SSL_rail_force_max)]
        self.SSL_max.setText(SSLmax)
        
        
        
        f = open("D:\\BCWR\\SSL_rail_force_min.txt",'r') 
        line = f.readline()
        SSL_rail_force_min = np.array([])#
        while line:
            ZDL_min = float(line[0:12])
            SSL_rail_force_min = np.append(SSL_rail_force_min, ZDL_min)   
            line = f.readline()
        f.close() 
        f0 = open("D:\\BCWR\\SSL_rail_force_min.txt",'r')
        A = f0.readlines()
        f0.close()
        SSLmin = A[np.argmin(SSL_rail_force_min)]
        self.SSL_min.setText(SSLmin)        
        
        
        
        
        f = open("D:\\BCWR\\NQL_rail_force_max.txt",'r') 
        line = f.readline()
        NQL_rail_force_max = np.array([])#
        while line:
            ZDL_min = float(line[0:12])
            NQL_rail_force_max = np.append(NQL_rail_force_max, ZDL_min)   
            line = f.readline()
        f.close()
        
        f0 = open("D:\\BCWR\\NQL_rail_force_max.txt",'r')
        A = f0.readlines()
        f0.close()
        NQLmax = A[np.argmax(NQL_rail_force_max)]
        self.NQL_max.setText(NQLmax)



        f = open("D:\\BCWR\\NQL_rail_force_min.txt",'r') 
        line = f.readline()
        NQL_rail_force_min = np.array([])#
        while line:
            ZDL_min = float(line[0:12])
            NQL_rail_force_min = np.append(NQL_rail_force_min, ZDL_min)   
            line = f.readline()
        f.close()
        f0 = open("D:\\BCWR\\NQL_rail_force_min.txt",'r')
        A = f0.readlines()
        f0.close()
        NQLmin = A[np.argmin(NQL_rail_force_min)]
        self.NQL_min.setText(NQLmin)
        
        
        f = open("D:\\BCWR\\ZDL_rail_force_max.txt",'r') 
        line = f.readline()
        ZDL_rail_force_max = np.array([])#
        while line:
            ZDL_min = float(line[0:12])
            ZDL_rail_force_max = np.append(ZDL_rail_force_max, ZDL_min)   
            line = f.readline()
        f.close()
        f0 = open("D:\\BCWR\\ZDL_rail_force_max.txt",'r')
        A = f0.readlines()
        f0.close()
        ZDLmax = A[np.argmax(ZDL_rail_force_max)]
        self.ZDL_max.setText(ZDLmax)        
        
        
        
        
        f = open("D:\\BCWR\\ZDL_rail_force_min.txt",'r') 
        line = f.readline()
        ZDL_rail_force_min = np.array([])#
        while line:
            ZDL_min = float(line[0:12])
            ZDL_rail_force_min = np.append(ZDL_rail_force_min, ZDL_min)   
            line = f.readline()
        f.close()
        
        f0 = open("D:\\BCWR\\ZDL_rail_force_min.txt",'r')
        A = f0.readlines()
        f0.close()
        ZDLmin = A[np.argmin(ZDL_rail_force_min)]
        self.ZDL_min.setText(ZDLmin)




#Instantiate and pop up the window.
bcwr_ansys().mainloop()  
        
        
        
        
        
        
        
        