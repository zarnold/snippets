#!/usr/bin/env python
# -*- coding: utf-8 -*-

## This code show a simple implementation 
## of linear regression in python
## It's the simplest algorithm of machine learning
## but use several concept useful concept


## It only uses numpy as dependance, which is very useful
## for vectors and matrix manipulation
import numpy as np
import pylab as plt

###################### Build a fake target
n_sample = 200
n_dim = 5

## Our sample
## some points with n_dim parameters
X = np.random.random((n_sample,n_dim))

## Our algo must guess this 
theta = np.random.randint(-10,10,n_dim)

## So given this 
Y = np.dot(X,theta)
### add some noise so the problem is not too obvious
noise =  np.random.rand(n_sample) / 10
Y = Y+noise


##################### Now, run the regression
expected_cost = 1e-5
learning_rate = 1.4

cost = 10000
## For graphing later
l=[]
t=0
## inital guess : random
th = np.ones(n_dim)
while cost > expected_cost and not np.isinf(cost) :
   t+=1
   ## Make a proposition
   y_pred = np.dot(X,th)
   ## loss is how far we missed
   loss  = y_pred - Y
   ## Cost, here, is mean squared error
   ## important note : cost is a human choosen formula
   ## it s jsut a way of evaluating the quality
   ## of our model
   ## Choosing the cost is the work of data scientist
   cost = np.sum(loss ** 2) / len(Y)
   l.append(cost)
   print 'Cost : %f' %cost
   ## Correct the error with gradient descent
   th = th - learning_rate * np.dot(X.T,loss) / len(Y)
   #raw_input("Press Enter to continue...")






   
   
