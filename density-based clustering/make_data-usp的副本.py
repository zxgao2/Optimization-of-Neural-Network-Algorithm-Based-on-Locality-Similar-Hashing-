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

dirname = 'usps.t'
myfile = 'test-usps.pkl'

number = 2007

pictures = numpy.empty((number,256))
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
    for i in range(1,257):
        line2 =line1[i].split(':')
        a.append(float(line2[1]))
    image_narray = numpy.asarray(a,dtype = 'float64')
    pictures[index] = numpy.ndarray.flatten(image_narray)
    lables[index] = int(line1[0])-1
    index= index+1
'''
Center = []
Center_index = [0] *number
Center_dist = []
file = open("tmp-usps.txt")



n = 0
m= 1000000
id=0;
ineline1= ''
for line in file:
    n= n + 1
    if n <= m :
            if n == 1 :
                lineline1 = line.rstrip('\n')
                m = int(lineline1)+1
            else :
                lineline = line.rstrip('\n')
                Center.append(int(lineline))
    else:
            lineline = line.rstrip('\n')
            # print lineline
            #print "id",id
            Center_index[id] = int(float(lineline))
            id = id + 1
# print 'in',id,number1
#    for i in Center_index:
#  print i
for i in range (0,int(lineline1)):
        Data_begin.append(len(commondata.Data_index))
        for j in range(0,number):
            if Center_index[j] == Center[i]:
                commondata.Data_index.append(j+1)
        Data_end.append(len(commondata.Data_index)-1)

file.close()

'''

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
