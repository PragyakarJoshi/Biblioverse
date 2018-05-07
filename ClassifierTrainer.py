from nltk import FreqDist
from nltk.classify import NaiveBayesClassifier
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import nltk.classify.util

import os
import pickle

from DataCleaner import cleaner

negative_reviews = []
positive_reviews = []

def data_formation(review_list, polarity):
	file_path = "data/dataset/" + polarity
	for file in os.listdir(file_path):
		f = open(file_path + "/" + file, 'r')
		file_content = f.read()
		review_list.append((cleaner(file_content),polarity))
		f.close()

print("Cleaning the data and creating dictionary of POSITIVE reviews...")
data_formation(positive_reviews, "positive")
print("Cleaning the data and creating dictionary of NEGATIVE reviews...")
data_formation(negative_reviews, "negative")
print()

training_set = positive_reviews[:1500] + negative_reviews[:1500]
testing_set = positive_reviews[-167:] + negative_reviews[-167:]

total_positive = len(positive_reviews)
total_negative = len(negative_reviews)
total_reviews = total_positive + total_negative
total_training = len(training_set)
total_testing = len(testing_set)

print("Total Number of Reviews in the Dataset: ", total_reviews)
print("Total Positive Reviews:", total_positive)
print("Total Negative Reviews:", total_negative)
print("Total Reviews in Training Dataset: ", total_training)
print("Total Reviews in Testing Dataset: ", total_testing)
print()

print("Training the Classifier with the Training Dataset...")
classifier = NaiveBayesClassifier.train(training_set)

f = open('data/classified.pickle', 'wb')
pickle.dump(classifier, f)
f.close()
print("Classifier Trained and Saved")
print()

accuracy = nltk.classify.util.accuracy(classifier, testing_set)
print("Classifier Accuracy:", (round(accuracy*100,2)))
