import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.tri as tri
import matplotlib.cm as cm
import mplcursors
from sklearn.cluster import KMeans
from sklearn.cluster import AgglomerativeClustering

"""
phase_pd = pd.read_csv("./41x41/L0_2/41x41_phase_100_DL_5e-07.csv")
dp_pd = pd.read_csv("./41x41/L0_2/41x41_U_100_DL_5e-07.csv")
position_pd = pd.read_csv("./41x41/41x41position.csv")
element_pd = pd.read_csv("./41x41/41x41element.csv")
"""
phase_pd = pd.read_csv("./71x71/L0_2/71x71_phase_100_DL_5e-07.csv")
dp_pd = pd.read_csv("./71x71/L0_2/71x71_U_100_DL_5e-07.csv")
position_pd = pd.read_csv("./71x71/71x71position.csv")
element_pd = pd.read_csv("./71x71/71x71element.csv")

element = np.array(element_pd)
position = np.array(position_pd)
phase = np.array(phase_pd)
dp = np.array(dp_pd)
elements = element-1
nodes = position

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
step = [61,70,99]
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
    nodes = position
    # FEM data
    nodes_x = nodes[:,0]
    nodes_y = nodes[:,1]
    for k in range(len(step)):
        nodal_values = phase[:,step[k]]
        elements_quads = elements
        elements_all_tris = quads_to_tris(elements_quads)
        plt.suptitle('mesh size {0}x{0}'.format(m[i]-1), fontsize=12)
        plt.subplot(3,3,3*k+1)
        triangulation = tri.Triangulation(nodes_x, nodes_y, elements_all_tris)
        levels = np.arange(0, 1.01, 0.005)
        cmap = cm.get_cmap(name='jet', lut=None)
        plt.tricontourf(triangulation, nodal_values,levels=levels,cmap=cmap)
        plt.colorbar()
        plt.axis('equal')
        if k==0:
            plt.title("crack propagation",fontsize=10)
        plt.xlim([-0.1, 1.1])
        plt.ylim([-0.1,1.1])
        mplcursors.cursor()
        # K-mean Clustering
        plt.subplot(3,3,3*k+2)
        K = 10
        one = np.ones_like(nodal_values)
        values = np.concatenate((nodal_values,one), axis=0)
        values = values.reshape(2,-1).T
        km = KMeans(n_clusters=K).fit(values)
        y_pred = km.predict(values)
        plt.scatter(position[:,0],position[:,1],c=y_pred, cmap='Wistia', marker='s')
        plt.axis('equal')
        if k==0:
            plt.title("K-means",fontsize=10)
        plt.colorbar()
        # Agglomerative clustering
        plt.subplot(3,3,3*k+3)
        agg = AgglomerativeClustering(n_clusters=K)
        y_pred = agg.fit_predict(values)
        plt.scatter(position[:,0],position[:,1],c=y_pred, cmap='winter',marker=',')
        plt.axis('equal')
        if k==0:
            plt.title("Agglomerative",fontsize=10)
        plt.colorbar()

plt.show()
