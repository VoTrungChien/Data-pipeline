# producer7.py
from kafka import KafkaProducer
from kafka import KafkaConsumer
import numpy as np
import math
import matplotlib.pyplot as plt
import time,csv
import pandas as pd
import seaborn as sns
import pylab as pl


consumer = KafkaConsumer('stream')
i=0
for msg in consumer:
    i=+1
    producer = KafkaProducer(bootstrap_servers='localhost:9092')
    fname = "input7.dat"
    with open(fname) as fp:
    #data_to_send = ""
        line=fp.readline()
        j=0
        while line:
            data_to_send = ""
            j+=1
            values = line.split(' ')
            for i in range(len(values)):
                data_to_send += values[i].strip()+' '
            line=fp.readline()
            data_to_send = data_to_send+" "
            producer.send('stream7', bytes(data_to_send, encoding='utf-8'))
    producer.close()
    fp.closed
    if i==100:
        break
