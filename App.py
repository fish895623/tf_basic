import pld
import tensorflow as tf


# 사용할 데이터 정의
x_data = [1, 2, 3]
y_data = [1, 2, 3]


# W, X, Y 정의
# W = tf.Variable(tf.random_normal([1]), name='weight')
W = tf.Variable(5.0)
X = tf.compat.v1.placeholder(tf.float32, shape=[None], name='x')
Y = tf.compat.v1.placeholder(tf.float32, shape=[None], name='y')


# 사용할 식 정의. linear regression
hypothesis = W * X
# cost func 정의
# cost(W, b) = (1/m) * sigma(i = 1 ~ m)((W * X) - Y)^2
cost = tf.reduce_mean(tf.square(hypothesis - Y))


# minimize하기
# GradientDescentOptimizer의 식
# W := W - a * (1/m) * sigma(i = 1 ~ m)((W*xi - yi) * xi)
# 어느 정도로 시도할 것인지 결정
learning_rate = 0.1  # a
# 기울기 값
# (1/m) * sigma(i = 1 ~ m)((W*xi - yi) * xi)
gradient_W = tf.reduce_mean((W * X - Y) * X)

# W - a * (1/m) * sigma(i = 1 ~ m)((W*xi - yi) * xi)
descent_W = W - learning_rate * gradient_W

# W에 descent값을 재할당 한다.

# W := W - a * (1/m) * sigma(i = 1 ~ m)((W*xi - yi) * xi)
update_W = W.assign(descent_W)


# 세션 열기
sess = tf.compat.v1.Session()

# Variable 초기화하기
sess.run(tf.compat.v1.global_variables_initializer())

for step in range(101):
    sess.run(update_W, feed_dict={X: x_data, Y: y_data})
    print(step, sess.run(cost, feed_dict={X: x_data, Y: y_data}), sess.run(W))