'''Adapted from www.machinelearningmastery.com for keras==0.1.3'''

import pandas as pd  
from random import random
import numpy
import numpy as np
from keras.models import Sequential  
from keras.layers.core import Dense, Activation,Dropout  
from keras.layers.recurrent import LSTM
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler

look_back=10
dataframe = pd.read_csv('international-airline-passengers.csv', usecols=[1], engine='python', skipfooter=3)
dataset = dataframe.values

numpy.random.seed(7)
scaler = MinMaxScaler(feature_range=(0, 1))
dataset = scaler.fit_transform(dataset)
train_size = int(len(dataset) * 0.8)
test_size = len(dataset) - train_size
train, test = dataset[0:train_size,:], dataset[train_size:len(dataset),:]
print(len(train), len(test))	

def create_dataset(dataset, look_back=1):
	dataX, dataY = [], []
	for i in range(len(dataset)-look_back):
		a = dataset[i:(i+look_back), 0]
		dataX.append(a)
		dataY.append(dataset[i + look_back, 0])
	return numpy.array(dataX), numpy.array(dataY)
trainX, y_train = create_dataset(train, look_back)
testX, y_test = create_dataset(test, look_back)

r=[]
for i in range(0,len(trainX)):
    r.append([[trainX[i][0]],[trainX[i][1]],[trainX[i][2]]])

trainX=np.array(r)
trainX
trainX.shape
p=[]
for i in range(0,len(y_train)):
    p.append([y_train[i]])
y_train=np.array(p)
y_train.shape[0]

model = Sequential()  
model.add(LSTM(20, y_train.shape[0], return_sequences=False))  
model.add(Dense(y_train.shape[0], 1))  
model.add(Activation("linear"))  
model.compile(loss="mean_squared_error", optimizer="rmsprop")  

model.fit(trainX, y_train, batch_size=15, nb_epoch=5)  


predicted = model.predict(trainX)  
plt.figure(figsize=(9,6))
line1,=plt.plot(predicted,linewidth=2,color='r',label='PREDICTION')
line2,=plt.plot(y_train,linewidth=2,color='b',label='TIME SERIES')
plt.title("TIME SERIES PREDICTION")
plt.legend([line1, line2])
plt.show()