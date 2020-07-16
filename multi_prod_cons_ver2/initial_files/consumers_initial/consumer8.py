from kafka import KafkaConsumer
import numpy as np
import math
import matplotlib.pyplot as plt
import seaborn as sns

consumer = KafkaConsumer('stream8')
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
    if j==800:
        j=0
        #print(data_received)
        data_list=data_received
        data=np.array((data_list))
        x_list=np.random.rand(100).tolist()
        x = np.array((x_list))
        x_res=x.reshape((10,int(math.sqrt(len(x)))))
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
#print(data_received)
#print(type(data_received))
#data=np.array((data_received))
#data_res=data.reshape(math.sqrt(len(x)),math.sqrt(len(x)))
#data_res=data.reshape(len(data)/800,800)
#fig, ax = plt.subplots(figsize=(800,800))
#sns.heatmap(data_res, square=True, ax=ax)
#plt.yticks(rotation=0,fontsize=16);
#plt.xticks(fontsize=12);
#plt.tight_layout()
#plt.savefig('colorlist.png')
