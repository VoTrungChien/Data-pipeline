import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.tri as tri
#import matplotlib.collections
#import matplotlib.cm as cm

phase_pd = pd.read_csv("./41x41/L0_2/41x41_phase_100_DL_5e-07.csv")
dp_pd = pd.read_csv("./41x41/L0_2/41x41_U_100_DL_5e-07.csv")
position_pd = pd.read_csv("./41x41/41x41position.csv")
element_pd = pd.read_csv("./41x41/41x41element.csv")

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

# FEM data
nodes_x = nodes[:,0]
nodes_y = nodes[:,1]
nodal_values = phase[:,20]
elements_quads = elements
elements_all_tris = quads_to_tris(elements_quads)

values = phase[:,99]
values_d = dp
# create an unstructured triangular grid instance
triangulation = tri.Triangulation(nodes_x, nodes_y, elements_all_tris)
# plot the contours
plt.tricontourf(triangulation, nodal_values)
# show
plt.colorbar()
plt.axis('equal')
plt.show()
