# %% [markdown]
import pld
import tensorflow as tf

test = tf.constant("TEST")

print(test)

sess = tf.compat.v1.Session()
print(sess.run(test))

X_1 = tf.compat.v1.placeholder(tf.float32, [2, 3])
X_2 = tf.compat.v1.placeholder(tf.float32, [None, 3])
print(X_1)
print(X_2)
# %% [markdown]
# 텐서플로우를 이용하여 행곱을 연산하는 방법
X_3 = tf.placeholder(tf.float32, [2, 4])
x3_data = [[1, 2, 3, 4],
           [4, 3, 2, 1]]

W_1 = tf.placeholder(tf.float32, [4, 2])
w1_data = [[0, 1],
           [1, 2],
           [2, 3],
           [3, 4]]

exp = tf.matmul(X_3, W_1)
session = tf.Session()
session.run(tf.global_variables_initializer())

a = session.run(exp, feed_dict={X_3: x3_data, W_1: w1_data})
session.close()

a
# %% [markdown]
x4 = tf.placeholder(tf.float32, [2, 2])
x4data = [[4, 5],
          [7, 8]]

w2 = tf.Variable(tf.random_normal([2, 2]))

exp = tf.matmul(x4, w2)
session = tf.Session()
session.run(tf.global_variables_initializer())
print(session.run(w2))