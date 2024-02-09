import sys 

sys.path.append('~/anaconda3/envs/nlp-sent/lib/python3.12/site-packages/')
import nltk
from nltk.corpus import imdb

nltk.download('imdb')

train_reviews = imdb.train()
test_review = imdb.test()
