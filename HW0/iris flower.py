import numpy as np
import pandas as pd

df = pd.DataFrame(pd.read_csv('/Users/sunxiran/Desktop/iris.data.csv',header=None))##remember to change the file path!^.^
data = df.values
data.shape #for this, we got the shape of the array

from matplotlib import pyplot as plt
import numpy as np
import random

f1=[] ## f1 for the first attributes of the samples
f2=[]
colors=[]  ## for colors
a = raw_input("Enter your input number, range 1-150: ");  
a = int(a)
b = raw_input("enter the first attribute as x_lable, from0-3");
b = int(b)
c = raw_input("enter the second attribute as y_lable, from0-3, but cannot be the same num as b");
c = int(c)
h=[]

for j in range(0, a): ## get the points we wanna show in the figure, and just change the number of 
    i = random.randint(0,149)
    while(i in h):
        i = random.randint(0,149)
    f1.append(data[i,b]) ## change the number of 0, and 1 in the next row we can get different combination
    f2.append(data[i,c])
    color={}    ## get the color (same color with the same type of flower)
    if data[i,4] == 'Iris-setosa':
        colors.append('r')
    elif data[i,4] == 'Iris-versicolor':
        colors.append('b')
    else:
        colors.append('g')
    h.append(i)

if b == 0:
    plt.xlabel("sepal length/cm") 
elif b == 1:
    plt.xlabel("sepal width/cm")
elif b == 2:
    plt.xlabel("petal length/cm")
else:
    plt.xlabel("petal width/cm")
    
if c == 0:
    plt.ylabel("sepal length/cm") 
elif c == 1:
    plt.ylabel("sepal width/cm")
elif c == 2:
    plt.ylabel("petal length/cm")
else:
    plt.ylabel("petal width/cm")
    
    
plt.scatter(f1, f2,c=colors)
plt.savefig('plot.png')