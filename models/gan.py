#!/bin/env python3

import numpy as np
import tensorflow as tf

# placeholders for data
dimg = tf.placeholder('float', [None, 784], name='data')
labels = tf.placeholder('float', [None, 10], name='labels')

# weight matrices and bias vectors
dw1 = tf.Variable(tf.random_normal([5,5,1,32], stddev=1), name='w1')
dw2 = tf.Variable(tf.random_normal([5,5,32,64], stddev=1), name='w2')
dw3 = tf.Variable(tf.random_normal([7*7*64, 1024], stddev=1), name='w3')
dw4 = tf.Variable(tf.random_normal([1024, 10], stddev=1), name='w4')

db1 = tf.Variable(tf.random_normal([32], stddev=1), name='b1')
db2 = tf.Variable(tf.random_normal([64], stddev=1), name='b2')


# generator network
def g(noise,gw1,gw2,gw3,gw4,gb1,gb2):
	with tf.name_scope('input'):
		layer1 = tf.nn.relu(tf.matmul(noise, gw1))
	with tf.

# discriminator network
def d(dimg,dw1,dw2,dw3,dw4,db1,db2):
	with tf.name_scope('input'):
		layer1 = tf.reshape(data, [-1, 28, 28, 1])
	with tf.name_scope('conv_1'):
		conv1 = tf.nn.conv2d(layer1, filter=dw1, strides=[1,1,1,1], padding='SAME')
		conv1b = tf.nn.relu(conv1 + db1)
		pool1 = tf.nn.max_pool(conv1b, ksize=[1,2,2,1], strides=[1,2,2,1], padding='SAME')
	with tf.name_scope('conv_2'):
		conv2 = tf.nn.conv2d(pool1, filter=dw2, strides=[1,1,1,1], padding='SAME')
		conv2b = tf.nn.relu(conv2 + db2)
		pool2 = tf.nn.max_pool(conv2b, ksize=[1,2,2,1], strides=[1,2,2,1], padding='SAME')
	with tf.name_scope('flatten'):
		flat = tf.reshape(pool2, [-1, 7 * 7 * 64])
	with tf.name_scope('dense'):
		dense1 = tf.nn.relu(tf.matmul(flat, dw3))
	with tf.name_scope('output'):
		out = tf.matmul(dense1, dw4)
		return out

# loss function

# training operation

# session

