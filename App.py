import pld
import tensorflow as tf

a = tf.compat.v1.placeholder("float")
b = tf.compat.v1.placeholder("float")

y = tf.multiply(a, b)

sess = tf.compat.v1.Session()

print(sess.run(y, feed_dict={a: 3, b: 3}))
