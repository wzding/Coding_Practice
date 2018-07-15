"""
As with the softmax function, TensorFlow has a function to do the cross entropy calculations for us.
To create a cross entropy function in TensorFlow, you'll need to use two new functions:

tf.reduce_sum()
tf.log()
"""
import tensorflow as tf

softmax_data = [0.7, 0.2, 0.1]
one_hot_data = [1.0, 0.0, 0.0]

softmax = tf.placeholder(tf.float32)
one_hot = tf.placeholder(tf.float32)

cross_entropy = -tf.reduce_sum(tf.multiply(one_hot, tf.log(softmax)))

# TODO: Print cross entropy from session
with tf.Session() as sess:
    print(sess.run(cross_entropy,
    feed_dict={one_hot: one_hot_data, softmax: softmax_data}))
