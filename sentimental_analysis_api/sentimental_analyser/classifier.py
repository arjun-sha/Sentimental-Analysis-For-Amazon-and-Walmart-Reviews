from sentimental_analysis_api.sentimental_analyser.algorithms import (NaiveBayesClassifier,
                                                                      VaderClassifier)
from sentimental_analysis_api.exceptions import ClassificationException


class Classifier:
    def __init__(self) -> None:
        pass

    @classmethod
    def classify(
        cls,
        input_string: str = None,
        file_name: str = None,
        batch: bool = False,
        algorithm: str = "vader",
        sarcasm: bool = False,
        emoji: bool = False,
        lang: str = "en",
    ):
        if algorithm == "vader":
            classifier = VaderClassifier()
        if algorithm == "naive_bayes":
            classifier = NaiveBayesClassifier()

        score = classifier.classify(input_string)
        return score
