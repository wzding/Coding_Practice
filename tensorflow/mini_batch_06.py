"""
Mini-batching is a technique for training on subsets of the dataset instead of
all the data at one time. This provides the ability to train a model, even if
a computer lacks the memory to store the entire dataset.

Mini-batching is computationally inefficient, since you can't calculate the loss
simultaneously across all samples. However, this is a small price to pay in
order to be able to run the model at all.

It's also quite useful combined with SGD. The idea is to randomly shuffle the
data at the start of each epoch, then create the mini-batches. For each
mini-batch, you train the network weights with gradient descent. Since these
batches are random, you're performing SGD with each batch.

Let's look at the MNIST dataset with weights and a bias to see if your machine
can handle itself.
The total memory space required for the inputs, weights and bias is around 174
megabytes, which isn't that much memory. You could train this whole dataset
on most CPUs and GPUs.
"""
import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data
import numpy as np
from helper import batches

learning_rate = 0.001
n_input = 784  # MNIST data input (img shape: 28*28)
n_classes = 10  # MNIST total classes (0-9 digits)
# Import MNIST data
mnist = input_data.read_data_sets('MNIST_DATA/', one_hot=True)

# features are already scaled
train_features = mnist.train.images
test_features = mnist.test.images
train_labels = mnist.train.labels.astype(np.float32)
test_labels = mnist.test.labels.astype(np.float32)

# weights and bias
weights = tf.Variable(tf.random_normal([n_input, n_classes]))
bias = tf.Variable(tf.random_normal([n_classes]))

"""
In order to use mini-batching, you must first divide your data into batches.
Unfortunately, it's sometimes impossible to divide the data into batches of
exactly equal size. In that case, the size of the batches would vary, so you
need to take advantage of TensorFlow's tf.placeholder() function to receive
the varying batch sizes.

The None dimension is a placeholder for the batch size. At runtime,
TensorFlow will accept any batch size greater than 0.
"""
features = tf.placeholder(tf.float32, [None, n_input])
labels = tf.placeholder(tf.float32, [None, n_classes])

# Logits - xW + b
logits = tf.add(tf.matmul(features, weights), bias)
# Define loss and optimizer
cost = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(logits=logits, labels=labels))
optimizer = tf.train.GradientDescentOptimizer(learning_rate=learning_rate).minimize(cost)
# Calculate accuracy
correct_prediction = tf.equal(tf.argmax(logits, 1), tf.argmax(labels, 1))
accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))

# Set batch size
batch_size = 128
assert batch_size is not None, 'You must set the batch size'


init = tf.global_variables_initializer()
with tf.Session() as sess:
    sess.run(init)

    # Train optimizer on all batches
    for batch_features, batch_labels in batches(batch_size, train_features, train_labels):
        sess.run(optimizer, feed_dict={features: batch_features, labels: batch_labels})

    # Calculate accuracy for test dataset
    test_accuracy = sess.run(
        accuracy,
        feed_dict={features: test_features, labels: test_labels})

print('Test Accuracy: {}'.format(test_accuracy))
# Test Accuracy: 0.12559999525547028
"""
The accuracy is low, but you probably know that you could train on the dataset
more than once. You can train a model using the dataset multiple times.
"""
