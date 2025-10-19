import streamlit as st
import io
import os 
from langchain_groq import ChatGroq  # Groq requires a free API key from groq.com
from dotenv import load_dotenv

load_dotenv()

st.set_page_config(page_title="AI Resume Critiquer", page_icon="📃",layout="centered")

st.title("📃 AI Resume Critiquer")
st.markdown("Welcome to the AI Resume Critiquer! Upload your resume, and I'll provide feedback to help you improve it.")
