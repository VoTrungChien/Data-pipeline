# Executive_producer.py
from kafka import KafkaProducer
import time,csv
import numpy as np

data='/home/trungchien/multi_prod_cons/source_code/input{0}.dat'.format(1)
with open(data) as fp:
    div=4
    fps=fp.readlines()
    ls=len(fps)
    dl=ls//div
    for ip in range(1,div+1):
        Data_int=open('input{0}.dat'.format(ip),'w')
        for line in fps[(ip-1)*dl:ip*dl]:
            Data_int.write(line)
        print(type(line))
print('Executive Producer')
fp.closed
Data_int.close()
producer = KafkaProducer(bootstrap_servers='localhost:9092')
producer.send('stream', bytes('flag',encoding='utf-8'))
producer.close()

