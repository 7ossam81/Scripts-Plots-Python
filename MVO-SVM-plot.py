# -*- coding: utf-8 -*-
"""
Created on Thu Jul 21 16:21:07 2016

@author: Hossam
"""

# -*- coding: utf-8 -*-
"""
Created on Sun Jun 12 21:21:49 2016

@author: Hossam
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import matplotlib.lines as mlines


dataset=['CancerI','HeartI','IonosphereI','SonarI','VehicleI','VowelI','WineI','GermanI']
allconv=np.loadtxt(open("convergence.csv","rb"),delimiter=",")


j=0
for i in range(0,8):

    ax = plt.subplot(111)
 
    line1=plt.plot(allconv[:,j],'bo-', linewidth=2 ,markersize=4,markeredgecolor='b',\
        fillstyle='none',markeredgewidth='2',markevery=5)
    line2=plt.plot(allconv[:,j+1],'rs-',linewidth=2, markersize=4,markeredgecolor='r',\
        fillstyle='none',markeredgewidth='2',markevery=5)
    line2=plt.plot(allconv[:,j+2],'gv-',linewidth=2, markersize=4,markeredgecolor='g',\
        fillstyle='none',markeredgewidth='2',markevery=5)
    line2=plt.plot(allconv[:,j+3],'m*-',linewidth=2, markersize=4,markeredgecolor='m',\
        fillstyle='none',markeredgewidth='2',markevery=5)
    line2=plt.plot(allconv[:,j+4],'cD-',linewidth=2, markersize=4,markeredgecolor='c',\
        fillstyle='none',markeredgewidth='2',markevery=5)
    
    
    
    plt.xlabel('Iteration')
    plt.ylabel('Fitness(Accuracy)')
    
    
    
    
    b_line = mlines.Line2D([], [], color='b',linewidth=2 , marker='o',markersize=4, label='MVO')
    r_line = mlines.Line2D([], [], color='r',linewidth=2, marker='s',markersize=4, label='GA')
    g_line = mlines.Line2D([], [], color='g',linewidth=2, marker='v',markersize=4, label='PSO')
    m_line = mlines.Line2D([], [], color='m',linewidth=2, marker='*',markersize=4, label='BAT')
    c_line = mlines.Line2D([], [], color='c',linewidth=2, marker='D',markersize=4, label='FF')

#    
#    
    plt.legend(handles=[b_line ,r_line,g_line,m_line,c_line],loc=4)
#    
#    ax.set_xticklabels((50,100,500,1000,5000,10000,20000))
    
    plt.grid()
    
    plt.savefig(str(dataset[i])+'.eps', format='eps', dpi=1000)
    
    plt.show()
    j=j+5