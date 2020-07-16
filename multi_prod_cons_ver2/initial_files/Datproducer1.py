#DatProducer.py
from kafka import KafkaProducer
import time,csv
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import pylab as pl
producer = KafkaProducer(bootstrap_servers='localhost:9092',max_request_size=15728640)
DatContent = [i.strip().split() for i in open("input.dat").readlines()]

with open("input.csv", "w") as f:
    writer = csv.writer(f,dialect='excel')
    writer.writerows(DatContent)
f.close()
dataframe=pd.read_csv("input.csv",names=['length','width'])

with open("input.csv") as fp:
    line = fp.readline()
    #data_to_send = ""
    while line:
        data_to_send = ""
        values = line.split(',')
        for i in range(len(values)):
            data_to_send += values[i].strip()+' '
        line = fp.readline()
        #print('asdfasdf{0}'.format(line))
        data_to_send = data_to_send+" "
        producer.send('heatmap', bytes(data_to_send, encoding='utf-8'))
producer.close()
fp.closed
#producer = KafkaProducer(bootstrap_servers='localhost:9092')
#producer1 = KafkaProducer(value_serializer=lambda m: json.dumps(m).encode('utf-8'))



