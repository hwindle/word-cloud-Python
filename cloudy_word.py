#!/usr/bin/env python3

import wordcloud
import numpy as np
from matplotlib import pyplot as plt
from IPython.display import display
import io
import sys

file_contents = ''
with open('ch48_pride_and_predujudice.txt', encoding='utf8') as f:
    for line in f:
        file_contents += line.strip('\n')

def calculate_frequencies(file_contents):
    # Here is a list of punctuations and uninteresting words you can use to process your text
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~“”'''
    uninteresting_words = ["the", "a", "to", "if", "is", "it", "of", "and", "or", "an", "as", "i", "me", "my", \
    "we", "our", "ours", "you", "your", "yours", "he", "she", "him", "his", "her", "hers", "its", "they", "them", \
    "their", "what", "which", "who", "whom", "this", "that", "am", "are", "was", "were", "be", "been", "being", \
    "have", "has", "had", "do", "does", "did", "but", "at", "by", "with", "from", "here", "when", "where", "how", \
    "all", "any", "both", "each", "few", "more", "some", "such", "no", "nor", "too", "very", "can", "will", "just", "one", "in"]

    # getting rid of punctuations.
    for char in file_contents:
        if char in punctuations:
            file_contents = file_contents.replace(char, '')

    words = file_contents.split()
    interesting_words = []
    for word in words:
        if word.istitle():
            pass
        elif word.lower() in uninteresting_words:
            pass
        else:
            interesting_words.append(word)

    # using a dictionary to count each word
    frequencies = {}
    for item in interesting_words:
        # a word that is 1st appearing in dictionary
        if item not in frequencies.keys():
            frequencies[item] = 1
        else:
            # an existing key being incremented
            frequencies[item] += 1

    #wordcloud
    cloud = wordcloud.WordCloud()
    cloud.generate_from_frequencies(frequencies)
    return cloud.to_array()


myimage = calculate_frequencies(file_contents)
plt.imshow(myimage, interpolation = 'nearest')
plt.axis('off')
plt.show()
