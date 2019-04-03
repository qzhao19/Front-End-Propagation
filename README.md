# Front-end-propagation
Simulation of front-end propagation

# Overview
This projet aims to solve the problem of front-end propagation, which could be modeled by the following partial differential equation called Eikonal Equation 

<a href="https://www.codecogs.com/eqnedit.php?latex=w_t(t,&space;x,&space;y)&plus;F(x,&space;y)||\Delta_{x}w(t,&space;x,&space;y)||^2=0,&space;w(0,&space;x,&space;y)=\phi{(x,&space;y)}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?w_t(t,&space;x,&space;y)&plus;F(x,&space;y)||\Delta_{x}w(t,&space;x,&space;y)||^2=0,&space;w(0,&space;x,&space;y)=\phi{(x,&space;y)}" title="w_t(t, x, y)+F(x, y)||\Delta_{x}w(t, x, y)||^2=0, w(0, x, y)=\phi{(x, y)}" /></a>

The equation coule be solved in the filed of calculation:

<a href="https://www.codecogs.com/eqnedit.php?latex=$D=[a,&space;b]*[c,&space;d]$" target="_blank"><img src="https://latex.codecogs.com/gif.latex?$D=[a,&space;b]*[c,&space;d]$" title="$D=[a, b]*[c, d]$" /></a>

# Requirement

Python 3.7 NumPy 1.15.4

# Usages

To run this script, you should follow below command:

    python main.py --model option(model_1 or model_2) --method option(method_1 or method_2)
   
# Visualization


