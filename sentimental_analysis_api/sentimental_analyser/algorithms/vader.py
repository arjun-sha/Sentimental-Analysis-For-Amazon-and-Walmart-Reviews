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

    def _get_insight(self, score):
        insight = (
            "Positive"
            if score["pos"] > score["neg"]
            else "Negative"
            if score["pos"] < score["neg"]
            else "Neutral"
        )
        return {"insight": insight}

    def classify(self, input_str):
        score = SentimentIntensityAnalyzer().polarity_scores(input_str)
        pol_sub = self._get_polarity_subjectivity(input_str)
        insight = self._get_insight(score)
        score.update(dict(pol_sub, **insight))
        return score
