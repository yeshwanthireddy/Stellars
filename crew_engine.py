from crewai import Agent, Task, Crew
import subprocess

from agents.text_agent import analyze_text
from agents.url_agent import analyze_url
from agents.sender_agent import analyze_sender


# -------- Local LLM via Ollama (Direct Call) --------
def call_llama(prompt):

    try:
        result = subprocess.run(
            ["ollama", "run", "llama3"],
            input=prompt,
            capture_output=True,
            text=True,
            timeout=60
        )

        return result.stdout.strip()

    except Exception as e:
        return f"Decision: UNKNOWN\nReason: LLM failed ({e})"


# -------- Manager Agent (No LLM Inside CrewAI) --------
manager = Agent(
    role="Cybersecurity Manager",
    goal="Decide phishing risk",
    backstory="Senior phishing analyst",
    verbose=False,
    allow_delegation=False
)


# -------- Main Engine --------
def run_phishguard(text, url):

    # Get agent scores
    text_score = analyze_text(text)
    url_score = analyze_url(url)
    sender_score = analyze_sender(text)

    # Build prompt
    prompt = f"""
You are a cybersecurity expert.

Message:
{text}

URL:
{url}

Scores:
Text: {text_score}
URL: {url_score}
Sender: {sender_score}

Classify as SAFE, WARNING, or PHISHING.
Give short reason.
"""

    # Call Llama3 directly
    llm_output = call_llama(prompt)

    # CrewAI task (for structure/logging only)
    task = Task(
        description=prompt,
        expected_output="Decision and reason",
        agent=manager
    )

    crew = Crew(
        agents=[manager],
        tasks=[task],
        process="sequential"
    )

    # Run CrewAI (no LLM inside)
    try:
        crew.kickoff()
    except:
        pass  # Ignore internal LLM errors


    return {
        "text": text_score,
        "url": url_score,
        "sender": sender_score,
        "result": llm_output
    }
