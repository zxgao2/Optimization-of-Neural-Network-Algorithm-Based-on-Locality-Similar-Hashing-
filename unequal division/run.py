# -*- coding: utf-8 -*-
import data
import commondata
training_data,test_data,begin_end,index = data.load_data_wrapper()

import network
net = network.Network([36,30,commondata.NumClass])
d=15.0
for i in range(10):
    
    d=d / 10
    print(d)
    net.SGD(training_data,300,begin_end,index,d,test_data = test_data)

import cPickle
write_file = open('weight.pkl','wb')
cPickle.dump([net.weights[:],net.biases[:]],write_file,-1)
write_file.close()

