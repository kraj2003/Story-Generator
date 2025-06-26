import streamlit as st
import os
from groq import Groq
from config.settings import get_api_key

@st.cache_resource
def init_groq_client():
    api_key = get_api_key()
    if not api_key:
        return None
    return Groq(api_key=api_key)

def get_groq_client():
    client = init_groq_client()
    if not client:
        handle_missing_api_key()
        return None
    return client

def handle_missing_api_key():
    with st.expander("🔑 API Configuration", expanded=True):
        api_key_input = st.text_input(
            "Enter your Groq API Key:",
            type="password",
            help="Get your free API key from https://console.groq.com/"
        )
        
        if api_key_input:
            os.environ["GROQ_API_KEY"] = api_key_input
            st.success("API Key set! Advanced story generation is now available.")
            st.rerun()