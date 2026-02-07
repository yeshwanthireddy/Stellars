from agents.text_agent import analyze_text
from agents.url_agent import analyze_url
from agents.sender_agent import analyze_sender
from agents.consensus import decide


def main():

    print("===== PhishGuard =====")

    text = input("\nEnter Email / Message:\n")
    url = input("\nEnter URL (press Enter if none):\n")


    text_score = analyze_text(text)


    if url.strip() == "":
        url_score = 0
    else:
        url_score = analyze_url(url)


    sender_score = analyze_sender(text)


    result, final_score = decide(
        text_score,
        url_score,
        sender_score
    )


    print("\n----- RESULT -----")
    print("Text Risk   :", text_score)
    print("URL Risk    :", url_score)
    print("Sender Risk :", sender_score)
    print("Final Score :", final_score)
    print("Decision    :", result)


if __name__ == "__main__":
    main()
