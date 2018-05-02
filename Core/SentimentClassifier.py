#!/usr/bin/python
# -*- coding: utf-8 -*-

import pickle
from DataCleaner import cleaner
from ReviewGrabber import GetBookReviews


def SentimentAnalyzer(review):
	f = open('data/classified.pickle', 'rb')
	classifier = pickle.load(f)
	sentiment = classifier.classify(cleaner(review))
	f.close()
	return sentiment

def RatingGenerator(book_name):
	reviews = GetBookReviews(book_name)
	total_reviews = 0
	total_positives = 0
	total_negatives = 0
	for review in reviews:
		sentiment = SentimentAnalyzer(review)
		if sentiment == "positive":
			total_positives += 1
		elif sentiment == "negative":
			total_negatives +=1

	total_reviews = total_positives + total_negatives
	stars = (total_positives * 5) / total_reviews
	rating = round(stars, 2)

# RatingGenerator('Steve Jobs')
