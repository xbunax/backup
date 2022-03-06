import random
import numpy as np
arr = [i for i in range(0,12,2)]
arr1 = [i for i in range(0,12,2)]
n=0
x=[]
while True:
    n+=1
    random.shuffle(arr)
    if arr==sorted(arr1):
        print(n,arr)
        break
    else:
        print(n,arr)
