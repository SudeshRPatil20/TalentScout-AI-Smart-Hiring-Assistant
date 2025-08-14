# TalentScout AI – Smart Hiring Assistant

An interactive Streamlit app that screens candidates, collects basic info, and **auto-generates technical questions** based on the candidate’s tech stack using Google’s Generative AI via LangChain.

[![Watch on YouTube](https://github.com/SudeshRPatil20/TalentScout-AI-Smart-Hiring-Assistant/blob/main/images/Screenshot%20(733).png)](https://www.youtube.com/watch?v=Yz4ee15U9Sw)

> Click the thumbnail to watch the demo on YouTube.

---

## ✨ Features

- 📋 Guided candidate intake (name, email, experience, role, location)
- 🧠 LLM-powered question generation tailored to a provided tech stack
- ⚙️ Configurable model, temperature, and token limits from the sidebar
- 🔐 `.env`-based key management
- 🧩 Built with Streamlit + LangChain + Google Generative AI

---

## 🧰 Tech Stack

- **Python**, **Streamlit**
- **LangChain** (`langchain_core`, `langchain_google_genai`)
- **Google Generative AI** (`google-generativeai`)
- **python-dotenv** for environment variables

---

## 🚀 Quick Start

### 1) Clone & Install
```bash
git clone https://github.com/<your-username>/talentscout-ai.git
cd talentscout-ai
pip install -r requirements.txt


requirements.txt

streamlit
python-dotenv
google-generativeai
langchain
langchain-core
langchain-google-genai

2) Set Environment Variables

Create a .env file in the project root:

LANGCHAIN_API_KEY=your_langchain_api_key_optional
GOOGLE_API_KEY=your_google_genai_api_key


The app reads GOOGLE_API_KEY via dotenv for google.generativeai.
LANGCHAIN_API_KEY is optional and only used if you want LangSmith tracing.

3) Run the App
streamlit run app.py


Open the URL Streamlit prints (usually http://localhost:8501).

🖥️ Usage

In the sidebar, paste your Google GenAI API key (or rely on .env).

Select a model (e.g. gemini-1.5-flash-8b-latest) and adjust temperature / max tokens.

Fill in the candidate details on the main screen and click Next ➡️.

Enter the candidate’s tech stack and click Generate Questions.

Review the generated questions shown by the app.

🧩 Code Overview

app.py — Streamlit UI and chat flow (intro → tech stack → questions → conclude)

Uses a ChatPromptTemplate to ask the LLM for 3–5 technical questions:

question_prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful hiring assistant. Ask 3 to 5 technical questions based on the tech stack provided."),
    ("user", "Tech Stack: {tech_stack}")
])


LLM wrapper:

llm = ChatGoogleGenerativeAI(model=model_name)
result = (question_prompt | llm | StrOutputParser()).invoke({"tech_stack": tech_stack})

🔐 Notes on API Keys

You can set GOOGLE_API_KEY in .env or paste it into the sidebar.

Never commit your .env file—add it to .gitignore.

🧪 Troubleshooting

ModuleNotFoundError: Ensure all packages are installed from requirements.txt.

Key/Quota errors: Verify GOOGLE_API_KEY is valid and has access to the selected model.

Nothing happens on click: Check the terminal logs where Streamlit is running for exceptions.

🗺️ Roadmap

 Persist candidate responses to a database (e.g., SQLite / Postgres)

 Export questions & candidate info as PDF

 Add role-specific prompt templates and evaluation rubrics

 Multi-turn follow-ups based on candidate answers

📜 License

MIT — feel free to use and adapt.

🙌 Acknowledgements

Streamlit

LangChain

Google Generative AI
