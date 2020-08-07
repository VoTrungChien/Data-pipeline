import numpy
import numpy as np
import matplotlib.pyplot as plt
from pandas import read_csv
import math

m = np.array([41,51, 61, 71])
n = np.array([2, 4, 6, 8])
point = np.array([[0.5,0.5],[1,0.5],[1,1]])
j = 3
#phase-field behaviours based mesh sizes
plt.figure(1)
for k in range(len(point)):
    plt.subplot(3,1,k+1)
    plt.suptitle("Phase-field behaviours based mesh sizes")
    plt.title('point {0}'.format(k+1))
    for i in range(len(m)):
        phase_pd = read_csv("./{0}x{0}/L0_{1}/{0}x{0}_phase_100_DL_5e-07.csv".format(m[i],n[j]))
        pos_pd = read_csv("./{0}x{0}/{0}x{0}position.csv".format(m[i]))
        phase = phase_pd.values
        pos = pos_pd.values
        p=[l for l in range(len(pos)) if (pos[l]==[point[k,0],point[k,1]]).all()]
        phase = phase[p,:].reshape(-1,1)
        plt.plot(range(phase.shape[0]),phase)
# Error based mesh sizes
plt.figure(2)
phase_pd_0 = read_csv("./{0}x{0}/L0_{1}/{0}x{0}_phase_100_DL_5e-07.csv".format(m[0],n[j]))
pos_pd_0 = read_csv("./{0}x{0}/{0}x{0}position.csv".format(m[0]))
phase_0 = phase_pd_0.values
pos_0 = pos_pd_0.values
for k in range(len(point)):
    p0=[l for l in range(len(pos_0)) if (pos_0[l]==[point[k,0],point[k,1]]).all()]
    plt.subplot(3,1,k+1)
    plt.suptitle('Error based mesh sizes')
    plt.title('point {0}'.format(k+1))
    for i in range(len(m)):
        phase_pd = read_csv("./{0}x{0}/L0_{1}/{0}x{0}_phase_100_DL_5e-07.csv".format(m[i],n[j]))
        pos_pd = read_csv("./{0}x{0}/{0}x{0}position.csv".format(m[i]))
        phase = phase_pd.values
        pos = pos_pd.values
        p=[l for l in range(len(pos)) if (pos[l]==[point[k,0],point[k,1]]).all()]
        phase = phase[p,:].reshape(-1,1)-phase_0[p0,:].reshape(-1,1)
        phase = np.sqrt(phase**2)
        plt.plot(range(phase.shape[0]),phase)
plt.show()

