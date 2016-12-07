# -*- coding: utf-8 -*-
"""
Created on Wed Sep 21 14:52:20 2016

@author: zhanggaoyang
"""
#2016年11月8日改正重力加速度为9.8m/s^2
#所有数字均需写成浮点数，不能出现整数，出现整数会导致除法运算出错！很重要！很重要！很重要！
from breezypythongui import EasyFrame
import numpy as np


class Sigma_Check(EasyFrame):
    """Application window for the 动弯应力."""
 
    def __init__(self):
        """Sets up the window and the widgets."""
        EasyFrame.__init__(self, title = '动弯应力检算')

        # Label and field for the 轴重
        self.addLabel(text = "轴重（t）",
                      row = 0, column = 0)
        self.zhouzhong = self.addFloatField(value = 17.0,
                                              precision = 1,
                                              row = 0,
                                              column = 1)
        # Label and field for 转向架轴数
        self.addLabel(text = "轴数(n=2.0,3.0or4.0)",
                      row = 0, column = 2)
        self.zhoushu = self.addFloatField(value = 2.0,
                                             precision = 1,                                         
                                             row = 0,
                                             column = 3) 
        # Label and field for the 轴距
        self.addLabel(text = "轴距(m)",
                      row = 0, column = 4)
        self.zhouju = self.addFloatField(value = 2.5,
                                              precision = 1,                                             
                                              row = 0,
                                              column = 5)

        # Label and field for the 钢轨支点刚度
        self.addLabel(text = "钢轨支点刚度(kN/mm)",
                      row = 1, column = 0)
        self.D = self.addFloatField(value = 33.0,
                                              precision = 3,                                         
                                              row = 1,
                                              column = 1)
        # Label and field for the 轨枕间距
        self.addLabel(text = "轨枕间距(m)",
                      row = 1, column = 2)
        self.a = self.addFloatField(value = 0.60,
                                              precision = 3,                                           
                                              row = 1,
                                              column = 3)                                                                          

        # Label and field for the 钢轨弹模Ex
        self.addLabel(text = "钢轨弹模Ex(GPa)",
                      row = 1, column = 4)
        self.Ex = self.addFloatField(value = 210.0,
                                              precision = 3,                                          
                                              row = 1,
                                              column = 5)

        # Label and field for the number of 钢轨惯性矩Ix
        self.addLabel(text = "钢轨惯性矩Ix(cm^4)",
                      row = 2, column = 0)
        self.Ix = self.addFloatField(value = 3069.0,
                                             precision = 3,                                           
                                             row = 2,
                                             column = 1) 

        # Label and field for the number of 轨头抗弯惯性矩W头
        self.addLabel(text = "轨头抗弯惯性矩W头(cm^3)",
                      row = 2, column = 2)
        self.W1 = self.addFloatField(value = 318.0,
                                             precision = 3,                                           
                                             row = 2,
                                             column = 3) 
        # Label and field for the number of 轨底抗弯惯性矩W底
        self.addLabel(text = "轨底抗弯惯性矩W底(cm^3)",
                      row = 2, column = 4)
        self.W2 = self.addFloatField(value = 385.0,
                                             precision = 3,                                           
                                             row = 2,
                                             column = 5) 

        # Label and field for the number of 速度系数a
        self.addLabel(text = "速度系数a",
                      row = 3, column = 0)
        self.alpha = self.addFloatField(value = 1.0,
                                             precision = 3,                                          
                                             row = 3,
                                             column = 1) 
        # Label and field for the 偏载系数β
        self.addLabel(text = "偏载系数β",
                      row = 3, column = 2)
        self.beita_p = self.addFloatField(value = 0.0,
                                              precision = 3,                                          
                                              row = 3,
                                              column = 3)

        # Label and field for the 横向水平力系数f
        self.addLabel(text = "横向水平力系数f",
                      row = 3, column = 4)
        self.f = self.addFloatField(value = 1.25,
                                              precision = 9,                                         
                                              row = 3,
                                              column = 5)

        # Label and field for the number of 钢轨的允许应力
        self.addLabel(text = "钢轨的允许应力(MPa)",
                      row = 4, column = 0)
        self.sigma_allow = self.addFloatField(value = 351.5,
                                             precision = 3,                                             
                                             row = 4,
                                             column = 1)







        # Label and field for the number of 轨头压应力(MPa)
        self.addLabel(text = "结果1：轨头压应力(MPa)",
                      row = 5, column = 0, foreground = "red")
        self.sigma_1d = self.addFloatField(value = 0.0,
                                          precision = 3,                                             
                                          row = 5,
                                          column = 1)
        # Label and field for the number of 轨底拉应力(MPa)
        self.addLabel(text = "结果2：轨底拉应力(MPa)",
                      row = 5, column = 2, foreground = "red")
        self.sigma_2d = self.addFloatField(value = 0.0,
                                          precision = 3,                                             
                                          row = 5,
                                          column = 3)
       

        # The command button1
        self.addButton(text = "开始检算", row = 5, column = 4,
                       command = self.check)



        
    # The event handler method for the button
    def check(self):
        """Obtains the data from the input fields and uses
        them to check 动弯应力."""
        try:
            zhouzhong = self.zhouzhong.getNumber()#(t)
            zhoushu = self.zhoushu.getNumber()#(m)            
            zhouju = self.zhouju.getNumber()#(m)
            D = self.D.getNumber()#(kN/mm)
            a = self.a.getNumber()#(m)
            Ex = self.Ex.getNumber()#(GPa)
            Ix = self.Ix.getNumber()#(cm^4)
            W1 = self.W1.getNumber()#(cm^3)
            W2 = self.W2.getNumber()#(cm^3)
            alpha = self.alpha.getNumber()
            beita_p = self.beita_p.getNumber()
            f = self.f.getNumber()
            sigma_allow = self.sigma_allow.getNumber()#(MPa)
        except ValueError:
            self.messageBox(title = "错误",
                            message = "请输入数字！") 
        k = D / a#MPa
        beita = (k / (4*Ex*Ix*10**7)) ** (1/4.0)
        x1 = 0
        x2 = zhouju*1*1000
        x3 = zhouju*2*1000
        #x4 = zhouju*3*1000#用不到
        if zhoushu < 2.5:
            M1 = (zhouzhong*10**3*9.8/2.0 * np.exp(-beita*x1)*(np.cos(beita*x1)-np.sin(beita*x1))) / (4*beita)
            M2 = (zhouzhong*10**3*9.8/2.0 * np.exp(-beita*x2)*(np.cos(beita*x2)-np.sin(beita*x2))) / (4*beita)
            M = M1 + M2
        if 2.5 < zhoushu < 3.5:
            M1 = (zhouzhong*10**3*9.8/2.0 * np.exp(-beita*x1)*(np.cos(beita*x1)-np.sin(beita*x1))) / (4*beita)
            M2 = (zhouzhong*10**3*9.8/2.0 * np.exp(-beita*x2)*(np.cos(beita*x2)-np.sin(beita*x2))) / (4*beita)
            M3 = (zhouzhong*10**3*9.8/2.0 * np.exp(-beita*x3)*(np.cos(beita*x3)-np.sin(beita*x3))) / (4*beita)
            M11 = M1 + M2 + M3
            M22 = M1 + 2*M2
            M = np.max((M11,M22))
        if 3.5 < zhoushu < 4.5:
            M1 = (zhouzhong*10**3*9.8/2.0 * np.exp(-beita*x1)*(np.cos(beita*x1)-np.sin(beita*x1))) / (4*beita)
            M2 = (zhouzhong*10**3*9.8/2.0 * np.exp(-beita*x2)*(np.cos(beita*x2)-np.sin(beita*x2))) / (4*beita)
            M3 = (zhouzhong*10**3*9.8/2.0 * np.exp(-beita*x3)*(np.cos(beita*x3)-np.sin(beita*x3))) / (4*beita)
            M4 = (zhouzhong*10**3*9.8/2.0 * np.exp(-beita*x3)*(np.cos(beita*x3)-np.sin(beita*x3))) / (4*beita)
            M11 = M1 + M2 + M3 + M4
            M22 = M1 + 2*M2 + M3
            M = np.max((M11,M22))        
        Md = M * (1 + alpha + beita_p) * f
        sigma_1 = Md / W1 /1000.0
        sigma_2 = Md / W2 /1000.0 
        self.sigma_1d.setNumber(sigma_1)
        self.sigma_2d.setNumber(sigma_2)
        if sigma_1 < sigma_allow and sigma_2 < sigma_allow:
            self.messageBox(title = "动弯应力合格！",
                            message = "你真棒！")
        else:
            self.messageBox(title = "动弯应力不合格！",
                            message = "回头看看哪里错了！")            



#Instantiate and pop up the window.
Sigma_Check().mainloop()
