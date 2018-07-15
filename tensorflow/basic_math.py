import tensorflow as tf
x = tf.add(2, 5)
y = tf.subtract(10, 6)
z = tf.multiply(2, 5)

"""
It may be necessary to convert between types to make certain operators work together.
For example, if you tried the following, it would fail with an exception:
"""
tf.subtract(tf.constant(2.0), tf.constant(1))
# convert types
tf.subtract(tf.cast(tf.constant(2.0), tf.int32), tf.constant(1))

def get_weights(n_features, n_labels):
    """
    Return TensorFlow weights
    :param n_features: Number of features
    :param n_labels: Number of labels
    :return: TensorFlow weights
    """
    weights = tf.Variable(tf.truncated_normal((n_features, n_labels)))
    return weights


def get_biases(n_labels):
    """
    Return TensorFlow bias
    :param n_labels: Number of labels
    :return: TensorFlow bias
    """
    biases = tf.Variable(tf.zeros(n_labels))
    return biases
    
def linear(input, w, b):
    """
    Return linear function in TensorFlow
    :param input: TensorFlow input
    :param w: TensorFlow weights
    :param b: TensorFlow biases
    :return: TensorFlow linear function
    """
    # TODO: Linear Function (xW + b)
    return tf.add(tf.matmul(input, w) ,b)
