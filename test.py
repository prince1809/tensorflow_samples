import tensorflow as tf


hello = tf.constant('Hello world')
sess = tf.Session()
sess.run(hello)

a= tf.constant(10)
b = tf.constant(32)
sess.run(a+b)
