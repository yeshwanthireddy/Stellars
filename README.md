# PhishGuard – Real-Time Phishing Detection System

PhishGuard is an intelligent cybersecurity system designed to detect phishing emails and malicious links in real time. It provides instant warnings to users before they open unsafe content through a browser extension and a desktop application.

This project was developed for the EpochOn 2.0 Hackathon under the theme of Agentic AI and Responsible Autonomy.

---

## Project Overview

Phishing attacks are one of the major causes of online fraud, identity theft, and data breaches. Attackers often use fake emails, shortened URLs, and spoofed websites to trick users into revealing sensitive information.

PhishGuard addresses this problem by using a multi-agent AI system that analyzes messages and URLs before allowing users to access them.

---

## Objectives

- Detect phishing emails and links in real time  
- Warn users before opening suspicious websites  
- Reduce online fraud and data theft  
- Provide simple and effective security tools  

---

## Key Features

- Browser extension for automatic link interception  
- Instant popup alerts with risk levels  
- Multi-agent AI-based analysis system  
- Detection of shortened and fake URLs  
- Desktop application for manual scanning  
- Risk scoring and decision mechanism  
- Fast and lightweight processing  

---

## System Architecture

PhishGuard follows a multi-agent architecture.

### Agents Used

- Text Agent: Analyzes email and message content  
- URL Agent: Evaluates domain patterns and link behavior  
- Sender Agent: Checks sender credibility  
- Consensus Agent: Combines results and makes final decision  

All agents communicate with the backend server using REST APIs.

---

## Technical Stack

### Frontend
- JavaScript  
- HTML and CSS  
- Chrome and Edge Extension API  

### Backend
- Python 3.10  
- Flask  

### AI and Machine Learning
- Scikit-learn  
- TF-IDF Vectorization  
- Logistic Regression  
- Rule-based heuristics  

### Desktop Application
- Tkinter  

### Development Tools
- Git and GitHub  
- Visual Studio Code  
- Virtual Environment  

---

## Project Structure

phishguard/
│
├── agents/
│ ├── url_agent.py
│ ├── text_agent.py
│ └── sender_agent.py
│ |___ consensus.py
|
├── background_server.py
├── train_text.py
├── prepare_text_data.py
│
├── phishguard_extension/
│ ├── manifest.json
│ ├── content.js
│ └── background.js
│
├── desktop_app.py
├── requirements.txt
└── README.md


---

## How It Works

1. User clicks on a link in an email or webpage  
2. Browser extension intercepts the click  
3. The link is sent to the backend server  
4. Multiple agents analyze the content  
5. A risk score is calculated  
6. A warning popup is displayed  
7. The user decides whether to continue  

---

## Installation and Setup

### Clone the Repository
```bash
git clone https://github.com/your-username/phishguard.git
cd phishguard

###Create Virtual Environment
python -m venv venv
venv\Scripts\activate


###Install Dependencies
pip install -r requirements.txt


###Run Backend Server
python background_server.py


###Load Browser Extension

Open Chrome or Edge

Go to chrome://extensions

Enable Developer Mode

Click Load Unpacked

Select the phishguard_extension folder


###Run Desktop Application
python desktop_app.py


###Future Enhancements

Mobile application support

Deep learning-based detection models

Cloud-based threat intelligence integration

Enterprise email security plugins

Centralized phishing database


###Team

Team Name: Stellars

Members: G. Yeshwanthi, B. Anitha, P. Siddi Sri

Institution: Amrita School of Computing

Event: EpochOn 2.0 Hackathon