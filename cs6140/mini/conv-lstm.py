# ConvLSTM2D
import os
import math

import numpy
import pandas as pd

from sklearn.metrics import r2_score
from sklearn.preprocessing import MinMaxScaler

from keras.layers import ConvLSTM2D, Dense, TimeDistributed, Conv2D,BatchNormalization, AveragePooling3D,Reshape, Flatten
from keras.models import Sequential


def create_dataset(dataset, look_back=1):
    dataX, dataY = [], []
    for i in range(len(dataset)-look_back-1):
        a = dataset[i:(i+look_back), :].copy()
        a[-1,-1] = 0
        dataX.append(a)
        dataY.append(dataset[i + look_back - 1, -1])
    return numpy.array(dataX), numpy.array(dataY)

def load_dataset(path, cut = -1):
    dfs = []
    for f in os.listdir(path):
        df = pd.read_csv(path + f, engine='python', skipfooter=1)
        df = df.drop(columns=['index'])
        dfs.append(df)

    df = pd.concat(dfs, ignore_index=True)
    dataset = df.values
    dataset = dataset.astype('float32')

    if cut != -1:
        dataset = dataset[:cut,:]

    return dataset

def main(test_name):
    numpy.random.seed(7)
    look_back = 5

    TRAIN_PATH = '../data/ml/' + test_name +'/training/'
    TEST_PATH = '../data/ml/' + test_name +'/test/'
    VALIDATION_PATH = '../data/ml/' + test_name +'/validation/'

    scaler = MinMaxScaler(feature_range=(0, 1))

    train = load_dataset(TRAIN_PATH)
    train = scaler.fit_transform(train)

    test = load_dataset(TEST_PATH)
    test = scaler.fit_transform(test)

    validation = load_dataset(VALIDATION_PATH)
    validation = scaler.fit_transform(validation)


    trainX, trainY = create_dataset(train, look_back)
    testX, testY = create_dataset(test, look_back)
    validationX, validationY = create_dataset(validation, look_back)


    trainX = numpy.reshape(trainX, (trainX.shape[0], train.shape[1], trainX.shape[1], trainX.shape[1], trainX.shape[1]))
    testX = numpy.reshape(testX, (testX.shape[0], test.shape[1], testX.shape[1], testX.shape[1], testX.shape[1]))
    validationX = numpy.reshape(validationX, (validationX.shape[0], validation.shape[1], validationX.shape[1], validationX.shape[1], validationX.shape[1]))

    model = Sequential()

    #model.add(ConvLSTM2D(3, kernel_size=3, padding = "same", batch_input_shape=(1, train.shape[1], look_back), return_sequences=True, stateful=True))
    #model.add(TimeDistributed((Conv2D(1, kernel_size=3, padding = "same"))))
    #model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

    # ConvLSTM2D will add one more dim automatically
    model.add(ConvLSTM2D(64, 3, input_shape=(1, train.shape[1], look_back, 1)))
    model.add(Flatten())
    model.add(Dense(1))
    model.compile(loss='mean_absolute_error', optimizer='adam')

    model.summary()
    model.fit(trainX, trainY, epochs=20, batch_size=20, verbose=2)

    # make predictions
    trainPredict = model.predict(trainX)
    testPredict = model.predict(testX)
    validationPredict = model.predict(validationX)

    trainScore = r2_score(trainY.flatten(), trainPredict.flatten())
    print('Train Score: %.2f R2' % (trainScore))
    testScore = r2_score(testY.flatten(), testPredict.flatten())
    print('Test Score: %.2f R2' % (testScore))
    validationScore = r2_score(validationY.flatten(), validationPredict.flatten())
    print('Validation Score: %.2f R2' % (validationScore))

if __name__ == "__main__":
    print("Starting running experiment:\n")
    for test_name in ["KMeans", "PageRank", "SGD", "web_server"]:
        print("Case %s", test_name)
        main(test_name)

