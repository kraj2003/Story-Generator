import os
from typing import Dict, Any
import streamlit as st

class AppSettings:
    # Page Configuration
    PAGE_TITLE = "AI Story Generator Pro"
    PAGE_ICON = "📚" 
    LAYOUT = "wide"
    
    # AI Model Settings
    DEFAULT_MODEL = "gemma2-9b-it"
    MAX_TOKENS = 3000
    TOP_P = 0.95
    FREQUENCY_PENALTY = 0.1
    PRESENCE_PENALTY = 0.1
    
    # Story Settings
    WORD_TARGETS = {
        "Short": "600-800 words",
        "Medium": "1200-1500 words", 
        "Long": "2000-2500 words"
    }
    
    WORD_ESTIMATES = {
        "Short": 700,
        "Medium": 1350,
        "Long": 2250
    }
    
    # UI Settings
    GENRES = [
        "Fantasy", "Science Fiction", "Mystery/Thriller",
        "Romance", "Horror", "Adventure", "Comedy", "Drama"
    ]
    
    TONES = ["Neutral", "Dark", "Light-hearted", "Dramatic", "Humorous"]
    
    POV_OPTIONS = ["First Person", "Third Person"]
    
    COMPLEXITY_LEVELS = ["Straightforward", "Layered", "Complex"]
    
    TIME_PERIODS = ["Contemporary", "Historical", "Future", "Timeless"]
    
    EMOTIONAL_CORES = [
        "Love", "Loss", "Discovery", "Redemption", 
        "Survival", "Growth", "Justice", "Freedom"
    ]
    
    NARRATIVE_STRUCTURES = [
        "Linear", "Flashbacks", "Multiple Timeline", "Circular"
    ]

def get_api_key() -> str:
    return st.secrets.get("GROQ_API_KEY") or os.getenv("GROQ_API_KEY")