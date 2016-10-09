import numpy
import random
import Queue


def hasNumbers(inputString):
    return any(char.isdigit() for char in inputString)


def get_syllable_dict():
    sylDict = {}
    with open('sylDict.txt', 'r') as f:
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


# print sylDict
words2vectors = {}
syl_dict = get_syllable_dict()

with open('glove.6B.50d.txt') as f:
    for line in f:
        l = line.split()
        words2vectors[l[0]] = numpy.array(l[1:], dtype=numpy.float32)

word = 'sky'
center_point = words2vectors[word]

queue = Queue.PriorityQueue()
for w, v in words2vectors.iteritems():
    queue.put((numpy.linalg.norm(center_point - v), w))

i = 0
syll = syl_dict[word.lower()]
i = 0
for x in range(100):
    if i >= 10:
        break
    d, w = queue.get()
    if syl_dict[w] == syll:
        print w
        i += 1
