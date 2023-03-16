import os
import pickle

import joblib

from sentimental_analysis_api.sentimental_analyser.preprocessing import Preprocess


class NaiveBayesClassifier:
    def __init__(self) -> None:
        self.model = self.load_model()
        self.bag_of_words = self.load_words()

    @staticmethod
    def load_model():
        path_model = os.path.join(
            os.path.dirname(__file__), "models/naive_bayes_model_v1_0_1"
        )
        model = joblib.load(path_model)
        return model

    @staticmethod
    def load_words():
        path_bagofwords = os.path.join(
            os.path.dirname(__file__), "models/bag_of_words_naive_bayes.pkl"
        )
        cv = pickle.load(open(path_bagofwords, "rb"))
        return cv

    def classify(self, input_str):

        data = Preprocess.naive_bayes_preprocess(input_str)
        X_data = self.bag_of_words.transform(data).toarray()
        y_pred = self.model.predict(X_data)
        insight = "Positive" if y_pred[0] == 1 else "Negative"

        return {"result": int(y_pred[0]), "insight": insight}
