from textblob import TextBlob
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer


class VaderClassifier:
    def __init__(self) -> None:
        pass

    def _get_polarity_subjectivity(self, input_str):
        blob = TextBlob(input_str).sentiment
        polarity = blob.polarity
        subjectivity = blob.subjectivity
        return {"polarity": polarity, "subjectivity": subjectivity}

    def classify(self, input_str):
        score = SentimentIntensityAnalyzer().polarity_scores(input_str)
        pol_sub = self._get_polarity_subjectivity(input_str)
        score.update(pol_sub)
        return score
