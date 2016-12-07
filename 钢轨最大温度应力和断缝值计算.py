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


class stress_and_lamda(EasyFrame):
    """Application window for the 温度应力及钢轨断缝值计算."""
 
    def __init__(self):
        """Sets up the window and the widgets."""
        EasyFrame.__init__(self, title = '温度应力及钢轨断缝值计算')

        # Label and field for the 钢轨类型
        self.addLabel(text = "钢轨类型：",
                      row = 0, column = 0)
        # Add the button group1
        self.group1 = self.addRadiobuttonGroup(row = 0, column = 1,
                                              columnspan = 4,
                                              orient = HORIZONTAL)

        # Add the radio buttons to the group
        self.group1.addRadiobutton("Rail-50")
        defaultRB1 = self.group1.addRadiobutton("Rail-60")
        self.group1.addRadiobutton("Rail-75")


        # Select one of the buttons in the group
        self.group1.setSelectedButton(defaultRB1)        
        
        
        
        # Label and field for the 当地最高气温
        self.addLabel(text = "当地最高气温(℃)(气温不是轨温)：",
                      row = 1, column = 0, foreground = "red")
        self.tmax = self.addFloatField(value = 58.9,
                                              precision = 1,
                                              row = 1,
                                              column = 1)
        # Label and field for the 当地最低气温
        self.addLabel(text = "当地最低气温(℃)：",
                      row = 2, column = 0)
        self.tmin = self.addFloatField(value = -26.9,
                                              precision = 1,
                                              row = 2,
                                              column = 1)
        # Label and field for the 设计锁定轨温
        self.addLabel(text = "设计锁定轨温(℃)：",
                      row = 3, column = 0)
        self.te = self.addFloatField(value = 20.0,
                                              precision = 1,
                                              row = 3,
                                              column = 1)        
        # Label and field for the 设计锁定轨温调整幅度
        self.addLabel(text = "设计锁定轨温调整幅度(℃)：",
                      row = 4, column = 0)
        self.delt_tk = self.addFloatField(value = 5.0,
                                              precision = 1,
                                              row = 4,
                                              column = 1)

        # Label and field for the 线路纵向阻力(kN/(m.轨))
        self.addLabel(text = "线路纵向阻力(kN/(m.轨))(务必保留小数)：",
                      row = 5, column = 0)
        self.r = self.addFloatField(value = 8.0,
                                              precision = 1,
                                              row = 5,
                                              column = 1)

        
        
        
        # The command button1
        self.addButton(text = "开始计算", row = 6, column = 0,
                       command = self.compute)


        # Output field and command button for the results
        self.addLabel(text = "结果1：钢轨最大温度压应力(MPa)",
                      row = 7, column = 0, foreground = "red")
        self.sigmat_ya_max = self.addFloatField(value = 0.0,
                                          precision = 3,                                             
                                          row = 7,
                                          column = 1)        
        self.addLabel(text = "结果2：钢轨最大温度拉应力(MPa)",
                      row = 8, column = 0, foreground = "red")
        self.sigmat_la_max = self.addFloatField(value = 0.0,
                                          precision = 3,                                             
                                          row = 8,
                                          column = 1)
        self.addLabel(text = "结果3：钢轨断缝值(mm)",
                      row = 9, column = 0, foreground = "red")        
        self.lamda = self.addFloatField(value = 0.0,
                                          precision = 1,                                             
                                          row = 9,
                                          column = 1)


        
    # The event handler method for the button
    def compute(self):
        """Obtains the data from the input fields and uses
        them to calculate 温度应力及钢轨断缝值计算."""
        try:
            tmax = self.tmax.getNumber()#(℃)
            tmin = self.tmin.getNumber()#(℃)
            te = self.te.getNumber()#(℃)
            delt_tk = self.delt_tk.getNumber()#(℃)        
            r = self.r.getNumber()#(kN/(m.轨))           
        except ValueError:
            self.messageBox(title = "错误",
                            message = "请输入数字！") 

        if self.group1.getSelectedButton()["value"] == "Rail-50":
            F = 65.8 * 10 ** 2#mm²
        if self.group1.getSelectedButton()["value"] == "Rail-60":
            F = 77.45 * 10 ** 2#mm²
        if self.group1.getSelectedButton()["value"] == "Rail-75":
            F = 95.04 * 10 ** 2#mm²            
            
            
        tmax = tmax + 20#最高轨温等于最高气温加20度    
        E = 2.1 * 10 ** 5
        alpha = 1.18 * 10 **(-5)
        delt_tu_max = tmax - (te - delt_tk)
        delt_td_max = (te + delt_tk) - tmin
        sigmat_ya_max = E * alpha * delt_tu_max
        sigmat_la_max = E * alpha * delt_td_max
        lamda = E * F * (alpha * delt_td_max) ** 2 / r
        self.messageBox(title = "错误",
                            message = '%s' % lamda)
     
        self.sigmat_ya_max.setNumber(sigmat_ya_max)        
        self.sigmat_la_max.setNumber(sigmat_la_max)
        self.lamda.setNumber(lamda)


#Instantiate and pop up the window.
stress_and_lamda().mainloop()
