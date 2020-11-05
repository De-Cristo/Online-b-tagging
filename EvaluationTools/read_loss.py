#-*-coding:UTF-8 -*-
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

df_news = pd.read_table('./losses.log', header=None, delim_whitespace=True)
#print(df_news)

loss = []
val_loss = []

f=open('./losses.log')
GetLine = f.readlines()
for line in GetLine:
    temp1 = line.strip("\n")
    temp2 = temp1.split(" ")
    loss.append(float(temp2[0]))
    val_loss.append(float(temp2[1]))
'''
x = []
for i in range(1,51):
    x.append(i)


y1 = np.sin(x1)
print(y1)
'''
x = np.linspace(1,len(GetLine),len(GetLine))
#print(x)

#print(loss)
#plt.plot(x1,y1,"r",marker='*',ms=10,label="a")
plt.plot(x,loss,"r",marker='*',ms=10,label="loss")
plt.plot(x,val_loss,"b",marker='*',ms=10,label="val_loss")
plt.xlabel('Epoch')
plt.ylabel('loss')
plt.legend(['loss','val_loss'])
plt.show()

