import sys as s
import numpy as np
for x in s.argv:
    path=x
txtfile=open(path,'r')
arr = np.loadtxt(path, delimiter = '\n', dtype=np.int)
p = np.percentile(arr, 90)
m = np.median(arr)
print ("%.2f"%(p)+"\n"+
       "%.2f"%(m)+"\n"+
       "%.2f"%max(arr)+"\n"+
       "%.2f"%min(arr)+"\n"+
       "%.2f"%(np.mean(arr)))

