# -*- coding: utf-8 -*-
"""
Created on Fri Jul 14 20:10:01 2017

@author: Hossam
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas



data = pandas.read_csv('sentiment.csv')

labels=list(data.columns.values)
data= data.as_matrix()



PublicationsCount = data[0,:]

N=12
ind = np.arange(N)  # the x locations for the groups

width = 0.35       # the width of the bars


plt.figure(figsize=(16,5)) 

s = plt.subplot(1,1,1)
rects1 = plt.bar(ind, PublicationsCount, width, color='#696969',edgecolor='black')




s.set_ylabel('Number of publications',fontsize=16)
#ax.set_title('Scores by group and gender')
s.set_xticks(ind)
s.set_xticklabels(labels)
s.tick_params(labelsize=18)

for a,b in zip(ind,PublicationsCount ):
    plt.text(a, b, str(b), fontsize=15)

#plt.grid()



plt.savefig('sentiment.pdf', format='pdf', dpi=1000,bbox_inches='tight')
  

plt.show()