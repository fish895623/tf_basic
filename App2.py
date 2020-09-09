import pld
import tensorflow as tf

test = tf.constant("TEST")

print(test)

sess = tf.compat.v1.Session()
print(sess.run(test))
