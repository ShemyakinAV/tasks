import sys as s
import numpy as np
path1 = 'input1.txt'
txtfile1=open(path1,'r')
arr1 = np.loadtxt(path1, delimiter = ' ', dtype=np.float)
x1=(arr1[0][0])
y1=(arr1[0][1])
x2=(arr1[1][0])
y2=(arr1[1][1])
x3=(arr1[2][0])
y3=(arr1[2][1])
x4=(arr1[3][0])
y4=(arr1[3][1])
path2 = 'input2.txt'
txtfile2=open(path2,'r')
arr2 = np.loadtxt(path2, delimiter = ' ', dtype=np.float)
for i in range(len(arr2)):
   for j in range(len(arr2[i])):
      if(arr2[i][j]==x1 and arr2[i][j]==y1):
         print(0, end = ' ')
