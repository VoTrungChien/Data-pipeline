from kafka import KafkaConsumer
import numpy as np
import math
import matplotlib.pyplot as plt
import seaborn as sns

consumer = KafkaConsumer('stream1')
j=0
data_received=[]
print('hello')
for msg in consumer:
    j+=1
    line=msg.value
    lines=line.decode() # convert bytes to strings
    values=lines.split()
    for i in range(len(values)):
        #data_received += values[i].strip()+' '
        data_received.append(float(values[i].strip()))
    print(j)
    if j==200:
        j=0
        #print(data_received)
        data_list=data_received
        data=np.array((data_list))
        data_res=data.reshape(int(math.sqrt(len(data))),int(math.sqrt(len(data))))
        fig, ax = plt.subplots()
        sns.heatmap(data_res, square=True, ax=ax)
        plt.yticks(rotation=0,fontsize=16);
        plt.xticks(fontsize=12);
        plt.tight_layout()
        #plt.savefig('colorlist.png')
        plt.show()
        data_received=[]
print('hello2')
