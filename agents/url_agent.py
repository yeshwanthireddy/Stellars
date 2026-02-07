import re
import socket
from urllib.parse import urlparse


# Common phishing keywords
SUSPICIOUS_WORDS = [
    "verify",
    "login",
    "account",
    "secure",
    "update",
    "bank",
    "confirm",
    "password",
    "reward",
    "free",
    "winner",
    "claim",
    "alert",
    "blocked",
    "security"
]

# URL shorteners
SHORTENERS = [
    "bit.ly",
    "tinyurl.com",
    "t.co",
    "goo.gl",
    "is.gd",
    "buff.ly",
    "rebrand.ly"
]


def analyze_url(url: str) -> float:
    """
    Analyze URL and return phishing risk score (0.0 to 1.0)
    """

    score = 0.0

    if not url:
        return 0.0

    url = url.strip().lower()

    parsed = urlparse(url)
    domain = parsed.netloc

    # -----------------------------
    # 1. Shortened URL check
    # -----------------------------
    for short in SHORTENERS:
        if short in domain:
            score += 0.3
            break

    # -----------------------------
    # 2. Suspicious keywords
    # -----------------------------
    for word in SUSPICIOUS_WORDS:
        if word in url:
            score += 0.07

    # -----------------------------
    # 3. IP address instead of domain
    # -----------------------------
    if re.search(r"\d+\.\d+\.\d+\.\d+", domain):
        score += 0.3

    # -----------------------------
    # 4. Excessive symbols
    # -----------------------------
    symbol_count = len(re.findall(r"[@=_\-&%$#]", url))
    if symbol_count >= 4:
        score += 0.15

    # -----------------------------
    # 5. URL length
    # -----------------------------
    if len(url) > 80:
        score += 0.1

    # -----------------------------
    # 6. DNS resolution check
    # -----------------------------
    try:
        socket.gethostbyname(domain)
    except:
        # Domain doesn't exist
        score += 0.4

    # -----------------------------
    # 7. HTTPS check
    # -----------------------------
    if not url.startswith("https"):
        score += 0.1

    # -----------------------------
    # Normalize score (0 - 1)
    # -----------------------------
    if score > 1.0:
        score = 1.0

    return round(score, 3)
