#!/usr/bin/env python
# coding: utf-8

# In[19]:


import matplotlib.pyplot as plt
import math
from matplotlib import cm


# In[20]:


vector_array=[]
data_file = open("field2.irreg.txt","r") 
data_file.readline()
data_file.readline()
data_file.readline()
data_file.readline()
data_file.readline()
data_file.readline()
for row_data in data_file: 
    split_data = row_data.split(" ")
    vector_array.append(split_data)


# In[21]:


X_DIM = []
Y_DIM = []
Z_DIM = []
U_DIM = []
V_DIM = []
W_DIM = []
C_DIM = []
for data_dim in vector_array:
    X_DIM.append(float(data_dim[0]))
    Y_DIM.append(float(data_dim[1]))
    Z_DIM.append(float(data_dim[2]))
    U_DIM.append(float(data_dim[3]))
    V_DIM.append(float(data_dim[4]))
    W_DIM.append(float(data_dim[5]))
    C_DIM.append(math.sqrt(math.pow(float(data_dim[3]),2) + math.pow(float(data_dim[4]),2)))


# In[22]:


fig, ax = plt.subplots()
cax = ax.quiver(X_DIM,Y_DIM,U_DIM,V_DIM,C_DIM,cmap='jet',scale=4,headaxislength =4)
ax.set_title('Vector Field Visualization')
clr_bar = fig.colorbar(cax, ticks=[0, 0.5,1],label='Flow Velocity')
clr_bar.ax.set_yticklabels(['Low', 'Medium', 'High'])
plt.xlabel("X Equivalent of Vectors")
plt.ylabel("Y Equivalent of Vectors")
plt.savefig('flow_vel_plot.png', dpi=300, bbox_inches='tight')







