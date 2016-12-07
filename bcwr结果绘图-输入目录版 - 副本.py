# -*- coding: utf-8 -*-
"""
Created on Sat Oct  8 16:47:51 2016

@author: zhanggaoyang
"""
#导入需要的模块
from breezypythongui import EasyFrame
import numpy as np
from matplotlib import pyplot as plt
from matplotlib.font_manager import FontProperties
font = FontProperties(fname=r"c:\windows\fonts\simsun.ttc", size=14)


class bcwr_Plot(EasyFrame):
    """Application window for the 动弯应力."""
 
    def __init__(self):
        """Sets up the window and the widgets."""
        EasyFrame.__init__(self, title = 'bcwr结果图')

        # Label and field for the 结果所在的路径
        self.addLabel(text = "结果所在的路径：",
                      row = 0, column = 0)
        self.lujing = self.addTextArea("F:\\TZY\\bcwr", 
                                    row = 0, column = 1,
                                    columnspan = 5,
                                    width = 140, height = 2)

        # The command button1
        self.addButton(text = "绘制结果图", row = 1, column = 0,
                       command = self.plot)
 
            # The event handler method for the button
    def plot(self):
        """Obtains the data from the input fields and uses
        them to check 动弯应力."""
        lujing = self.lujing.getText()
        lujing = lujing.strip()
        #读取钢轨纵向力和距离左桥台距离数组
        f = open(lujing + "\\pr.dat") 
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
        plt.savefig(lujing + "\\pr", dpi=800)
        plt.close('all')
        
        
        
        
        #读取固定支座墩台定及其对应的纵向位移和纵向力数组
        f = open(lujing + "\\pd.dat") 
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
        plt.savefig(lujing + "\\pd-weiyi", dpi=800)
        plt.close('all')
        
        #绘制固定支座纵向力柱状图
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
        plt.savefig(lujing + "\\pd-force", dpi=800)
        plt.close('all')
        
        
        
        
        #读取对应桥梁梁体单元节点距左桥台距离、梁体单元节点与长轨条的纵向相对位移数组
        f = open(lujing + "\\bru.dat") 
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
        plt.savefig(lujing + "\\bridge_jdweiyi", dpi=800)
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
        plt.savefig(lujing + "\\bridge_xdweiyi", dpi=800)
        plt.close('all')
        
        
        
        
        #读取长轨条各单元距左台距离、长轨条各单元节点纵向位移数组
        f = open(lujing + "\\ru.dat") 
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
        plt.savefig(lujing + "\\rail_jdweiyi", dpi=800)
        plt.close('all')

#Instantiate and pop up the window.
bcwr_Plot().mainloop()
