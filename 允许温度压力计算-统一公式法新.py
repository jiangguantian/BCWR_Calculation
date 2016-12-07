# -*- coding: utf-8 -*-
"""
Created on Wed Sep 21 14:52:20 2016

@author: zhanggaoyang
"""

#所有数字均需写成浮点数，不能出现整数，出现整数会导致除法运算出错！很重要！很重要！很重要！
import sys
versionNumber = sys.version_info.major
if versionNumber == 2:
    from Tkinter import HORIZONTAL
else:
    from tkinter import HORIZONTAL


from breezypythongui import EasyFrame
from breezypythongui import DISABLED
import numpy as np


class delt_Tc(EasyFrame):
    """Application window for the 允许温度压力."""
 
    def __init__(self):
        """Sets up the window and the widgets."""
        EasyFrame.__init__(self, title = '允许温度压力计算')

        # Label and field for the 曲线半径R
        self.addLabel(text = "曲线半径R（m）(直线输入：0.0,且均须带小数)：",
                      row = 0, column = 0)
        self.R = self.addFloatField(value = 0.0,
                                              precision = 1,
                                              row = 0,
                                              column = 1)
        # Label and field for the 桥上或道岔上的附加压力P(kN)
        self.addLabel(text = "桥上或道岔上的附加压力P(kN)：",
                      row = 1, column = 0)
        self.Pf = self.addFloatField(value = 0.0,
                                              precision = 3,
                                              row = 1,
                                              column = 1)
        # Label and field for the 稳定性安全系数K
        self.addLabel(text = "稳定性安全系数K：",
                      row = 2, column = 0)
        self.K = self.addFloatField(value = 1.3,
                                              precision = 1,
                                              row = 2,
                                              column = 1) 
        # Label and field for the 钢轨类型
        self.addLabel(text = "钢轨类型：",
                      row = 3, column = 0)
        # Add the button group1
        self.group1 = self.addRadiobuttonGroup(row = 3, column = 1,
                                              columnspan = 4,
                                              orient = HORIZONTAL)

        # Add the radio buttons to the group
        self.group1.addRadiobutton("Rail-50")
        defaultRB1 = self.group1.addRadiobutton("Rail-60")
        self.group1.addRadiobutton("Rail-75")


        # Select one of the buttons in the group
        self.group1.setSelectedButton(defaultRB1)


        # Label and field for the 道床横向阻力类型
        self.addLabel(text = "道床横向阻力类型：",
                      row = 4, column = 0)
        # Add the button group2
        self.group2 = self.addRadiobuttonGroup(row = 4, column = 1,
                                              columnspan = 4,
                                              orient = HORIZONTAL)

        # Add the radio buttons to the group
        self.group2.addRadiobutton("2-1760/km")
        self.group2.addRadiobutton("2-1840/km")
        defaultRB2 = self.group2.addRadiobutton("3-1667/km")

        # Select one of the buttons in the group
        self.group2.setSelectedButton(defaultRB2)


        # The command button1
        self.addButton(text = "开始计算", row = 5, column = 0,
                       command = self.compute)


        # Output field and command button for the results
        self.addLabel(text = "结果1：临界温度压力值(kN)",
                      row = 6, column = 0, foreground = "red")
        self.Pw = self.addFloatField(value = 0.0,
                                          precision = 1,                                             
                                          row = 6,
                                          column = 1)         
        self.addLabel(text = "结果2：允许温度压力值(kN)",
                      row = 7, column = 0, foreground = "red")
        self.P_allow = self.addFloatField(value = 0.0,
                                          precision = 1,                                             
                                          row = 7,
                                          column = 1)
        self.addLabel(text = "结果3：允许温升(℃)",
                      row = 8, column = 0, foreground = "red")        
        self.delt_Tc = self.addFloatField(value = 0.0,
                                          precision = 1,                                             
                                          row = 8,
                                          column = 1)
        self.addLabel(text = "结果4：试算得到的轨道弯曲半波长L(cm)",
                      row = 9, column = 0, foreground = "red")        
        self.L = self.addFloatField(value = 0.0,
                                          precision = 1,                                             
                                          row = 9,
                                          column = 1)

        
    # The event handler method for the button
    def compute(self):
        """Obtains the data from the input fields and uses
        them to calculate 允许温度压力."""
        try:
            R = 100 * self.R.getNumber()#(cm)
            Pf = 1000 * self.Pf.getNumber()#(N)           
        except ValueError:
            self.messageBox(title = "错误",
                            message = "请输入数字！") 
        if R == 0.0:
            R_daoshu = 0
        else:
            R_daoshu = 1 / R
            
        if self.group1.getSelectedButton()["value"] == "Rail-50":
            Iy = 377#cm^4
            F = 65.8#cm²
        if self.group1.getSelectedButton()["value"] == "Rail-60":
            Iy = 524#cm^4
            F = 77.45#cm²
        if self.group1.getSelectedButton()["value"] == "Rail-75":
            Iy = 661#cm^4
            F = 95.04#cm²
            
        if self.group2.getSelectedButton()["value"] == "2-1760/km":
            Q = 85#N/cm
        if self.group2.getSelectedButton()["value"] == "2-1840/km":
            Q = 89#N/cm
        if self.group2.getSelectedButton()["value"] == "3-1667/km":
            Q = 115#N/cm            

        Rop_daoshu = 1.39639 * 10 ** (-5)
        Rpie_daoshu = R_daoshu + Rop_daoshu
        t = 3.575 * 10 ** (-7)
        beita = 1.0
        E = 2.1 * 10 ** 7
        f = 0.2
        w = 2 * beita * E * Iy * np.pi**2 * (t + 4 * Rpie_daoshu / np.pi**3)
        lfang = (w + np.sqrt(w**2 + (4*Q / np.pi**3 - w*t/f)*2 * f * beita * E * Iy * np.pi**2)) / (4*Q / np.pi**3 - w*t/f)
        L = np.sqrt(lfang)
        Pw = (2 * beita * E * Iy * np.pi**2 * (f + t * lfang) / lfang + 4*Q  * lfang / np.pi**3) / (f + t * lfang + 4*lfang / np.pi**3 * Rpie_daoshu)
        K = 1.3
        P_allow = Pw / K
        alpha = 1.18 * 10**(-5)
        delt_Tc = (P_allow / 2.0 - Pf) / (E * F * alpha)
        self.Pw.setNumber(Pw/1000.0)        
        self.P_allow.setNumber(P_allow/1000.0)
        self.delt_Tc.setNumber(delt_Tc)
        self.L.setNumber(L)

#Instantiate and pop up the window.
delt_Tc().mainloop()
