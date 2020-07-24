import numpy as np
import math
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.collections

phase_pd = pd.read_csv("./41x41/L0_2/41x41_phase_100_DL_5e-07.csv")
dp_pd = pd.read_csv("./41x41/L0_2/41x41_U_100_DL_5e-07.csv")
position_pd = pd.read_csv("./41x41/41x41position.csv")
element_pd = pd.read_csv("./41x41/41x41element.csv")

position = np.asarray(position_pd)
element = np.asarray(element_pd)-1
phase = np.asarray(phase_pd)
dp = np.asarray(dp_pd)

print(position.shape)
print(element.shape)
print(phase.shape)
print(dp.shape)

def showMeshPlot(nodes, elements, values):

    y = nodes[:,0]
    z = nodes[:,1]

    def quatplot(y,z, quatrangles, values, ax=None, **kwargs):

        if not ax: ax=plt.gca()
        yz = np.c_[y,z]
        verts= yz[quatrangles]
        pc = matplotlib.collections.PolyCollection(verts, **kwargs)
        pc.set_array(values)
        ax.add_collection(pc)
        ax.autoscale()
        return pc

    fig, ax = plt.subplots()
    ax.set_aspect('equal')

    pc = quatplot(y,z, np.asarray(elements), values, ax=ax,
             edgecolor="crimson")#, cmap="rainbow")
    fig.colorbar(pc, ax=ax)
    ax.plot(y,z)#, marker="o", ls="", color="crimson")

    ax.set(title='This is the plot for: quad', xlabel='Y Axis', ylabel='Z Axis')

    plt.show()

nodes = position
elements = element
stresses = phase[80]

showMeshPlot(nodes, elements, stresses)

