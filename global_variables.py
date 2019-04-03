# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 20:54:30 2019

@author: Administrator
"""

import numpy as np
n_x=50
n_y=50
a=-5.0
b=5.0
c=-5.0
d=5.0
T=0.6
h_x=(b-a)/n_x
h_y=(d-c)/n_y
N=int(0.06*n_x)
delta_T=T/N
A=1.0
data_w=np.zeros((n_x+1, n_y+1), dtype=float)
data_s=np.zeros((n_x+1, n_y+1), dtype=float)
data_wn=np.zeros((n_x+1, n_y+1), dtype=float)
