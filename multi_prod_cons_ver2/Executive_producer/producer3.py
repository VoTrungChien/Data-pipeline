# producer3.py
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
    if msg.value == b'flag':
        i=+1
        producer = KafkaProducer(bootstrap_servers='localhost:9092')
        fname = "input3.dat"
        with open(fname) as fp:
            line=fp.readline()
            j=0
            while line:
                j+=1
                print(j)
                data_to_send=line
                line=fp.readline()
                producer.send('stream3', bytes(data_to_send, encoding='utf-8'))
        print('in flag')
        producer.close()
        fp.closed
    if i==100:
        break
