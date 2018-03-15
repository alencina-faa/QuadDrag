# Quadatric Drag Solver

## Overview
The python script developed will compute the drag forces on either single or multiple objects which are in free fall and solve the equation of motion using the Euler Method. The script plots the displacement and velocity time histores of the objects. With a small enough user defined time step,`dt`, the error of the approximation is negligble. 

Skin friction is neglected in this calculation. 

## Equation of Motion
The equation of motion being solved is:

The drag force being computed is quadratic and follows the form:

![first equation](https://latex.codecogs.com/gif.latex?F_D&space;=&space;\frac{1}{2}{\rho}v^2C_dA) 

 * C<sub>D</sub> is the drag coefficient

 * v is the velocity of the object

 * A is the projected area of the object

 * &rho; is the fluid density

The full time dependent equation motion is:

![second equation](https://latex.codecogs.com/gif.latex?F_{net}=F_g-F_D&space;\underset{yields}{\rightarrow}&space;ma(t)=mg&space;-&space;\frac{1}{2}{\rho}v(t)^2C_dA)

## Example Run

```python
'''---- User Defined Parameters ----'''
Name = ['Object 1', 'Object 2'] # Names of all objects
weight = [4000, 10000]          # Array defining weight of objects [lbf]
Area = [1, 10]                  # Array defining area on which drag force will be applied to [ft^2]
distTOT = 50                    # total height of object to fall [ft]
g = 32.2                        # universal gravitation constant [ft/s^2]
rhow = 62.4                     # density of water [lbf/ft^3]
Cd = 1.2                        # drag coefficient
dt = 0.001                      # define time step for approximation [sec]
timeTot = 5                     # define total time to run
v_initial = -100                # inital velocity of object [ft/sec]
```
![fig1](https://github.com/nasriv/QuadDrag/blob/master/Fig1.png)

## Installation
Code written in Python3. Utilizies matplotlib.pyplot and numpy python packages. Edit user parameters in QuadDrag.py file and run using python

Mathematical equations developed using: https://www.codecogs.com/latex/eqneditor.php


       
  
