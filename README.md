# Quadatric Drag Solver

## Overview
The python script (based on https://github.com/nasriv/QuadDrag) compute the drag forces (F<sub>D</sub>) on either single or multiple objects (of wight P) which are in free fall and solve the equation of motion using the Euler Method. The script plots the displacement and velocity time histores of the objects. With a small enough user defined time step,`dt`, the error of the approximation is negligble. 

Skin friction is neglected in this calculation. 

This calculation includes Buoyancy force (B).

Units are un SI.

Program stops either after reaching a defined time or displacement.

## Equation of Motion
The equation of motion being solved is:

The drag force being computed is quadratic and follows the form:

![first equation](https://github.com/nasriv/QuadDrag/blob/master/Drag%20Equation.png) 

 * C<sub>D</sub> is the drag coefficient

 * v is the velocity of the object

 * A is the projected area of the object

 * &rho; is the fluid density

The full time dependent equation of motion is:

P - B - F<sub>D</sub> = ma

## Example Run

```python
'''---- User Defined Parameters ----'''
g = 9.8
# Array defining name of objects
Name = ['Object 1']
# Array defining weight of objects [kg]
weight = [.00002090395*g]
rhoo = [1000.] #Density of the objects [kg/m^3]
# Array defining area on which drag force will be applied to [m^2]
Area = [0.00332**2*math.pi/4 ]
distTOT = 0.53 # total height of object to fall [m]
rhow = 1.2 # density of souronding medium [i.e. air] [kg/m^3]
Cd = 0.5207 # drag coefficient
dt = 0.001 # define time step for approximation [sec]
timeTot = 10 # define total time to run
v_initial = 0 # inital velocity of object [ft/sec]
```
![fig1](https://github.com/nasriv/QuadDrag/blob/master/Fig1.png)

## Installation
Code written in Python3. Utilizies matplotlib.pyplot and numpy python packages. Edit user parameters in QuadDrag.py file and run using python

Mathematical equation visuals developed using: https://www.codecogs.com/latex/eqneditor.php


       
  
