import numpy
import random
import Queue



def hasNumbers(inputString):
    return any(char.isdigit() for char in inputString)

import os
def get_syllable_dict():
    sylDict = {}
    with open('haiku_nn/data_files/sylDict.txt', 'r') as f:
        for line in f:
            ls = str.split(line)
            key = ls[0].lower()
            if not hasNumbers(key):
                value = 0
                for i in range(1, len(ls)):
                    if hasNumbers(ls[i]):
                        value += 1

                sylDict[key] = value
    return sylDict

syl_dict = get_syllable_dict()

words2vectors = {}
with open('haiku_nn/data_files/glove.6B.50d.txt') as f:
    for line in f:
        l = line.split()
        words2vectors[l[0]] = numpy.array(l[1:], dtype=numpy.float32)

def get_neighbor_queue(word):
    center_point = words2vectors[word]
    queue = Queue.PriorityQueue()
    for w, v in words2vectors.iteritems():
        queue.put((numpy.linalg.norm(center_point - v), w))
    return queue

def n_nearest_same_syllable(word, n=10, timeout_steps=100):
    queue = get_neighbor_queue(word)
    w = queue.get()[1].lower()
    replacements = []
    if w in syl_dict:
        _ , syll = syl_dict[queue.get()[1].lower()]
        i = 0
        for x in range(timeout_steps):
            if i >= n:
                break
            d, w = queue.get()
            print w
            if w.lower() in syl_dict and syl_dict[w.lower()] == syll:
                replacements.append(w)
                i += 1
    return replacements


def generate_similar_haiku(haiku):
    lines = [haiku.line1, haiku.line2, haiku.line3]
    for line in lines:
        for word in l:
            lines[line][word] = random.choice(n_nearest_same_syllable(word))
    return lines


