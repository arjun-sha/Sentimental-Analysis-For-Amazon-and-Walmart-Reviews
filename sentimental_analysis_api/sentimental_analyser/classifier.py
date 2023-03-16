from sentimental_analysis_api.sentimental_analyser.algorithms import \
    VaderClassifier


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
            score = classifier.classify(input_string)
            return score
