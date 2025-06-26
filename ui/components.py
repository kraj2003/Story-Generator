import streamlit as st
from config.settings import AppSettings

def setup_page_config():
    settings = AppSettings()
    st.set_page_config(
        page_title=settings.PAGE_TITLE,
        page_icon=settings.PAGE_ICON,
        layout=settings.LAYOUT
    )

def render_header():
    st.title("📚 AI Story Generator Pro")
    st.markdown("*Create exceptional stories with advanced AI prompting techniques*")

def render_story_display(story: str):
    st.header("📖 Your Masterpiece")
    
    st.markdown(f'''
    <div style="
        background: linear-gradient(135deg, #f8f9fa 0%, #e9ecef 100%);
        padding: 30px;
        border-radius: 15px;
        border-left: 5px solid #007acc;
        margin: 20px 0;
        line-height: 1.8;
        font-family: 'Georgia', serif;
        font-size: 16px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    ">
    {story.replace(chr(10), '<br><br>')}
    </div>
    ''', unsafe_allow_html=True)

def render_footer():
    st.markdown("---")
    st.markdown('''
    <div style="text-align: center; color: #666; padding: 20px;">
        <h4>🎭 AI Story Generator Pro</h4>
        <p>Powered by Advanced Prompting Techniques & Groq AI</p>
        <p><small>Creating masterpieces with Llama-3.1-70B • Built with expertise and creativity</small></p>
    </div>
    ''', unsafe_allow_html=True)