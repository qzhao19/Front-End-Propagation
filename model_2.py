# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 21:09:24 2019

@author: Administrator
"""

import numpy as np


def initCondition(x, y):
    temp1=float(np.sqrt((x+1.0)**2 + y**2)-0.5)
    temp2=float(np.sqrt((x-1.0)**2 + y**2)-0.5)
    return min(1.0, max(temp1, temp2))

def analyticalSolution(t, x, y):
    temp1=float(np.sqrt((x+1.0)**2 + y**2)-0.5-t)
    temp2=float(np.sqrt((x-1.0)**2 + y**2)-0.5-t)
    return min(1.0, max(temp1, temp2))
    

