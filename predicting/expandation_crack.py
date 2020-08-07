import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.tri as tri
import matplotlib.cm as cm
import mplcursors
from sklearn.cluster import KMeans

# converts quad elements into tri elements
def quads_to_tris(quads):
    tris = [[None for j in range(3)] for i in range(2*len(quads))]
    for i in range(len(quads)):
        j = 2*i
        n0 = quads[i][0]
        n1 = quads[i][1]
        n2 = quads[i][2]
        n3 = quads[i][3]
        tris[j][0] = n0
        tris[j][1] = n1
        tris[j][2] = n2
        tris[j + 1][0] = n2
        tris[j + 1][1] = n3
        tris[j + 1][2] = n0
    return tris

m = np.array([61,71])
n = np.array([2,4,6,8])
step = [61,67,71,99]
u = [2.95e-5,3.35e-5,3.58e-5,4.15e-5]

for i in range(len(m)):
    j=0
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
    nodes = position
    # FEM data
    nodes_x = nodes[:,0]
    nodes_y = nodes[:,1]
    for k in range(len(step)):
        nodal_values = phase[:,step[k]]
        elements_quads = elements
        elements_all_tris = quads_to_tris(elements_quads)
        triangulation = tri.Triangulation(nodes_x, nodes_y, elements_all_tris)
        #plt.tricontour(triangulation, nodal_values,cmap='jet')
        levels = np.arange(0, 1.01, 0.005)
        cmap = cm.get_cmap(name='jet', lut=None)
        number='14{0}'.format(k+1)
        plt.subplot(number)
        plt.suptitle('mesh size {0}x{0}'.format(m[i]-1), fontsize=12)
        plt.tricontourf(triangulation, nodal_values,levels=levels,cmap=cmap)
        #plt.colorbar()
        plt.xlabel('u={0}mm & step ${1}th$'.format(u[k],step[k]), fontsize=12)
        #plt.ylabel('ylabel{0}'.format(j), fontsize=8)
        #plt.rcParams['font.family']='cursive'
        plt.rcParams['font.size']='8'
        #plt.tight_layout(pad=1)
        plt.axis('equal')
        plt.xlim([-0.1, 1.1])
        plt.ylim([-0.1,1.1])
        mplcursors.cursor()

plt.show()

