import streamlit as st
from config.settings import AppSettings
from data.examples import get_example_prompts

def render_sidebar() -> dict:
    settings = AppSettings()
    
    with st.sidebar:
        st.header("🎭 Story Mastery Controls")
        
        # Genre selection
        theme = st.selectbox(
            "Genre Expertise:",
            settings.GENRES
        )
        
        # Length control
        length = st.select_slider(
            "Story Depth:",
            options=["Short", "Medium", "Long"],
            value="Medium",
            help="Short: Focused impact, Medium: Rich development, Long: Epic depth"
        )
        
        st.subheader("🎨 Artistic Direction")
        
        # Tone selection
        tone = st.selectbox(
            "Emotional Tone:",
            settings.TONES,
            help="Sets the emotional atmosphere and word choice"
        )
        
        # POV selection
        pov = st.radio(
            "Narrative Perspective:",
            settings.POV_OPTIONS,
            help="First Person: Intimate, personal. Third Person: Versatile, cinematic"
        )
        
        st.subheader("⚡ AI Parameters")
        
        # Creativity slider
        creativity_level = st.slider(
            "Creative Risk Level:",
            min_value=0.1,
            max_value=1.0,
            value=0.7,
            step=0.1,
            help="Low: Reliable, coherent. Medium: Balanced creativity. High: Bold, experimental"
        )
        
        # Story complexity
        complexity = st.selectbox(
            "Narrative Complexity:",
            settings.COMPLEXITY_LEVELS,
            index=1,
            help="Controls plot intricacy and character development depth"
        )
        
        return {
            'theme': theme,
            'length': length,
            'tone': tone,
            'pov': pov,
            'creativity_level': creativity_level,
            'complexity': complexity
        }