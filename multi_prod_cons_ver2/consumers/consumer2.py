from kafka import KafkaConsumer
from kafka import KafkaProducer
import numpy as np
import math
import matplotlib.pyplot as plt
import seaborn as sns

consumer = KafkaConsumer('stream2')
j=0
data_received=[]
print('hello')
for msg in consumer:
    if j==0:
        Data_out=open('output2.dat','w')
    j+=1
    line=msg.value
    lines=line.decode() # convert bytes to strings
    Data_out.write(lines)
    if j==200:
        j=0
        Data_out.close()
        producer =KafkaProducer(bootstrap_servers='localhost:9092')
        producer.send('stream',bytes('endorsed',encoding='utf-8'))
        producer.close()
