import re

import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer


class Preprocess:
    def __init__(self) -> None:
        pass

    @classmethod
    def naive_bayes_preprocess(cls, data, batch=False):
        nltk.download("stopwords")
        ps = PorterStemmer()

        all_stopwords = stopwords.words("english")
        all_stopwords.remove("not")

        review = re.sub("[^a-zA-Z]", " ", data)
        review = review.lower()
        review = review.split()
        review = [ps.stem(word) for word in review if word not in set(all_stopwords)]
        review = " ".join(review)
        review = list(review)
        return review
