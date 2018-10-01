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
import random
import math
dirname = 'train'
myfile = 'train3.pkl'

number = 0
for filename in os.listdir(dirname):
 if filename == '.DS_Store':
  continue
 else:
    filename1 = dirname + '/' + filename
    for filename2 in os.listdir(filename1):
        if filename2 == '.DS_Store':
         continue
        else:
         number += 1

pictures = numpy.empty((number,commondata.ImageWidth*commondata.ImageHeight))
lables = numpy.empty(number)

index = 0
lable = 0
index1 = 0
number1 = 0
Data_begin = []
Data_end = []
k = 200
for filename in os.listdir(dirname):
 if filename == '.DS_Store' or filename == '0' or filename == '6' or filename == '7' or filename == '8' or filename == '9'  or filename == '1' :
  continue
 else:
    filename1 = dirname + '/' + filename
    for filename2 in os.listdir(filename1):
        if filename2 == '.DS_Store' :
            continue
        else:
           filename2 = filename1 + '/' + filename2
           image = Image.open(filename2)
           image = image.convert('L')
           image = image.resize((commondata.ImageHeight,commondata.ImageWidth))
           image_narray = numpy.asarray(image,dtype = 'float64')/100
           pictures[index] = numpy.ndarray.flatten(image_narray)
           lables[index] = lable
           index = index + 1
           number1 += 1
    float_query = pictures[index-number1];
    float_mat = []
    print index, number1
    print index-number1
    Center = []
    Center_index = [0] *number1
    Center_dist = []
    for i in range(index-number1,index):
        float_mat.append(pictures[i])

    if lable==0 :
      file = open("tmp2.txt")
    
    if lable==1:
            file = open("tmp3.txt")

    if lable==2:
                file = open("tmp4.txt")

    if lable==3:
                    file = open("tmp5.txt")
                    #if lable ==4:
                    #file = open("tmp5.txt")
    
    #
    '''
    if lable == 0 :
        file = open("tmp-test.txt")
    else:
        file =open("tmp-test1.txt")
    '''
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
            Center_index[id] = int(float(lineline))
            id = id + 1
    print 'in',id,number1
#    for i in Center_index:
#  print i
    for i in range (0,int(lineline1)):
        Data_begin.append(len(commondata.Data_index))
        for j in range(0,number1):
            if Center_index[j] == Center[i]:
             commondata.Data_index.append(j+index-number1+1)
        Data_end.append(len(commondata.Data_index)-1)
    lable= lable +1
    number1 = 0
    file.close()












commondata.Data_begin_end =zip(Data_begin,Data_end)
commondata.Modify_index(commondata.Data_index)
commondata.Modify_begin(commondata.Data_begin_end)
for i in commondata.Data_begin_end:
 print i[0],  i[1]
for i in commondata.Data_index:
 print i
print len(commondata.Data_begin_end)
lables = lables.astype(numpy.int)
write_file=open(myfile,'wb')
cPickle.dump([pictures[:],lables[:],commondata.Data_begin_end[:],commondata.Data_index[:]],write_file,-1)
write_file.close()
