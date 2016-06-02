# -*- coding: utf-8 -*-
"""
Created on Mon Dec 14 12:52:36 2015

@author: Paul Cheng

Ebbinghaus task: list generation
"""
import csv
import config
from random import shuffle

##List generation
def pool_maker(cond, config):
    # Generate a Pool either from Normal CVC words or Nonsense CVC words
    if cond:
        pd = open(config.cvcspool)
        words = [str(s[:3]) for s in pd]
        # print words

    else:
        pd = open(config.wordspool)
        words = [str(s[:3]) for s in pd]

    shuffle(words)

    return words


def lis_maker(words, num_word):
    # From Pool Pull out words to Make a List of Words
    word_list = []
    # Print num_word
    for n in range(num_word):
        word=words.pop(n)
        word_list.append(word)
    return word_list

def dic_maker(num_word, cond, conds, blocknum=0):
    # Generate dictionary and create blocks
    blocks = []
    word_pool = pool_maker(cond, config)

    for b in range(blocknum):
        block_num = b+1
        print 'Creating block %d' % block_num

        # Create an empty list of trials
        block = {'block_num':block_num,
               'list_words': lis_maker(word_pool, num_word),
               'number_words':num_word,
               'condition': []}
        if cond == True:
            block['condition'] = conds[0]
        else:
            block['condition'] = conds[1]

        blocks.append(block)

    return blocks

def block_maker(cond, config):
    # Simplify the out-put of the function
    blocks = dic_maker(config.num_word_list,
                       cond,
                       config.conditions,
                       config.num_block)
    # Print blocks
    return blocks

def mad_man_shuffler(word_list):
    shuffle(word_list)
    # Print word_list
    return word_list

