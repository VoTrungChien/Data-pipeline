# DatProducer2.py
from kafka import KafkaProducer
import time,csv
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import pylab as pl

producer = KafkaProducer(bootstrap_servers='localhost:9092')
producer.send('stream', bytes('flag',encoding='utf-8'))
producer.close()


#fname = "input.dat"
#with open(fname) as fp:
#    #data_to_send = ""
#    line=fp.readline()
#    j=0
#    while line:
#        data_to_send = ""
#        j+=1
#        values = line.split(' ')
#        for i in range(len(values)):
#            data_to_send += values[i].strip()+' '
#        line=fp.readline()
#        data_to_send = data_to_send+" "
#        producer.send('heatmap', bytes(data_to_send, encoding='utf-8'))
#producer.close()
#fp.closed
