''' Compute end velocity based on quadratic drag in water and air
(Define units in lbf, sec, ft)
'''
import numpy as np
import matplotlib.pyplot as plt
import math
import os

path = os.path.dirname(__file__)

'''------ USER DEFINED PARAMETERS -----'''
# Array defining name of objects
Name = ['Object 1', 'Object 2']
# Array defining weight of objects [lbf]
weight = [4000, 10000]
# Array defining area on which drag force will be applied to [ft^2]
Area = [1, 10]
distTOT = 50 # total height of object to fall [ft]
g = 32.2
rhow = 62.4 # density of medium 2 [i.e. water] [lbf/ft^3]
Cd = 1.2 # drag coefficient
dt = 0.001 # define time step for approximation [sec]
timeTot = 5 # define total time to run
v_initial = -100 # inital velocity of object [ft/sec]

plot = 'yes' # toggle whether to generate plot or not (yes/no)

''' --- START OF APPROXIMATE SOLUTION ----'''
n_dt = int (timeTot / dt)

j = 0
while j <= (len(Name) - 1):
    runtime = 0.0
    i = 0
    mass = weight[j] / g
    Fg = mass * g
    a = Area[j]
    dist = np.array([])
    vel = np.array([])
    accl = np.array([])
    dragF = np.array([])
    time = [0]
    vel = np.append(vel, v_initial)
    dist = np.append(dist, 0.0)
    while i <= n_dt:
        if vel[i] >= 0:
            dragF = np.append(dragF, -0.5*Cd*rhow*a*(vel[i])**2)
        if vel[i] < 0:
            dragF = np.append(dragF, 0.5*Cd*rhow*a*(vel[i])**2)
        accli = (dragF[i] + Fg)/mass
        accl = np.append(accl, accli)
        vel = np.append(vel, vel[i] + dt*accl[i])
        dist = np.append(dist, dist[i] + dt*vel[i]+0.5*accl[i]*dt**2)
        time = np.append(time, runtime)
        if i == n_dt:
            print(Name[j], time[i], ': distance(ft) = ', dist[i], '| velocity(ft/s) = ', vel[i] )

            if plot == 'yes':
                plt.subplot(2, 1, 1)
                plt.plot(time, vel, linewidth=1.0, label=Name[j])
                plt.title('Time History Plots')
                # velocity time history
                plt.ylabel('velocity(ft/s)')
                plt.grid(True)
                plt.legend(loc=1)

                # displacement plot
                plt.subplot(2, 1, 2)
                plt.plot(time, dist, ls='-', linewidth=1.0, label=Name[j])
                plt.ylabel('distance(ft)')
                plt.xlabel('time(s)')
                plt.grid(True)
                plt.legend(loc=4)
            break
        runtime += dt
        i += 1
    j += 1
if plot == 'yes':
    os.chdir(path)
    figure = plt.gcf()
    figure.set_size_inches(12, 8)
    plt.show()
