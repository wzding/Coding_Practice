"""
Weights and Bias in TensorFlow
The goal of training a neural network is to modify weights and biases to best
predict the labels. In order to use weights and bias, you'll need a Tensor that
can be modified. This leaves out tf.placeholder() and tf.constant(), since
those Tensors can't be modified. This is where tf.Variable class comes in.

You'll use the tf.global_variables_initializer() function to initialize the
state of all the Variable tensors.

Using the tf.Variable class allows us to change the weights and bias,
but an initial value needs to be chosen.

You'll use the tf.truncated_normal() function to generate random numbers
from a normal distribution.
"""
x = tf.Variable(5)
init = tf.global_variables_initializer()
with tf.Session as sess:
    sess.run(init)

n_features = 120
n_labels = 5
weights = tf.Variable(tf.truncated_normal((n_features, n_labels)))
bias = tf.Variable(tf.zeros(n_labels))
