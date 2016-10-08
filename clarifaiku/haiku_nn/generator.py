from __future__ import absolute_import, division, print_function

import os
#from six.moves import urllib

import tflearn
from tflearn.data_utils import *
from . import learn

# path = "shakespeare_input.txt"
# if not os.path.isfile(path):
#     urllib.request.urlretrieve("https://raw.githubusercontent.com/tflearn/tflearn.github.io/master/resources/shakespeare_input.txt", path)
#
maxlen = 100

# X, Y, char_idx = \
#     textfile_to_semi_redundant_sequences(path, seq_maxlen=maxlen, redun_step=3)
# print(X)
vocab = learn.get_vocab()
dictionary = {v: i for (i, v) in enumerate(list(vocab))}

# g = tflearn.input_data([None, maxlen, len(char_idx)])
# g = tflearn.lstm(g, 512, return_seq=True)
# g = tflearn.dropout(g, 0.5)
# g = tflearn.lstm(g, 512, return_seq=True)
# g = tflearn.dropout(g, 0.5)
# g = tflearn.lstm(g, 512)
# g = tflearn.dropout(g, 0.5)
# g = tflearn.fully_connected(g, len(char_idx), activation='softmax')
# g = tflearn.regression(g, optimizer='adam', loss='categorical_crossentropy',
#                        learning_rate=0.001)

net = tflearn.input_data(shape=[None, 1, len(vocab)])
net = tflearn.layers.recurrent.simple_rnn(net, 512, return_seq=True)
net = tflearn.dropout(net, 0.5)
net = tflearn.fully_connected(net, len(vocab), activation='softmax')
net = tflearn.regression(net, optimizer='adam', loss='categorical_crossentropy',
                       learning_rate=0.001)

m = tflearn.SequenceGenerator(net, dictionary=dictionary,
                              seq_maxlen=maxlen,
                              clip_gradients=5.0,)
def words_to_ints(words, dictionary=dictionary):
    return[dictionary[word] for word in words]

def enumerate_haiku(haiku_arr, dictionary=dictionary):
    a1, a2, a3 = (words_to_ints(haiku_arr[0]), words_to_ints(haiku_arr[1]), words_to_ints(haiku_arr[2]))
    return a1 + a2 + a3
for haiku in learn.get_words()[:5]:
    m.fit(haiku[1], enumerate_haiku(haiku[0]), validation_set=0.1, batch_size=128,
          n_epoch=1, run_id='haiku')
    print("-- TESTING...")
    print("-- Test with temperature of 1.0 --")
    # print(m.generate(600, temperature=1.0, seq_seed=seed))
    print(m.generate(600, temperature=1.0))
    # print("-- Test with temperature of 0.5 --")
    # print(m.generate(600, temperature=0.5, seq_seed=seed)