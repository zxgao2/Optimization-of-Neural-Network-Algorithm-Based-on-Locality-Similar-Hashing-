# -*- coding: utf-8 -*-
import libpylshbox as pylshbox
import numpy as np
import time
from sklearn import datasets
import os
import cPickle
import numpy
from PIL import Image
import commondata
import math

dirname = 'dna.scale.txt'
myfile = 'train-dna.pkl'

number = 2000


pictures = numpy.empty((number,180))
lables = numpy.empty(number)

index = 0
lable = 0
index1 = 0
number1 = 0
Data_begin = []
Data_end = []
file = open(dirname)

while 1:
    line = file.readline()
    if not line:
        break
    a = []
    line1 = line.split(' ')
    k=1;
    for i in range(1,181):
        # print line1[i]
        #  print k
        if k<len(line1)-1:
            line2 =line1[k].split(':')
        if int(line2[0]) == i :
            a.append(float(line2[1]))
            k=k+1
        else:
            a.append(0)
# print  a

    image_narray = numpy.asarray(a,dtype = 'float64')
    pictures[index] = numpy.ndarray.flatten(image_narray)
    lables[index] = int(line1[0])-1
    index= index+1

float_query = pictures[23];
dists=[]
indices = []
for i in range (0, index):
    k= 0
    for j in range(0,180):
     k = k+ ((pictures[i].tolist())[j] - (float_query.tolist())[j]) *((pictures[i].tolist())[j] - (float_query.tolist())[j])
    dists.append(math.sqrt(k))
    indices.append(i)

for i in range (0,index-1):
    for j in range (i+1,index):
        if dists[i]> dists[j] :
            m = dists[i]
            dists[i]=dists[j]
            dists[j]=m
            m=indices[i]
            indices[i]=indices[j]
            indices[j]=m


k = (dists[len(indices)-1] - dists[0]) /(index)
k1 = dists[1]
print(k)
Data_begin.append(len(commondata.Data_index))
for i in range(len(indices)):
        #commondata.Data_index.append(indices[i]+number1*lable+1)
        #print (dists[i] - k1)
        if i < len(indices)-1 :
         if (dists[i] - k1) <=  k :
            #print (i*number1/group+j)
                commondata.Data_index.append(indices[i]+1)
                k1 = dists[i]
                continue
         else :
                    Data_end.append(len(commondata.Data_index)-1)
                    commondata.Data_index.append(indices[i]+1)
                    Data_begin.append(len(commondata.Data_index)-1)
                                
        else:
                    commondata.Data_index.append(indices[i]+1)
                    Data_end.append(len(commondata.Data_index)-1)
                                            
        k1 = dists[i]



commondata.Data_begin_end =zip(Data_begin,Data_end)
commondata.Modify_index(commondata.Data_index)
commondata.Modify_begin(commondata.Data_begin_end)
for i in commondata.Data_begin_end:
    print i[0],  i[1]
print len(commondata.Data_begin_end)


lables = lables.astype(numpy.int)
write_file=open(myfile,'wb')
cPickle.dump([pictures[:],lables[:],commondata.Data_begin_end[:],commondata.Data_index[:]],write_file,-1)
write_file.close()
