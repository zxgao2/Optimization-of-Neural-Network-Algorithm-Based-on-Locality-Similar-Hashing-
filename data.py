# -*- coding: utf-8 -*-

import cPickle
import numpy as np
import commondata

NumClass = commondata.NumClass
ImageWidth = commondata.ImageWidth
ImageHeight = commondata.ImageHeight

def vectorized_result(j):
    e = np.zeros((NumClass,1))
    e[j] = 1.0
    return e
    
def load_data():
    f = open('train-sat.pkl','rb')
    training_data = cPickle.load(f)
    f.close()
    
    
    f = open('test-sat.pkl','rb')
    test_data = cPickle.load(f)
    f.close()
    
    return (training_data,test_data)

def load_data_wrapper():
    tr_d,te_d = load_data()
    len1 = 36
    training_inputs = [np.reshape(x,(len1,1)) for x in tr_d[0]]
    training_results = [vectorized_result(y) for y in tr_d[1]]
    training_data = zip(training_inputs,training_results)
   # print training_data[0]
    test_inputs = [np.reshape(x,(len1,1)) for x in te_d[0]]
    test_data = zip(test_inputs,te_d[1])
    return (training_data,test_data)
