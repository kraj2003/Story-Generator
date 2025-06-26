import streamlit as st
import re
from typing import List, Dict, Any

class TextUtils:
    @staticmethod
    def clean_text(text: str) -> str:
        # Remove extra whitespace and normalize line breaks
        text = re.sub(r'\s+', ' ', text.strip())
        text = re.sub(r'\n\s*\n', '\n\n', text)
        return text
    
    @staticmethod
    def extract_keywords(text: str, num_keywords: int = 10) -> List[str]:
        # Simple keyword extraction
        words = re.findall(r'\b[a-zA-Z]{4,}\b', text.lower())
        # Remove common words
        common_words = {'that', 'with', 'have', 'this', 'will', 'they', 'from', 'been', 'said', 'each', 'which', 'their', 'time', 'would', 'there', 'could', 'other'}
        keywords = [word for word in words if word not in common_words]
        
        # Count frequency
        word_freq = {}
        for word in keywords:
            word_freq[word] = word_freq.get(word, 0) + 1
        
        # Return top keywords
        return sorted(word_freq.keys(), key=lambda x: word_freq[x], reverse=True)[:num_keywords]
    
    @staticmethod
    def estimate_reading_time(text: str, wpm: int = 200) -> int:
        word_count = len(text.split())
        return max(1, word_count // wpm)
    
    @staticmethod
    def get_text_statistics(text: str) -> Dict[str, Any]:
        words = text.split()
        sentences = text.count('.') + text.count('!') + text.count('?')
        paragraphs = text.count('\n\n') + 1
        
        return {
            'word_count': len(words),
            'sentence_count': sentences,
            'paragraph_count': paragraphs,
            'avg_words_per_sentence': len(words) / max(sentences, 1),
            'avg_sentences_per_paragraph': sentences / max(paragraphs, 1)
        }

class UIHelpers:
    @staticmethod
    def create_progress_tracker(steps: List[str]) -> None:
        """Create a visual progress tracker"""
        progress_container = st.container()
        with progress_container:
            cols = st.columns(len(steps))
            for i, (col, step) in enumerate(zip(cols, steps)):
                with col:
                    st.markdown(f"**{i+1}.** {step}")
    
    @staticmethod
    def show_success_animation():
        """Show a success animation"""
        st.balloons()
        st.success("🎉 Masterpiece Created!")
    
    @staticmethod
    def format_story_for_display(story: str) -> str:
        """Format story text for better display"""
        # Add proper paragraph spacing
        story = story.replace('\n', '\n\n')
        # Ensure dialogue is properly formatted
        story = re.sub(r'(".*?")', r'<em>\1</em>', story)
        return story

class ValidationHelpers:
    @staticmethod
    def validate_story_prompt(prompt: str) -> tuple[bool, str]:
        """Validate user story prompt"""
        if not prompt or len(prompt.strip()) < 10:
            return False, "Please provide a more detailed story concept (at least 10 characters)."
        
        if len(prompt) > 1000:
            return False, "Story concept is too long. Please keep it under 1000 characters."
        
        # Check for inappropriate content (basic check)
        inappropriate_words = ['violence', 'explicit', 'harmful']  # Extend as needed
        if any(word in prompt.lower() for word in inappropriate_words):
            return False, "Please ensure your story concept is appropriate for all audiences."
        
        return True, "Valid prompt"
    
    @staticmethod
    def validate_story_parameters(params: Dict[str, Any]) -> tuple[bool, str]:
        """Validate story generation parameters"""
        required_params = ['theme', 'length', 'tone', 'pov', 'creativity_level']
        
        for param in required_params:
            if param not in params:
                return False, f"Missing required parameter: {param}"
        
        if not 0.1 <= params['creativity_level'] <= 1.0:
            return False, "Creativity level must be between 0.1 and 1.0"
        
        return True, "Valid parameters"