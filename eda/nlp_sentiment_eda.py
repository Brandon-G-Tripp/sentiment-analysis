import nltk
nltk.download('imdb')

from nltk.corpus import imdb
train_reviews = imdb.train()
test_review = imdb.test()
