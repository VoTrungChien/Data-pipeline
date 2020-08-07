import numpy as np
import matplotlib.pyplot as plt
table = [[10*10,20*20,30*30,40*40,50*50,60*60,70*70],[53.05,267.46,1500.62,8575.37,22174.51,54924.19,117989.64]]
t = np.array(table).T 
plt.figure(1)
plt.plot(t[:,0],t[:,1],'g--',t[:,0],t[:,1],'rs')
plt.xlabel('elements [-]',fontsize=12)
plt.ylabel('runtime [s]',fontsize=12)
plt.tight_layout(pad=1)
plt.show()
