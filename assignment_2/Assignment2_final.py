# -*- coding: utf-8 -*-
"""
Created on Mon May 18 20:48:16 2020

@author: SC
"""
import numpy as np
import matplotlib.pyplot as plt
import math

read_data = open("slice150.raw","rb")

data_arr = np.zeros((512,512))
for i in np.arange(0,512):
    for j in np.arange(0,512):
        data_arr[i][j] = int.from_bytes(read_data.read(2), byteorder='little')


fig, axes = plt.subplots(3, 2, figsize=(16,20))

# task(a) Profile line    

X_SCALE = []
k = 0
for i in range(0,512):
    k += 1
    X_SCALE.append(k)

axes[0, 0].plot(X_SCALE, data_arr[256])
axes[0, 0].set_title("256 profile line")




# task(b) Mean  and variance values   

mean_data_set = np.mean(data_arr)

variance_data_set = np.var(data_arr)



# task(c) histogram of 2D Data set   

hist_arr = data_arr.flatten()
bi = int(np.max(hist_arr)-np.min(hist_arr))+1

axes[0, 1].hist(hist_arr, bins=bi, histtype='step')
axes[0, 1].set_title("histogram")



# task(d) linear Transformation   

lin_data = np.zeros((512,512))
rmax = np.max(data_arr)
for m in np.arange(0,512):
    for n in np.arange(0,512):
        r = data_arr[m][n]
        lin_data[m][n] = ((r/rmax) * 255)

axes[1, 0].imshow(lin_data,cmap=plt.cm.gray)
axes[1, 0].set_title("linear transformation")



# task(e) Non linear Transformation  

non_lin_data = np.zeros((512,512))
rmax = np.max(data_arr)
for x in np.arange(0,512):
    for y in np.arange(0,512):
        r = data_arr[x][y]
        non_lin_data[x][y] = math.log2(r + 1)

axes[1, 1].imshow(non_lin_data,cmap=plt.cm.gray)
axes[1, 1].set_title("non linear transformation")



# task(f) boxcar smoothing filter
   
box_arr = np.array(data_arr)
for k in np.arange(0,502):
    for l in np.arange(0,502):
        sub2DArr = np.sum(box_arr[k:k+11, l:l+11])
        box_arr[k+5,l+5] = sub2DArr/121
        
axes[2, 0].imshow(box_arr,cmap=plt.cm.gray)
axes[2, 0].set_title("Boxcar smoothing filter")



# task(g) Median filter 

med_arr = np.array(data_arr)
for u in np.arange(0,502):
    for v in np.arange(0,502):
        sub2DArr = med_arr[u:u+11, v:v+11]
        sorted_array = np.sort(sub2DArr.flatten())
        med_arr[u+5,v+5] = sorted_array[60]
        
axes[2, 1].imshow(med_arr,cmap=plt.cm.gray)
axes[2, 1].set_title("Median filter")


plt.savefig('assignment2.png',dpi=170, bbox_inches='tight')
