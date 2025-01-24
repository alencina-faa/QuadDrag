''' Compute end velocity based on quadratic drag force. Includes buoyancy.
(Define units in kg, sec, m)
'''
import numpy as np
import matplotlib.pyplot as plt
import math
import os

path = os.path.dirname(__file__)

'''------ USER DEFINED PARAMETERS -----'''
g = 9.8
# Array defining name of objects
Name = ['Object 1']
# Array defining weight of objects [kg]
weight = [.00002090395*g]
rhoo = [1000.] #Density of the objects [kg/m^3]
# Array defining area on which drag force will be applied to [m^2]
Area = [0.00332**2*math.pi/4 ]
distTOT = 0.53 # total height of object to fall [m]
rhow = 1.2 # density of souronding  medium [i.e. air] [kg/m^3]
Cd = 0.5207 # drag coefficient
dt = 0.001 # define time step for approximation [sec]
timeTot = 10 # define total time to run
v_initial = 0 # inital velocity of object [ft/sec]

plot = 'yes' # toggle whether to generate plot or not (yes/no)

''' --- START OF APPROXIMATE SOLUTION ----'''
n_dt = int (timeTot / dt)

j = 0
while j <= (len(Name) - 1):
    runtime = 0.0
    i = 0
    mass = weight[j] / g
    Fg = mass * g - rhow*np.power(rhoo,-1)*weight
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
        if (i == n_dt) or (dist[i] >= distTOT):
            print(Name[j] + '\t time = ' + f"{time[i]:.3f}" + ' s\t| distance = ' + f"{dist[i]:.3f}" + ' m\t| velocity = ' + f"{vel[i]:.3f}" + ' m/s' )

            if plot == 'yes':
                plt.subplot(2, 1, 1)
                plt.plot(time, vel, linewidth=1.0, label=Name[j])
                plt.title('Time History Plots')
                # velocity time history
                plt.ylabel('velocity(m/s)')
                plt.grid(True)
                plt.legend(loc=4)

                # displacement plot
                plt.subplot(2, 1, 2)
                plt.plot(time, dist, ls='-', linewidth=1.0, label=Name[j])
                plt.ylabel('distance(m)')
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
