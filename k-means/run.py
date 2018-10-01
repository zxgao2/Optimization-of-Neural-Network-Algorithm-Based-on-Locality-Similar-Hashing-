# -*- coding: utf-8 -*-
import data
import random
training_data,test_data,begin_end,index = data.load_data_wrapper()

import network
net = network.Network([1024,30,10])
#random.shuffle(begin_end)
mini_batches= []
print len(begin_end)
    #for  i in range(0,len(begin_end)):
    #print 'set',i
    #n = 0
    #for k in range(begin_end[i][0],begin_end[i][1]+1):
    # print index[k]
    # n= n+1
#print 'set',i, n
for i in range(len(begin_end)):
    mini_batch1=[]

    for k in range(begin_end[i][0],begin_end[i][1]+1):
        mini_batch1.append(training_data[index[k]-1])
    random.shuffle(mini_batch1)
    print len(mini_batch1)
        #    if len(mini_batch1) > max_index:
        #max_index = len(mini_batch1)
        #mini_batches.append(mini_batch1)
        #for i in range (max_index):
        #mini_batch1= []
        #for k in range(len(mini_batches)):
        #if len(mini_batches[k]) > i :
        #   mini_batch1.append(mini_batches[k][i])
        #else :
        #    mini_batch1.append(mini_batches[k][random.randint(0,len(mini_batches[k])-1)])
    mini_batches.append(mini_batch1)
d=15.0
    #for i in range(10):
    
d=d / 10
    #print(d)
net.SGD(mini_batches,1000,begin_end,index,d,test_data = test_data)

import cPickle
write_file = open('weight.pkl','wb')
cPickle.dump([net.weights[:],net.biases[:]],write_file,-1)
write_file.close()

