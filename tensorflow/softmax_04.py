"""
The softmax function squashes it's inputs, typically called logits or logit
scores, to be between 0 and 1 and also normalizes the outputs such that they
all sum to 1. This means the output of the softmax function is equivalent to
a categorical probability distribution. It's the perfect function to use as
the output activation for a network predicting multiple classes.

tf.nn.softmax() implements the softmax function for you. It takes in
logits and returns softmax activations.
"""
import tensorflow as tf

def run():
    output = None
    logit_data = [2.0, 1.0, 0.1]
    logits = tf.placeholder(tf.float32)

    # TODO: Calculate the softmax of the logits
    softmax = tf.nn.softmax(logits)

    with tf.Session() as sess:
        # TODO: Feed in the logit data
        output = sess.run(softmax, feed_dict={logits: logit_data})

    return output
