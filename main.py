# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 20:50:12 2019

@author: Administrator
"""
import argparse
import global_variables as global_var
import numpy as np


ap = argparse.ArgumentParser()
ap.add_argument("-m", '--model', default='model_1',  help='Function model')
ap.add_argument("-a", "--method", default='method_1', help='Method')
args = vars(ap.parse_args())


if args.get("model") == 'model_1':
    import model_1 as model
elif args.get("model") == 'model_2':
    import model_2 as model

if args.get("method") == 'method_1':
    import method_1 as method
elif args.get("method") == 'method_2':
    import method_2 as method




def calcInitCondition():
    for i in range(global_var.n_x+1):
        for j in range(global_var.n_y+1):
            x_i=global_var.a+i*global_var.h_x
            y_j=global_var.c+j*global_var.h_y
            global_var.data_w[i, j]=model.initCondition(x_i, y_j)

def calcAnalyticalSolution():
    for i in range(global_var.n_x+1):
        for j in range(global_var.n_y+1):
            x_i=global_var.a+i*global_var.h_x
            y_j=global_var.c+j*global_var.h_y
            global_var.data_s[i, j]=model.analyticalSolution(global_var.T, x_i, y_j)

            
def calcNumericalSolution():
    # initialize data_wn
    for i in range(global_var.n_x+1):
        for j in range(global_var.n_y+1):
            global_var.data_wn[i, j]=1.0
            
    for n in range(1, global_var.N+1):
        for i in range(1, global_var.n_x):
            for j in range(1, global_var.n_y):
                global_var.data_wn[i, j]=global_var.data_w[i, j]-method.diff_w(i, j)
                
        for i in range(global_var.n_x+1):
            for j in range(global_var.n_y+1):
                global_var.data_w[i, j]=global_var.data_wn[i, j]
    
    
    
def calcMxError():
    error=0.0
    for i in range(global_var.n_x+1):
        for j in range(global_var.n_y+1):
            temp=np.abs(global_var.data_wn[i, j]-global_var.data_s[i, j])
            if error<temp:
                error=temp
    return error        
    
    
    
    
calcInitCondition()
# print(global_var.data_w)
calcAnalyticalSolution()
# print(global_var.data_s)
calcNumericalSolution()
# print(global_var.data_wn)
error=calcMxError()

print(error)

np.savetxt('./result/analytical_solution.txt',global_var.data_s, delimiter=';')
np.savetxt('./result/numerical_Solution.txt',global_var.data_wn,delimiter=';')  
   
    
    
    
    
    
    
    
    