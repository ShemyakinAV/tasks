import sys as s
import numpy as np
import os
for x in s.argv:
    path = s.argv[1]
os.chdir(path)
arr1 = np.loadtxt("Cash1.txt", delimiter = '\n', dtype=np.float)
arr2 = np.loadtxt("Cash2.txt", delimiter = '\n', dtype=np.float)
arr3 = np.loadtxt("Cash3.txt", delimiter = '\n', dtype=np.float)
arr4 = np.loadtxt("Cash4.txt", delimiter = '\n', dtype=np.float)
arr5 = np.loadtxt("Cash5.txt", delimiter = '\n', dtype=np.float)
finalarray = np.array([max(arr1),max(arr2),max(arr3),max(arr4),max(arr5)])
print(max(finalarray))
