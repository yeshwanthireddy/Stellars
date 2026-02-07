import re
import whois
import datetime


def extract_domain(text):

    match = re.search(r"@([\w.-]+)", text)

    if match:
        return match.group(1)

    return None


def analyze_sender(text):

    domain = extract_domain(text)

    if not domain:
        return 0.4


    try:
        info = whois.whois(domain)

        date = info.creation_date

        if isinstance(date, list):
            date = date[0]

        if not date:
            return 0.6

        age = (datetime.datetime.now() - date).days

        score = 0

        if age < 180:
            score += 0.4

        elif age < 365:
            score += 0.2

        return min(score, 1.0)

    except:
        return 0.5
