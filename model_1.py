# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 20:45:19 2019

@author: Administrator
"""
import numpy as np

def initCondition(x, y):
    # return min(1.0, float(np.sqrt(x**2+y**2)-0.5))
    temp=float(np.sqrt(x**2+y**2)-0.5)
    if temp<1.0:
        return temp
    else:
        return 1.0


def analyticalSolution(t, x, y):
    # return min(1.0, float(np.sqrt(x**2+y**2)-0.5-t))
    temp=float(np.sqrt(x**2+y**2)-0.5-t)
    if temp<1.0:
        return temp
    else:
        return 1.0


