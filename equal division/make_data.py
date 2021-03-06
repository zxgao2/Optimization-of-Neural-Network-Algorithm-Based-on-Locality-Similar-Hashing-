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

dirname = 'train'
myfile = 'train.pkl'

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
    float_query = pictures[index-1];
    float_mat = []
    print index, number1
    print index-number1
    for i in range(index-number1,index):
        float_mat.append(pictures[i])
    rhp_mat = pylshbox.rhplsh()
    float_mat=np.array(float_mat)
    rhp_mat.init_mat(float_mat.tolist(), '', 521, 32, 3)
    float_query = np.array(float_query)
    result = rhp_mat.query(float_query.tolist(), 2, number1)
    indices, dists = result[0], result[1]
    group=100
 #   for j in range(group):
  #      float_query = np.array(float_query)
#        print ' '
 #       print(float_query)
#        print ' '
 #       result = rhp_mat.query(float_query.tolist(), 2, (number1/group)+1)
 #       indices, dists = result[0], result[1]
  #      print(len(indices))
  # for i in range(len(indices)):
  #        print indices[i], '\t', dists[i]
  #  print len(indices)
 #   Data_begin.append(commondata.Data_index) 
    for i in range(group):
       Data_begin.append(len(commondata.Data_index)) 
       for j in range(number1/group):
        #print (i*number1/group+j)
        commondata.Data_index.append(indices[i*number1/group+j]+number1*lable+1)
       Data_end.append(len(commondata.Data_index)-1) 
 #   float_query = float_mat[indices[len(indices)-1]]
  #      print indices[len(indices)-1]
    lable = lable + 1
    number1 = 0;
#for i in commondata.Data_index:
#print (commondata.Data_index)
#print(pictures)
commondata.Data_begin_end =zip(Data_begin,Data_end)
commondata.Modify_index(commondata.Data_index)
commondata.Modify_begin(commondata.Data_begin_end)
#for i in commondata.Data_begin_end:
# print i[0],  i[1] 
print len(commondata.Data_index)
lables = lables.astype(numpy.int)
write_file=open(myfile,'wb')
cPickle.dump([pictures[:],lables[:],commondata.Data_begin_end[:],commondata.Data_index[:]],write_file,-1)
write_file.close()
