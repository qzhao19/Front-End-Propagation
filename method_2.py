# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 13:29:18 2019

@author: Administrator
"""

import global_variables as global_var
import numpy as np

def funcF(x, y):
    return 1.0

def u_plus(i, j):
    return float((global_var.data_w[i+1, j]-global_var.data_w[i,j])/global_var.h_x)
    
def u_minus(i, j):
    return float(-(global_var.data_w[i-1, j]-global_var.data_w[i,j])/global_var.h_x)

def v_plus(i, j):
    return float((global_var.data_w[i, j+1]-global_var.data_w[i,j])/global_var.h_y)    
    
def v_minus(i, j):
    return float(-(global_var.data_w[i, j-1]-global_var.data_w[i,j])/global_var.h_y)
    
    
def diff_w(i, j):
    x_i=global_var.A+i*global_var.h_x
    y_j=global_var.c+j*global_var.h_y
#     result=delta_T*funcF(x_i, x_j)*(np.sqrt(((u_plus(i, j)+u_minus(i, j))/2)**2 + ((v_plus(i, j)+v_minus(i, j))/2)**2) - \
#                                     A*((u_plus(i, j)-u_minus(i, j))/2 + (v_plus(i,j)-v_minus(i, j))/2))  

    result=global_var.delta_T*funcF(x_i, y_j)*(0.5*np.sqrt(np.power((u_plus(i, j)+u_minus(i, j)), 2)+np.power((v_plus(i, j)-v_minus(i, j)), 2)) - \
                                    0.5*global_var.A*((u_plus(i, j)-u_minus(i, j))+(v_plus(i, j)-v_minus(i, j))))

    return result