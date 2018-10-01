# -*- coding: utf-8 -*-
import data
import commondata
training_data,test_data = data.load_data_wrapper()

import network
net = network.Network([36,30,commondata.NumClass])
d=1.4
for i in range(10):
    d=d+0.1
    print(d)
    net.SGD(training_data,300,10,d,test_data = test_data)

import cPickle
write_file = open('weight.pkl','wb')
cPickle.dump([net.weights[:],net.biases[:]],write_file,-1)
write_file.close()


