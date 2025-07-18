import os
import streamlit as st
from dotenv import load_dotenv
import google.generativeai as genai
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

# Load API key from environment
load_dotenv()
os.environ['LANGCHAIN_API_KEY'] = "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"
os.environ['LANGCHAIN_TRACING_V2'] = "true"
os.environ['LANGCHAIN_PROJECT'] = "Hiring Assistant Chatbot"

# Initialize session state
if "stage" not in st.session_state:
    st.session_state.stage = "intro"
    st.session_state.candidate_info = {}

# Initialize prompt templates
question_prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful hiring assistant. Ask 3 to 5 technical questions based on the tech stack provided."),
    ("user", "Tech Stack: {tech_stack}")
])

# Define LLM
def generate_questions(tech_stack, model_name, api_key):
    genai.configure(api_key=api_key)
    llm = ChatGoogleGenerativeAI(model=model_name)
    output_parser = StrOutputParser()
    chain = question_prompt | llm | output_parser
    result = chain.invoke({"tech_stack": tech_stack})
    return result

# Streamlit UI
st.title("💼 TalentScout Hiring Assistant")

st.sidebar.title("Configuration")
api_key = st.sidebar.text_input("Enter your GenAI API key", type="password")
llm_model = st.sidebar.selectbox("Select LLM", ["gemini-1.5-flash-8b-latest", "gemma-7b", "flan-t5-xl"])
temperature = st.sidebar.slider("Temperature", 0.0, 1.0, 0.7)
max_tokens = st.sidebar.slider("Max Tokens", 50, 300, 150)

def reset():
    st.session_state.stage = "intro"
    st.session_state.candidate_info = {}

st.sidebar.button("🔄 Reset Chat", on_click=reset)

# Chat Flow
if st.session_state.stage == "intro":
    st.write("👋 Hello! I'm TalentScout AI, here to assist with your job application.")
    st.write("Let's get started. Please fill in the following:")
    name = st.text_input("Full Name")
    email = st.text_input("Email Address")
    phone = st.text_input("Phone Number")
    experience = st.text_input("Years of Experience")
    position = st.text_input("Desired Position")
    location = st.text_input("Current Location")

    if st.button("Next ➡️"):
        if name and email and phone and experience and position:
            st.session_state.candidate_info.update({
                "name": name, "email": email, "phone": phone,
                "experience": experience, "position": position, "location": location
            })
            st.session_state.stage = "tech_stack"
        else:
            st.warning("Please fill in all required fields.")

elif st.session_state.stage == "tech_stack":
    st.write(f"Thanks, {st.session_state.candidate_info['name']}! Now tell me about your technical skills.")
    tech_stack = st.text_area("List your tech stack (e.g., Python, Django, MySQL, Docker)")

    if st.button("Generate Questions"):
        if tech_stack:
            st.session_state.candidate_info["tech_stack"] = tech_stack
            with st.spinner("Generating technical questions..."):
                questions = generate_questions(tech_stack, llm_model, api_key)
                st.session_state.generated_questions = questions
                st.session_state.stage = "questions"
        else:
            st.warning("Please enter your tech stack.")

elif st.session_state.stage == "questions":
    st.success("Here are your technical questions:")
    st.write(st.session_state.generated_questions)
    st.session_state.stage = "conclude"

elif st.session_state.stage == "conclude":
    st.write("✅ Thank you for completing the initial screening!")
    st.write("Our team will review your answers and contact you at the provided email/phone.")
    st.write("Good luck with your application! 🚀")

# import google.generativeai as genai


# genai.configure(api_key="********************************************8")

# models = genai.list_models()

# for model in models:
#     print(f"Model name: {model.name}")
#     print(f"Supported methods: {model.supported_generation_methods}")
#     print("="*40)
