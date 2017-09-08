
"""
Created on Sun Jun 12 21:21:49 2016

@author: Hossam
"""

import pandas
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import matplotlib.lines as mlines



data = pandas.read_csv('Accuracy.csv')

    
plt.figure(figsize=(8,5))          
labels=list(data.columns.values)
          
data3= data.as_matrix()
axes   = plt.subplot(111)

   
box=plt.boxplot(data3, labels=labels, patch_artist=True)

colors = ['red', 'blue', 'green', 'pink']
for patch, color in zip(box['boxes'], colors):
    patch.set_facecolor(color)
    
    
#plt.xlabel('Classifier')


#plt.xlabel('xlabel', fontsize=22)
plt.ylabel('Accuracy', fontsize=22)

#ax.xaxis.set_tick_params(labelsize=14)
plt.tick_params(labelsize=22)


    
plt.grid()

plt.savefig('Data1.pdf', format='pdf', dpi=1000,bbox_inches='tight')

plt.show()
   
