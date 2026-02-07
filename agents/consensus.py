def decide(text_score, url_score, sender_score):

    final = (text_score + url_score + sender_score) / 3


    if final > 0.7:
        return "PHISHING", round(final, 3)

    elif final > 0.4:
        return "WARNING", round(final, 3)

    else:
        return "SAFE", round(final, 3)
