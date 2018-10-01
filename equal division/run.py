# -*- coding: utf-8 -*-
import data
training_data,test_data,begin_end,index = data.load_data_wrapper()

import network
net = network.Network([1024,30,10])
d=1.4
for i in range(10):
    
    d=d+0.1
    print(d)
    net.SGD(training_data,35,begin_end,index,d,test_data = test_data)

import cPickle
write_file = open('weight.pkl','wb')
cPickle.dump([net.weights[:],net.biases[:]],write_file,-1)
write_file.close()

