import tensorflow as tf
import numpy as np
inputW = ""
cell = tf.nn.rnn_cell.LSTMCell(num_units=32, state_is_tuple=True)
model = tf.Model
def magic_func(modelW2V, word):
    vec = modelW2V
    return vec

inputV = magic_func(model)


outputs, states = tf.nn.bidirectional_dynamic_rnn(
    cell_fw=cell,
    cell_bw=cell,
    dtype=tf.float64,
    sequence_length=100,
    inputs=inputV)

cell = tf.nn.rnn_cell.LSTMCell(num_units=64, state_is_tuple=True)
cell = tf.nn.rnn_cell.MultiRNNCell(cells=[cell] * 4, state_is_tuple=True)

result = tf.contrib.learn.run_n(
    {"outputs": outputs, "last_states": last_states},
    n=1,
    feed_dict=None)

# Batch size
B = 4
# (Maximum) number of time steps in this batch
T = 8
RNN_DIM = 128
NUM_CLASSES = 10

# The *acutal* length of the examples
example_len = [1, 2, 3, 8]

# The classes of the examples at each step (between 1 and 9, 0 means padding)
y = np.random.randint(1, 10, [B, T])
for i, length in enumerate(example_len):
    y[i, length:] = 0

# The RNN outputs
rnn_outputs = tf.convert_to_tensor(np.random.randn(B, T, RNN_DIM), dtype=tf.float32)

# Output layer weights
W = tf.get_variable(
    name="W",
    initializer=tf.random_normal_initializer(),
    shape=[RNN_DIM, NUM_CLASSES])

# Calculate logits and probs
# Reshape so we can calculate them all at once
rnn_outputs_flat = tf.reshape(rnn_outputs, [-1, RNN_DIM])
logits_flat = tf.batch_matmul(rnn_outputs_flat, W)
probs_flat = tf.nn.softmax(logits_flat)

# Calculate the losses
y_flat = tf.reshape(y, [-1])
losses = tf.nn.sparse_softmax_cross_entropy_with_logits(logits_flat, y_flat)

# Mask the losses
mask = tf.sign(tf.to_float(y_flat))
masked_losses = mask * losses

# Bring back to [B, T] shape
masked_losses = tf.reshape(masked_losses, tf.shape(y))

# Calculate mean loss
mean_loss_by_example = tf.reduce_sum(masked_losses, reduction_indices=1) / example_len
mean_loss = tf.reduce_mean(mean_loss_by_example)