from kafka import KafkaProducer
from kafka import KafkaConsumer
import numpy as np
import math
import matplotlib.pyplot as plt
import seaborn as sns

consumer= KafkaConsumer('stream')
count=0
for msg in consumer:
    #line=msg.value
    #endorsement=line.decode()
    if msg.value==b'endorsed':
        count += 1
        print('endorsed')
        print(count)
    if count == 4:
        data1=open('output1.dat').read()
        data2=open('output2.dat').read()
        data3=open('output3.dat').read()
        data4=open('output4.dat').read()
        with open ('output.dat','w') as fp:
            Data_out=data1+data2+data3+data4
            fp.write(Data_out)
        fp.closed
        with open ('output.dat') as fp:
            line=fp.readline()
            j=0
            Data=[]
            while line:
                j+=1
                values = line.split()
                for i in range(len(values)):
                    Data.append(float(values[i].strip()))
                line=fp.readline()
                print(j)
        fp.closed
        data_an=np.array((Data))
        data_res=data_an.reshape(int(math.sqrt(len(data_an))),int(math.sqrt(len(data_an))))
        fig, ax = plt.subplots()
        sns.heatmap(data_res,square=True, ax=ax)
        plt.yticks(rotation=0,fontsize=16)
        plt.xticks(fontsize=12);
        plt.tight_layout()
        plt.show()
        Data=[]
        count = 0






