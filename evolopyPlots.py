# -*- coding: utf-8 -*-
"""
Created on Sun Jun 12 21:21:49 2016

@author: Hossam
"""

import pandas
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import matplotlib.lines as mlines



#colnames = ['Algorithms','Benchmark','dim','Matlab','Python']
data = pandas.read_csv('EvoloPy-comparison.csv')

Algorithms = data.Algorithms.tolist()
Benchmark = data.Benchmark.tolist()
dim = data.dim.tolist()
Matlab = data.Matlab.tolist()
Python = data.Python.tolist()

j=0
for i in range(0,7):

    ax = plt.subplot(111)
    #matlab = [0.132672378,0.16617228,0.650739131,1.42639682,23.13139249,99.69769905,835.3820675]
    #python=[0.570000887, 1.070001602, 5.095007181, 10.24101567, 51.49507403,99.16014218,203.3912871]
    
    line1=plt.plot(Matlab[j:j+7-1],'bo-', linewidth=2 ,markersize=7,markeredgecolor='b',\
        fillstyle='none',markeredgewidth='2')
    line2=plt.plot(Python[j:j+7-1],'rs-',linewidth=2, markersize=7,markeredgecolor='r',\
        fillstyle='none',markeredgewidth='2')
    
    plt.xlabel('Dimension')
    plt.ylabel('Time (s)')
    
    
    
    
    blue_line = mlines.Line2D([], [], color='blue', marker='o',markersize=4, label='EvoloPy')
    red_line = mlines.Line2D([], [], color='red', marker='s',markersize=4, label='Matlab')
    
    
    plt.legend(handles=[blue_line ,red_line],loc=2)
    
    ax.set_xticklabels((50,100,500,1000,5000,10000,20000))
    
    plt.grid()
    
    plt.savefig(str(Algorithms[j])+'.eps', format='eps', dpi=1000)
    
    plt.show()
    j=j+7