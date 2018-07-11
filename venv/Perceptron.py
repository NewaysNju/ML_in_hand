#! /usr/bin/env python3
# -*- coding:utf-8 -*-
# @Author   : niuhui
# @Email    : niuhui1@jd.com
# @Time     : 2018/6/19 16:06

def dot(x, y):
    sum = 0
    for i in range(len(x)):
        sum += x[i] * y[i]
    return sum
def add(x,y):
    sumv = []
    for i, j in zip(x, y):
        sumv.append(i + j)
    return sumv
def listm(a, v):
    for i in range(len(v)):
        v[i] = a * v[i]
    return v

class Perceptron(object):
    def __init__(self, w0, b0, alpha):
        self.initial_w = w0
        self.initial_b = b0
        self.learning_rate = alpha


    def trainmodel(self, train, label):
        self.w = self.initial_w
        self.b = self.initial_b
        misflag = True
        while misflag:
            misflag = False
            for i in range(len(train)):
                if (dot(self.w,train[i])+self.b)*label[i] <= 0:
                    misflag = True
                    self.w = add(self.w, listm(self.learning_rate * label[i],train[i]))
                    self.b = self.b + self.learning_rate * label[i]
                    break



    def predict(self, test):
        if dot(self.w, test) + self.b > 0:
            return 1
        elif dot(self.w, test) + self.b < 0:
            return 0
        else:
            return '无法判断'


if __name__ == '__main__':
    train = [[3,3],[4,3],[1,1]]
    label = [1,1,-1]
    model = Perceptron([0,0],0,1)
    model.trainmodel(train, label)
    print(model.predict([4,3]))
