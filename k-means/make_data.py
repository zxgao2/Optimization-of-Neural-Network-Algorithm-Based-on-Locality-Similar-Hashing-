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
myfile = 'train2.pkl'

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
 if filename == '.DS_Store' or filename == '0' or filename == '6' or filename == '7' or filename == '8' or filename == '9' : 
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
           image_narray = numpy.asarray(image,dtype = 'float64')/256
           pictures[index] = numpy.ndarray.flatten(image_narray)
           lables[index] = lable
           index = index + 1
           number1 += 1
    float_query = pictures[index-number1];
    float_mat = []
    print index, number1
    print index-number1
    for i in range(index-number1,index):
        float_mat.append(pictures[i])
    Center = []
    Center_index = []
    Center_dist = []

    for i in range(0,k):
        p = random.randint(0,number1-1)
        Center_index.append(p)
        Center.append(float_mat[p])
        Center_dist.append(10000.0)
    Boolean = 0
    ff=0
    while (Boolean < k) :
        print ff
        Flat = [0] * number1
        Flat_dist = [10000.0] * number1
        num= 0;
        for i in range(0,k):
            for j in range(0,number1):
                dist = math.sqrt(sum([(Center[i][m] - float_mat[j][m]) * (Center[i][m] - float_mat[j][m]) for m in range(0,len(Center[i]))]))
                    #  if Center_index[i] == j :
                    #print 'index',j,dist
                    #if dist == 0.0:
                    #num=+1
                
                if Flat_dist[j] > dist :
                    Flat_dist[j] =dist
                    Flat[j] = i
#   print 'num',num
#  print 'step one '
        dist_1 = [[0 for i in range(len(Center[0]))] for i in range(k)]
        l = [0] * k
        for j in range(0,number1):
            for m in range (0,len(Center[0])):
                    dist_1[Flat[j]][m] = dist_1[Flat[j]][m] + float_mat[j][m]
            #print dist_1[Flat[j]][m]
            l[Flat[j]] = l [Flat[j]] + 1
# for i in range(0,k):
# print l[i]
#      print 'step two'

        for j in range(0,k):
            if l[j]>0 :
                g = 0
                for m in range (0,len(Center[0])):
                    # print dist_1[j][m], l[j],j
                    dist_1[j][m] = dist_1[j][m] / l[j]
                    g = g+(Center[j][m] - dist_1[j][m])*(Center[j][m] - dist_1[j][m])
                g = math.sqrt(g)
                if abs(Center_dist[j] - g) < 0.1 :
                    Boolean = Boolean +1
                #print 'Boolean',Boolean
                else :
                    Boolean = 0
                #  print 'g',g
                Center_dist[j] = g
# print Center_dist[j]
# print 'step three'
        if Boolean < k :
            for i in range(0,k):
                Center[i] = dist_1[i]
#  print Center[i]
#print 'Boolean', Boolean
        ff = ff+1

    for i in range (0,k):
        Data_begin.append(len(commondata.Data_index))
        for j in range(0,number1):
            if Flat[j] == i:
             commondata.Data_index.append(j+index-number1+1)
        Data_end.append(len(commondata.Data_index)-1)
    lable= lable +1
    number1 = 0












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
