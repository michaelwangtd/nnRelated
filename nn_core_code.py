#!/usr/bin/env python
# -*- coding:utf-8 -*-

import tensorflow as tf
import numpy as np

if __name__ == '__main__':

    # network structure
    D_input = 2
    D_hidden = 2
    D_label = 1
    lr = 1e-4

    ## container
    x = tf.placeholder(tf.float32,shape=[None,D_input],name='x')    # input
    t = tf.placeholder(tf.float32,shape=[None,D_label],name='t')    # output
    '''
        dtype：数据类型。常用的是tf.float32,tf.float64等数值类型
        shape：数据形状。默认是None，就是一维值，也可以是多维，比如[2,3], [None, 3]表示列是3，行不定
        name：名称。
    '''

    ## hidden layer
    # init W
    W_h1 = tf.Variable(tf.truncated_normal([D_input,D_hidden],stddev=0.1),name='W_h')
    # init b
    b_h1 = tf.Variable(tf.constant(0.1,shape=[D_hidden]),name='b_h')    # [0.1,0.1]
    '''
        tensorflow中的变量tf.Variable是用于定义在训练过程中可以更新的值。权重W和偏移b正符合该特点。
        tf.truncated_normal([matrix row,matrix col],stddev标准差):截断方式产生正态分布
        tf.constant(constant num ,shape):产生shape形状的常量
    '''
    # calculate
    pre_act_h1 = tf.matmul(x,W_h1) + b_h1
    # activation fuc
    act_h1 = tf.nn.relu(pre_act_h1,name='act_h')

    ## output layer（process similar to hidden layer）
    W_o = tf.Variable(tf.truncated_normal([D_hidden,D_label],stddev=0.1),name='W_o')
    b_o = tf.Variable(tf.constant(0.1,shape=[D_label]),name='b_o')
    pre_act_o = tf.matmul(act_h1,W_o) + b_o
    y = tf.nn.relu(pre_act_o,name='act_y')

    ## feedback
    # loss fun
    loss = tf.reduce_mean((y - t) ** 2)

    # train update weight and bias
    train_step = tf.train.AdamOptimizer(lr).minimize(loss)
    '''
        选择想要用于更新权重的训练方法和每次更新步伐（lr），除tf.train.AdamOptimizer外还有tf.train.RMSPropOptimizer等。默认推荐AdamOptimizer。
    '''

    ## init data
    X = [[0,0],[0,1],[1,0],[1,1]]
    Y = [[0],[1],[1],[0]]
    X = np.array(X).astype('int16')
    Y = np.array(Y).astype('int16')

    ## load model
    # 1 create session
    sess = tf.InteractiveSession()
    '''
        sess = tf.InteractiveSession()是比较方便的创建方法
        也有sess = tf.Session()方式
        但该方式无法使用tensor.eval()快速取值等功能
    '''
    # 2 init params

    # tf.initialize_all_variables().run()   deprecated
    init = tf.global_variables_initializer()
    sess.run(init)

    ## train model（GD 方式）
    T = 10000
    for i in range(T):
        # print 'training index: ',i
        sess.run(train_step,feed_dict={x:X,t:Y})
    '''
        这里训练网络的方式有几种：
            （1）GD：将所有数据输入到网络，算出平均梯度来更新一次网络的方法叫做GD
            （2）SGD：一次只输入一个训练数据到网络，算出梯度来更新一次网络的方法叫做SGD
            （3）batch-GD:这是上面两个方法的折中方式。每次计算部分数据的平均梯度来更新权重。部分数据的数量大小叫做batch_size
            （4）shuffle：shuffle是用于打乱数据在矩阵中的排列顺序
    '''

    ## predict
    print('X: ',X)
    print('Y: ',Y)

    print(sess.run(y,feed_dict={x:X}))

    print(sess.run(act_h1,feed_dict={x:X}))












