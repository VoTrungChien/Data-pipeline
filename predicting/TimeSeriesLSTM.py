# LSTM for international airline passengers problem with regression framing
import numpy
import numpy as np
import matplotlib.pyplot as plt
from pandas import read_csv
import math
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_squared_error

m=np.array([41,51,61,71])
n=np.array([2,4,6,8])
s=0
t=3
point=np.array([0.5,0.5])
phase_pd_60 = read_csv("./{0}x{0}/L0_{1}/{0}x{0}_phase_100_DL_5e-07.csv".format(m[s],n[t]))
pos_pd_60 = read_csv("./{0}x{0}/{0}x{0}position.csv".format(m[s]))
pos_60 = pos_pd_60.values
p=[i for i in range(len(pos_60)) if (pos_60[i]==[point[0],point[1]]).all()]
phase_60 = phase_pd_60.values[p,:].reshape(-1,1)
phase_60 = phase_60.astype('float32')

s=3
phase_pd_70 = read_csv("./{0}x{0}/L0_{1}/{0}x{0}_phase_100_DL_5e-07.csv".format(m[s],n[t]))
pos_pd_70 = read_csv("./{0}x{0}/{0}x{0}position.csv".format(m[s]))
pos_70 = pos_pd_70.values
p=[i for i in range(len(pos_70)) if (pos_70[i]==[point[0],point[1]]).all()]
phase_70 = phase_pd_70.values[p,:].reshape(-1,1)
phase_70 = phase_70.astype('float32')
# split into train and test sets
train_size = int(len(phase_60) * 0.60)
test_size = len(phase_60) - train_size
trainX, testX = phase_60[0:train_size,:], phase_60[train_size:len(phase_60),:]
trainY, testY = phase_70[0:train_size,:], phase_60[train_size:len(phase_60),:]
look_back = 1
# reshape input to be [samples, time steps, features]
trainX = numpy.reshape(trainX, (trainX.shape[0], 1, trainX.shape[1]))
testX = numpy.reshape(testX, (testX.shape[0], 1, testX.shape[1]))
# create and fit the LSTM network
model = Sequential()
model.add(LSTM(4, input_shape=(1, look_back)))
model.add(Dense(1))
model.compile(loss='mean_squared_error', optimizer='adam')
model.fit(trainX, trainY, epochs=100, batch_size=1, verbose=2)
# make predictions
trainPredict = model.predict(trainX)
testPredict = model.predict(testX)
trainScore = math.sqrt(mean_squared_error(trainY[:,0], trainPredict[:,0]))
print('Train Score: %.2f RMSE' % (trainScore))
testScore = math.sqrt(mean_squared_error(testY[:,0], testPredict[:,0]))
print('Test Score: %.2f RMSE' % (testScore))
trainPredictPlot = numpy.empty_like(phase_60)
trainPredictPlot[:, :] = numpy.nan
trainPredictPlot[0:len(trainPredict)] = trainPredict
testPredictPlot = numpy.empty_like(phase_60)
testPredictPlot[:, :] = numpy.nan
testPredictPlot[len(trainPredict):len(phase_60)] = testPredict
plt.plot(phase_70,label='70')
plt.plot(trainPredictPlot)
plt.plot(testPredictPlot)
plt.plot(phase_60,label='60')
plt.legend()
plt.show()
