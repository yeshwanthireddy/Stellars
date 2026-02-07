import joblib

model = joblib.load("models/text_model.pkl")


def analyze_text(text):

    prob = model.predict_proba([text])[0][1]

    return round(float(prob), 3)
