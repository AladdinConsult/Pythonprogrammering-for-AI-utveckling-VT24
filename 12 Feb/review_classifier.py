import contractions
import re
from string import punctuation
import json

def clean_text(text):
    # remove contractions
    text = contractions.fix(text)
    # make lower case
    text = text.lower()
    # remove punctuation
    text = re.sub('[%s]' % re.escape(punctuation), '', text)
    # remove numbers
    text = re.sub(r'\w*\d\w*', '', text)
    # remove stop words
    stopwords = [stopword.strip() for stopword in open('./12 Feb/data/stopwords_en.txt', 'r')]
    return ' '.join([word for word in text.split() if word not in stopwords])

class Review:
    def __init__(self, review_text, score): 
        self.review_text = review_text
        self.score = score 
        self.cleaned_review_text = clean_text(review_text)
        self.sentiment = 'NEGATIVE' if score <= 2 else 'NEAUTRAL' if score == 3 else 'POSITIVE'

reviews = []

with open('./12 Feb/data/Pet_Supplies_1000.json', 'r') as in_file:
    for line in in_file:
        data = json.loads(line)
        review_text = data['reviewText']
        overall = data['overall']
        reviews.append(Review(review_text, overall))