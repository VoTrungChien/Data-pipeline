import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import mplcursors

m = np.array([61,71])
n = np.array([2,4,6,8])
step = [61,67,71,99]
u = [2.95e-5,3.35e-5,3.58e-5,4.15e-5]

for i in range(len(m)):
    j=3

    plt.figure(i)
    phase_pd = pd.read_csv("./{0}x{0}/L0_{1}/{0}x{0}_phase_100_DL_5e-07.csv".format(m[i],n[j]))
    dp_pd = pd.read_csv("./{0}x{0}/L0_{1}/{0}x{0}_U_100_DL_5e-07.csv".format(m[i],n[j]))
    position_pd = pd.read_csv("./{0}x{0}/{0}x{0}position.csv".format(m[i]))
    element_pd = pd.read_csv("./{0}x{0}/{0}x{0}element.csv".format(m[i]))
    element = np.array(element_pd)
    position = np.array(position_pd)
    phase = np.array(phase_pd)
    dp = np.array(dp_pd)
    elements = element-1
    n1 = int(dp.shape[0]/2)
    n2 = dp.shape[1]
    uy = np.zeros((n1,n2))
    ux = uy
    for o in range(n1):
        for p in range(n2):
            ux[o,p] = dp[2*o,p]
            uy[o,p] = dp[2*o+1,p]
    for k in range(len(step)):
        levels = np.arange(0, 1.01, 0.005)
        cmap = cm.get_cmap(name='jet', lut=None)
        number='14{0}'.format(k+1)
        plt.subplot(number)
        plt.suptitle('mesh size {0}x{0}'.format(m[i]-1), fontsize=12)
        plt.quiver(position[:,0],position[:,1],ux[:,step[k]],uy[:,step[k]], color='blue')#,width=0.07,headwidth=3, headlength=4.)
        plt.xlabel('u={0}mm & step ${1}th$'.format(u[k],step[k]), fontsize=12)
        plt.rcParams['font.size']='8'
        plt.axis('equal')
        plt.xlim([-0.1, 1.1])
        plt.ylim([-0.1,1.1])
        mplcursors.cursor()

plt.show()

