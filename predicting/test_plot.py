import numpy as np
import pandas as pd

phase_pd = pd.read_csv("./41x41/L0_2/41x41_phase_100_DL_5e-07.csv")
position_pd = pd.read_csv("./41x41/41x41position.csv")

node=1000
ep=-0.5

position = np.array(position_pd)
phase = np.array(phase_pd)

phase_approx = phase[node,:]*1/2*(1-ep) + phase[node+1,:]*1/2*(1+ep);

node=np.array([[1,6,11,16,20],[1,7.25,13.5,19.75,26],[1,8.5,16,23.5,31],[1,9.75,18.5,27.5,36]])
p = np.array([i for i in range(len(position)) if (position[i]==[0.5,0.5]).all()])

point = np.concatenate((phase[p+int(node[0,0])].reshape(-1,1),phase[p+int(node[0,1])].reshape(-1,1),phase[p+int(node[0,2])].reshape(-1,1),phase[p+int(node[0,3])].reshape(-1,1),phase[p+int(node[0,4])].reshape(-1,1)),axis=1)
point = np.array(point)

i=70

#the B-spline representation of a 1-D curve
import matplotlib.pyplot as plt
from scipy.interpolate import splev, splrep
spl = splrep(node[0,:],point[i,:])
x2 = np.linspace(node[0,0], node[0,4], 200)
y2 = splev(x2, spl)
plt.figure(1)
plt.plot(node[0,:],point[i,:], 'o', x2, y2)
plt.axis([0,20.1,0,1.1])

#using interp1d and barycentric interpolator
from scipy import interpolate
f = interpolate.interp1d(node[0,:], point[i,:])
f1 = interpolate.BarycentricInterpolator(node[0,:], point[i,:])
xnew = np.arange(node[0,0], node[0,4], 0.1)
ynew = f(xnew)
plt.figure(2)
plt.axis([0,20.1,0,1.1])
plt.plot(node[0,:],point[i,:], 'o', xnew, ynew, '-')

#pchip interpolation
from scipy.interpolate import pchip_interpolate
x = np.linspace(node[0,0], node[0,4], num=100)
y = pchip_interpolate(node[0,:], point[i,:], x)
plt.figure(1)
plt.plot(node[0,:], point[i,:], "o", label="observation")
plt.plot(x, y, label="pchip interpolation")
plt.legend()

plt.show()


