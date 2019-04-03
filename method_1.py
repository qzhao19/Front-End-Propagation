# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 21:15:31 2019

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
    x_i=global_var.a+i*global_var.h_x
    x_j=global_var.c+j*global_var.h_y
    result=global_var.delta_T*funcF(x_i, x_j)*np.sqrt(np.power(max(-1*u_minus(i, j), 0.0), 2)+ \
                                                      np.power(max( 1*u_plus(i, j), 0.0),  2)+ \
                                                      np.power(max(-1*v_minus(i, j), 0.0), 2)+\
                                                      np.power(max( 1*v_plus(i, j), 0.0), 2))
    return result
