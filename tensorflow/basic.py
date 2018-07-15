# In TensorFlow, data isn’t stored as integers, floats, or strings.
# These values are encapsulated in an object called a tensor.

import tensorflow as tf
# Create TensorFlow object called hello_constant
# hello_constant is a 0-dimensional string tensor
hello_constant = tf.constant('Hello World!')
# Session
# TensorFlow’s api is built around the idea of a computational graph, a way of
# visualizing a mathematical process which you learned about in the MiniFlow
# lesson. Let’s take the TensorFlow code you ran and turn that into a graph
with tf.Session() as sess:
    # Run the tf.constant operation in the session
    output = sess.run(hello_constant)
    print(output)


"""
What if you want to use a non-constant? This is where tf.placeholder() and
feed_dict come into place.
tf.placeholder() returns a tensor that gets its value from data passed to the
tf.session.run() function, allowing you to set the input right before the
session runs.
"""
