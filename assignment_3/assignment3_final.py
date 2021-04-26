# -*- coding: utf-8 -*-
"""
Created on Tue Jun  2 23:38:33 2020

@author: SC
"""


import matplotlib.pyplot as plt
import numpy as np
import csv
import math

fig, axes = plt.subplots(4, 2, figsize=(16,20))

equalized_array = []
with open("i170b2h0_t0.txt","r") as f:
    reader = csv.reader(f)
    for row in reader:
        for k in row: 
            
            equalized_array.append(float(k))
            
            
            
b = np.array(equalized_array)
arr = b.reshape(500,500)

m = 0
band_2_arr = np.zeros((500,500))
for i in reversed(range(500)):
    for j in range(0,500):
        band_2_arr[i][j] = arr[m][j]
    m += 1


# task(a) min, max, mean and variance of band2

max_band2 = np.max(band_2_arr)

min_band2 = np.min(band_2_arr)

mean_band2 = np.mean(band_2_arr)

variance_band2 = np.var(band_2_arr)



# task(b) profile line through maximum value of band2 data set

result = np.where(band_2_arr == np.max(band_2_arr))
c = result[0]
row_value = c[0]

X = []
k= 0
for i in range(0,500):
    k += 1
    X.append(k)

axes[0, 0].plot(X, band_2_arr[row_value])
axes[0, 0].set_title("profile line")


# task(c) histogram band2 data set

data_arr = band_2_arr.flatten()

data_dict = {}
uniq_arr = np.unique(band_2_arr)
for k in uniq_arr:
     count_data = np.count_nonzero(band_2_arr == k)
     data_dict[k] = count_data
key_data = []
count_data = []
for key, value in data_dict.items():
    key_data.append(key)
    count_data.append(value)

axes[0, 1].plot(count_data)
axes[0, 1].set_title("Histogram of Band 2")

# task(d) rescale 0 to 255 (linear transforamtion) band 2 

k=0
l=0
rescale_arr = np.zeros((500,500))
rmax=np.max(band_2_arr)
for k in np.arange(0,500):
    for l in np.arange(0,500):
        r = band_2_arr[k][l]
        rescale_arr[k][l] = ((r/rmax) * 255)

im =axes[1, 0].imshow(rescale_arr,cmap=plt.cm.gray)
axes[1, 0].set_title("rescale band 2")


# task(e) Histogram equalization of all bands

def draw_histo(band_name,file,x,y):
    equalized_array = []
    with open(file,"r") as f:
        reader = csv.reader(f)
        for row in reader:
            for k in row: 
                equalized_array.append(float(k))



    b = np.array(equalized_array)
    arr = b.reshape(500,500)

    m = 0
    band_1_arr = np.zeros((500,500))
    for i in reversed(range(500)):
        for j in range(0,500):
    #         print(m)
    #         print(j)
            band_1_arr[i][j] = arr[m][j]
        m += 1



    newdict = {}
    cdf = 0
    sorted_arr = sorted(band_1_arr.flatten())
    uniq_arr =np.unique(sorted_arr)
    for m in uniq_arr:
        prob = np.count_nonzero(band_1_arr == m)
        prob_r = float(prob/250000)
        cdf = cdf + prob_r
        new_val = round(cdf * 255)
        newdict[m] = int(new_val)

    for m in range(0,500):
        for n in range(0,500):
            band_1_arr[m][n] = newdict[band_1_arr[m][n]]


    name_band = "Histogram Equalization of Band "+str(band_name)
    axes[x, y].imshow(band_1_arr,cmap=plt.cm.gray)
    axes[x, y].set_title(name_band)
    return band_1_arr


histo_equalization_band1 = draw_histo(1,"i170b1h0_t0.txt",1,1)
histo_equalization_band2 = draw_histo(2,"i170b2h0_t0.txt",2,0)
histo_equalization_band3 = draw_histo(3,"i170b3h0_t0.txt",2,1)
histo_equalization_band4 = draw_histo(4,"i170b4h0_t0.txt",3,0)

# task(f) RGB color Transformation 


rgb_arr = np.dstack([histo_equalization_band4, histo_equalization_band3, histo_equalization_band1]).reshape(500, 500, 3)
axes[3, 1].imshow(rgb_arr.astype(int))
axes[3, 1].set_title("color transformation")

fig.colorbar(im, ax=axes[1, 0],ticks=[np.min(rescale_arr), np.max(rescale_arr)], orientation='vertical')
plt.savefig('assignment3.png',dpi=150, bbox_inches='tight')