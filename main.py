import streamlit as st
from ui.components import setup_page_config, render_header, render_footer
from ui.sidebar import render_sidebar
from ui.main_content import render_main_content
from core.ai_client import get_groq_client
from utils.storage import StoryStorage, init_session_state

def main():
    # Initialize application
    setup_page_config()
    init_session_state()
    
    # Initialize storage
    storage = StoryStorage()
    
    # Check API key and get client
    client = get_groq_client()
    if not client:
        st.warning("Please configure your Groq API key to start generating stories.")
        return
    
    # Render main UI
    render_header()
    
    # Get story parameters from sidebar
    story_params = render_sidebar()
    
    # Render main content area
    render_main_content(client, story_params)
    
    # Show saved stories
    storage.render_saved_stories()
    
    # Render footer
    render_footer()

if __name__ == "__main__":
    main()