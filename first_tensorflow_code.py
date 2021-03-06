# -*- coding: utf-8 -*-
"""first tensorflow code.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/12-dS0hRl8bX8msoTFlEQIW_6cnc_YCFn
"""

import tensorflow as tf

zero_tensor = tf.zeros([3,3])

print(zero_tensor)

ones_tensor = tf.ones([1,1])

print(ones_tensor)

fill_tensor = tf.fill([4,4], 16)
print(fill_tensor)

first_constant =tf.constant([[1,2,3], [3,4,5]])
print(first_constant)

mess_constant = tf.constant(['Kaiser'])
print(mess_constant)

lins_tensor = tf.linspace(0.,9.,6)
print(lins_tensor)

range_tensor =tf.range(3.,6.,0.5)
print(range_tensor)

mat= tf.constant([[1.,2.,3.],[4.,5.,6.],[7.,8.,9.]])

slic = tf.slice(mat,[1,1],[2,2])
print(slic)

mat= tf.constant([[1.,2.,3.],[4.,5.,6.],[7.,8.,9.]])
rev=tf.reverse(mat,[0])
print(rev)



x = tf.constant([1.,2.,3.])
y= tf.constant([6.,7.,8.])

sum = tf.add(x,y)
print(sum)

mul = tf.multiply(x,y)
print(mul)

div = tf.divide(x,y)
print(div)

div2 = x/y
print(div2)

rep =tf.sign(x)
print(rep)

sq = tf.square(x)
print(sq)

sqt = tf.sqrt(x)
print(sqt)

rsqt = tf.pow(x,y)
print(rsqt)

cel = tf.floor(div)
print(cel)

expon = tf.exp(x)
print(expon)

dot = tf.tensordot(x,y,axes =0)
print(dot)

x = tf.constant([1.,2.,3.])
y= tf.constant([6.,7.,8.])

norm_mat = tf.norm(x,ord='euclidean', axis=None, keepdims=None, name=None)
print(norm_mat)

