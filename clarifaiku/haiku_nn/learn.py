import tensorflow as tf
import math
import random
import collections
import numpy as np
import re
from models import *
import os
from django.conf import settings

re_word = re.compile(r"[a-zA-Z']+")
#Returns Array of arrays of three line arrays, each of which is tokenized into words.
#In other words, returns haiku[haiku][line][word]
def get_words():
    return [[re.findall(re_word, line.lower()) for line in [haiku.line1, haiku.line2, haiku.line3]]
            for haiku in Haiku.objects.all()]
# datastring = """
# You never feed me.
# Perhaps I'll sleep on your face.
# That will sure show you.
# You're always typing.
# Well, let's see you ignore my
# sitting on your hands. In deep sleep hear sound
# cat vomit hairball somewhere
# will find in"""


# vocabulary_size = len(words)
# embedding_size = vocabulary_size
# batch_size = vocabulary_size
# #print vocabulary_size
# num_sampled = vocabulary_size/5
# #print num_sampled
# num_skips = 2
# skip_window = 1
# sess = tf.InteractiveSession()
# data_index = 0
#
#
# def build_dataset(words):
#     count = [['UNK', -1]]
#     count.extend(collections.Counter(words).most_common(vocabulary_size - 1))
#     dictionary = dict()
#     for word, _ in count:
#         dictionary[word] = len(dictionary)
#     data = list()
#     unk_count = 0
#     for word in words:
#         if word in dictionary:
#           index = dictionary[word]
#         else:
#           index = 0  # dictionary['UNK']
#           unk_count += 1
#         data.append(index)
#     count[0][1] = unk_count
#     reverse_dictionary = dict(zip(dictionary.values(), dictionary.keys()))
#     return data, count, dictionary, reverse_dictionary
# data, count, dictionary, reverse_dictionary = build_dataset(words)
# print('Most common words (+UNK)', count[:6])
# print('Sample data', data[:10], [reverse_dictionary[i] for i in data[:10]])
#
# def generate_batch(batch_size, num_skips, skip_window):
#     global data_index
#     assert batch_size % num_skips == 0
#     assert num_skips <= 2 * skip_window
#     batch = np.ndarray(shape=batch_size, dtype=np.int32)
#     labels = np.ndarray(shape=(batch_size, 1), dtype=np.int32)
#     span = 2 * skip_window + 1  # [ skip_window target skip_window ]
#     buffer = collections.deque(maxlen=span)
#     for _ in range(span):
#         buffer.append(data[data_index])
#         data_index = (data_index + 1) % len(data)
#     for i in range(batch_size // num_skips):
#         target = skip_window  # target label at the center of the buffer
#         targets_to_avoid = [skip_window]
#         for j in range(num_skips):
#             while target in targets_to_avoid:
#                 target = random.randint(0, span - 1)
#             targets_to_avoid.append(target)
#             batch[i * num_skips + j] = buffer[skip_window]
#             labels[i * num_skips + j, 0] = buffer[target]
#     buffer.append(data[data_index])
#     data_index = (data_index + 1) % len(data)
#     return batch, labels
#
# batch, labels = generate_batch(batch_size=8, num_skips=2, skip_window=1)
# for i in range(8):
#     print(batch[i], reverse_dictionary[batch[i]], '->', labels[i, 0], reverse_dictionary[labels[i, 0]])
#
# train_inputs = tf.placeholder(tf.int32, shape=[batch_size])
# train_labels = tf.placeholder(tf.int32, shape=[batch_size, 1])
#
# embeddings = tf.Variable(
#     tf.random_uniform([vocabulary_size, embedding_size], -1.0, 1.0))
# embed = tf.nn.embedding_lookup(embeddings, train_inputs)
#
# nce_weights = tf.Variable(
#   tf.truncated_normal([vocabulary_size, embedding_size],
#                       stddev=1.0 / math.sqrt(embedding_size)))
# nce_biases = tf.Variable(tf.zeros([vocabulary_size]))
#
# loss = tf.reduce_mean(
#   tf.nn.nce_loss(nce_weights, nce_biases, embed, train_labels,
#                  num_sampled, vocabulary_size))
#
# optimizer = tf.train.GradientDescentOptimizer(learning_rate=1.0).minimize(loss)
#
# init = tf.initialize_all_variables()
# # the ugly
#
# num_steps = vocabulary_size*2+1
#
# init.run()
# average_loss = 0
# for step in xrange(num_steps):
#     batch_inputs, batch_labels = generate_batch(
#         batch_size, num_skips, skip_window)
#     feed_dict = {train_inputs: batch_inputs, train_labels: batch_labels}
#     _, loss_val = sess.run([optimizer, loss], feed_dict=feed_dict)
#     average_loss += loss_val
# print average_loss/num_steps


def addHaiku(theme, l1, l2, l3):
    m_theme, _ = Theme.objects.update_or_create(theme=theme)
    m_haiku = Haiku.objects.update_or_create(theme=m_theme, line1=l1, line2=l2, line3=l3)

def add_from_files():
    if not os.path.exists(settings.HAIKU_DIR):
        os.makedirs(settings.HAIKU_DIR)
    for theme in os.listdir(settings.HAIKU_DIR):
        for filename in os.listdir(os.path.join(settings.HAIKU_DIR, theme)):
            with open(os.path.join(settings.HAIKU_DIR, theme, filename)) as f:
                lines = [line for line in f.read().splitlines() if line and not line.isspace()]
                print lines
                for haiku_lists in [lines[i:i + 3] for i in range(0, len(lines), 3)]:
                    addHaiku(theme, haiku_lists[0],haiku_lists[1],haiku_lists[2])

