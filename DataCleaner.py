#!/usr/bin/python
# -*- coding: utf-8 -*-

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

def punctuation_filter(tokens):
    punct_removed = [word for word in tokens if word.isalpha()]
    return punct_removed

def stop_words_filter(punct_removed_words):
    stop_words = set(stopwords.words('english'))
    stop_filtered = [w for w in punct_removed_words if not w in stop_words]
    return stop_filtered

def cleaner(reviews):
	tokens = word_tokenize(reviews.lower())
	cleaned = stop_words_filter(punctuation_filter(tokens))
	clean_dict = dict([(word, True) for word in cleaned])
	return clean_dict
