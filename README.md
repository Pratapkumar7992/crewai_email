# 📧 Crewai Email Writing Pipeline

This project demonstrates how to build a **multi-agent pipeline** using [CrewAI](https://github.com/joaomdmoura/crewAI) and **Gemini (`gemini/gemini-2.0-flash`)**.  
The pipeline consists of **4 agents** that collaboratively write and refine emails.

---

## 🚀 Agents

1. **Drafter** 📝  
   Creates a rough email draft from a subject + context.  
   *(Optional: can be skipped if you provide your own rough email.)*

2. **Grammar Checker** 🔍  
   Fixes grammar, spelling, and punctuation.

3. **Politeness Enhancer** 🙏  
   Rewrites the draft to sound polite, humble, and professional.

4. **Final Reviewer** ✅  
   Reviews the polished email for clarity and completeness, and suggests improvements.

---

## 📂 Project Structure

crewai_project/
├── config/
│ ├── agents.yaml # Agent definitions
│ ├── tasks.yaml # Task definitions
├── crew.py # Orchestration logic
├── helpers.py # Loads Gemini API key
├── .env.example # Example environment file
├── requirements.txt # Dependencies
└── README.md # Documentation

create Virtual enviroment

python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows


store your api key in .env 
GEMINI_API_KEY=your_api_key_here


For start project :- python crew.py

You are put you subject and input in crew.py 
inputs = {
    "subject": "suffering from fever",
    "context": "I have a fever and cannot come to the office today. Please request sick leave."
}


Your output will me :- 

Subject: Sick Leave Request
Dear [Manager’s Name],
I hope you are doing well. I am feeling unwell with a fever and will be unable to attend the office today.  
I kindly request sick leave for this day.  
Thank you for your understanding.  
Best regards,  
[Your Name]


🛠 Tech Stack

CrewAI
 – multi-agent framework
Gemini 2.0 Flash
 – LLM model
Python 3.10+


🌟 Features
Multi-agent sequential pipeline
Verbose mode (verbose=True) shows each agent’s step
Supports both generated drafts and user-provided drafts
Clear suggestions from reviewer agent

