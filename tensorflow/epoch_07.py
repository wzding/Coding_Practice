"""
An epoch is a single forward and backward pass of the whole dataset. This is
used to increase the accuracy of the model without requiring more data. This
section will cover epochs in TensorFlow and how to choose the right number of epochs.
"""
import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data
import numpy as np
from helper import batches

def print_epoch_stats(epoch_i, sess, last_features, last_labels):
    """
    print cost and validation accuracy of an epoch
    """
    current_cost = sess.run(
        cost,
        feed_dict={features: last_features, labels: last_labels})
    valid_accuracy = sess.run(
        accuracy,
        feed_dict={features: valid_features, labels: valid_labels})
    print("Epoch: {:<4} - Cost: {:<8.3} Valid Accuracy: {:<5.3}".format(
        epoch_i,
        current_cost,
        valid_accuracy))

n_input = 784
n_classes = 10

mnist = input_data.read_data_sets('MNIST_DATA/', one_hot=True)
train_features = mnist.train.images
valid_features = mnist.validation.images
test_features = mnist.test.images
train_labels = mnist.train.labels.astype(np.float32)
valid_labels = mnist.validation.labels.astype(np.float32)
test_labels = mnist.test.labels.astype(np.float32)

features = tf.placeholder(tf.float32, [None, n_input])
labels = tf.placeholder(tf.float32, [None, n_classes])

weights = tf.Variable(tf.random_normal([n_input, n_classes]))
bias = tf.Variable(tf.random_normal([n_classes]))

logits = tf.add(tf.matmul(features, weights), bias)

learning_rate = tf.placeholder(tf.float32)
cost = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(logits=logits,labels=labels))
optimizer = tf.train.GradientDescentOptimizer(learning_rate=learning_rate).minimize(cost)

correct_prediction = tf.equal(tf.argmax(logits, 1), tf.argmax(labels, 1))
accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))

init = tf.global_variables_initializer()

batch_size = 128
epochs = 80
learn_rate = 0.001

train_batches = batches(batch_size, train_features, train_labels)
with tf.Session() as sess:
    sess.run(init)

    for epoch_i in range(epochs):
        for batch_features, batch_labels in train_batches:
            train_feed_dict = {
                features: batch_features,
                labels: batch_labels,
                learning_rate: learn_rate}
            sess.run(optimizer, feed_dict=train_feed_dict)
            print_epoch_stats(epoch_i, sess, batch_features, batch_labels)
    test_accuracy = sess.run(
        accuracy,
        feed_dict={features: test_features, labels: test_labels})
    print('Test Accuracy: {}'.format(test_accuracy))
"""
This model continues to improve accuracy up to Epoch 9.
Let's increase the number of epochs to 100.
From looking at the output above, you can see the model doesn't increase the
validation accuracy after epoch 80. Let's see what happens when we increase
the learning rate to 0.1
Looks like the learning rate was increased too much. The final accuracy was
lower, and it stopped improving earlier. Let's stick with the previous learning
rate, but change the number of epochs to 80.
The accuracy only reached 0.86, but that could be because the learning rate was
too high. Lowering the learning rate would require more epochs, but could
ultimately achieve better accuracy.
"""
