import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

fo = open(r'D:\\Codes\\HelloWorld\ML\\2NodeNS\\RawSimpleSample.csv',mode='r')
Rawdata = fo.readlines()
data=[]
for k in Rawdata:
    data.append(list(map(float, k.rstrip('\n').split(',') )))

def Func(x):
    return x*1   #以该函数初始化
if(len(data[0])==3):
    for i in data:
        i.pop()
for i in data:
    if Func(i[0])>=i[1]:
        i.append(0)
    else:
        i.append(1)

data = np.asarray(data)
df = pd.DataFrame(data)
df.to_csv(r'D:\\Codes\\HelloWorld\ML\\2NodeNS\\SimpleSample.csv',header=None,index=None)


fig = plt.figure()
ax = fig.add_subplot(111)
X=np.linspace(0,10,256,endpoint=True)
for i in range(len(data)):
    ax.scatter(data[i,0],data[i,1],color="red" if data[i,2]==1 else "green")
plt.plot(X,Func(X),color="black")
plt.show()