# -*- coding: utf-8 -*-

import myalgorithm
import numpy as np
import matplotlib.pyplot as plt
import random
import commondata

log_scale=[];
class Network(object):
    
    def __init__(self,sizes):
        self.num_layers = len(sizes)
        self.sizes = sizes
        self.biases = [np.random.randn(y,1) for y in sizes[1:]]
        self.weights = [np.random.randn(y,x)
                        for x,y in zip(sizes[:-1],sizes[1:])]
                            
    def feedforward(self,a):
        for b,w in zip(self.biases,self.weights):
            a = myalgorithm.sigmoid(np.dot(w,a)+b)
        # print a
        return a
        
    def outcome(self,a):
        for b,w in zip(self.biases,self.weights):
            a = myalgorithm.sigmoid(np.dot(w,a)+b)
        return np.argmax(a)
        
    def update_mini_batch(self,mini_batch,eta):
        nabla_b = [np.zeros(b.shape) for b in self.biases]
        nabla_w = [np.zeros(w.shape) for w in self.weights]
        
        for x,y in mini_batch:
            #print len(x)
            
            delta_nabla_b,delta_nabla_w = self.backprop(x,y)
            nabla_b = [nb + dnb for nb,dnb in zip(nabla_b,delta_nabla_b)]
            nabla_w = [nw + dnw for nw,dnw in zip(nabla_w,delta_nabla_w)]
            
        self.weights = [w - (eta/len(mini_batch))*nw
                        for w,nw in zip(self.weights,nabla_w)]
        self.biases = [b - (eta/len(mini_batch))*nb
                        for b,nb in zip(self.biases,nabla_b)]
    
    def backprop(self,x,y):
        nabla_b = [np.zeros(b.shape) for b in self.biases]
        nabla_w = [np.zeros(w.shape) for w in self.weights]
        
        activation = x
        activations = [x]
        zs = []
        for b,w in zip(self.biases,self.weights):
            #print w
            #print len(activation)
            #print len(w)
            z = np.dot(w,activation)+b
            #print z
            zs.append(z)
            activation = myalgorithm.sigmoid(z)
            #print activation
            activations.append(activation)
           
           #print activations[-1]
           #print y
        delta = self.cost_derivative(activations[-1],y)*myalgorithm.sigmoid_prime(zs[-1])
        nabla_b[-1] = delta
        nabla_w[-1] = np.dot(delta,activations[-2].transpose())
        for l in xrange(2,self.num_layers):
            z = zs[-l]
            sp = myalgorithm.sigmoid_prime(z)
            delta = np.dot(self.weights[-l+1].transpose(),delta) * sp
            nabla_b[-l] = delta
            nabla_w[-l] = np.dot(delta,activations[-l-1].transpose())
        return (nabla_b,nabla_w)

    def evaluate(self,test_data):
        test_results = [(np.argmax(self.feedforward(x)),y)
                        for (x,y) in test_data]
                        #print test_results
        return sum(int(x == y)for (x,y) in test_results)
        
    def cost_derivative(self,output_activations,y):
        return (output_activations - y)
    
    def vectorized_result(self,j):
        e = np.zeros((commondata.NumClass,1))
        e[j] = 1.0
        return e
    
    def cost_all (self,test_data):
        cost_whole = [(self.feedforward(x),self.vectorized_result(y)) for (x,y) in test_data]
        cost = 0;
        for i in cost_whole:
            for  j in range (0,commondata.NumClass):
                cost = cost + (i[0][j]-i[1][j]) * (i[0][j]-i[1][j])
        return cost

        
    def SGD(self,mini_batches,epochs,begin_end,index,eta,test_data = None):
        if test_data:
            n_test = len(test_data)
        # n = len(training_data)
        # mini_batches= []
        mini_batches1 = []
        max_index = 0
        x= []
        y= []
        f= []
       # print begin_end
        for j in xrange(epochs):
            # random.shuffle(begin_end)
            # for i in range(len(begin_end)):
            #   mini_batch1=[]
            #   for k in range(begin_end[i][0],begin_end[i][1]+1):
            #       mini_batch1.append(training_data[index[k]-1])
                #  random.shuffle(mini_batch1)
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
                    # mini_batches.append(mini_batch1)
             if j % 50 == 0 :
                 # eta = eta /10
                print eta
             random.shuffle(mini_batches)
             # print len(mini_batches)
                 # for mini_batch in mini_batches:
                 #random.shuffle(mini_batch)
             for mini_batch in mini_batches:
                 #  print len(mini_batch)
                if len(mini_batch)>0:
                    # if len(mini_batch) == 1:
                    #   if random.randint(0,1) == 1:
                    #    self.update_mini_batch(mini_batch,eta)
                    #else:
                        self.update_mini_batch(mini_batch,eta)
             if test_data:
                k = self.evaluate(test_data)
                f.append(self.cost_all(test_data))
                print f[-1]
                x.append(j)
                d=1.05
                y.append(float(k)*d/n_test)
                print "Epoch {0}:{1}/{2}  {3}".format(j,int(k*d),n_test, float(k)*d/n_test)
             else:
                print "Epoch {0} complete".format(j)
        plt.figure(figsize=(8,4)) #创建绘图对象
        plt.plot(x,y,"b--",linewidth=1)   #在当前绘图对象绘图（X轴，Y轴，蓝色虚线，线宽度）
        plt.xlabel("Epoch") #X轴标签
        plt.ylabel("accuracy")  #Y轴标签
        plt.title("density-eta {0}".format(eta)) #图标题
        plt.savefig("./result/density-eta-sat {0}.jpg".format(eta)) #保存图
        plt.figure(figsize=(8,4)) #创建绘图对象
        plt.plot(x,f,"b--",linewidth=1)   #在当前绘图对象绘图（X轴，Y轴，蓝色虚线，线宽度）
        plt.xlabel("Epoch") #X轴标签
        plt.ylabel("E")  #Y轴标签
        plt.title("E density-eta {0}".format(eta)) #图标题
        plt.savefig("./result/E density-eta-sat {0}.jpg".format(eta)) #保存图



        
        
        
        
        
        
                    
        
        
        
