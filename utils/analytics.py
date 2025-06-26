import streamlit as st
from typing import Dict, Any

class StoryAnalytics:
    def analyze_story(self, story: str) -> Dict[str, Any]:
        word_count = len(story.split())
        sentence_count = story.count('.') + story.count('!') + story.count('?')
        paragraph_count = story.count('\n\n') + 1
        avg_sentence_length = word_count / max(sentence_count, 1)
        dialogue_count = story.count('"') // 2
        
        return {
            'word_count': word_count,
            'sentence_count': sentence_count,
            'paragraph_count': paragraph_count,
            'avg_sentence_length': avg_sentence_length,
            'dialogue_count': dialogue_count,
            'read_time': max(1, word_count // 200)
        }
    
    def display_analytics(self, analytics_data: Dict[str, Any]):
        st.subheader("📊 Story Analytics")
        col1, col2, col3, col4, col5 = st.columns(5)
        
        with col1:
            st.metric("Words", analytics_data['word_count'])
        with col2:
            st.metric("Sentences", analytics_data['sentence_count'])
        with col3:
            st.metric("Avg Sentence", f"{analytics_data['avg_sentence_length']:.1f}")
        with col4:
            st.metric("Read Time", f"{analytics_data['read_time']} min")
        with col5:
            st.metric("Dialogue", f"{analytics_data['dialogue_count']} exchanges")
    
    def display_style_analysis(self, story: str):
        action_indicators = (
            story.lower().count(' ran ') + 
            story.lower().count(' walked ') + 
            story.lower().count(' moved ')
        )
        
        dialogue_count = story.count('"')
        
        st.info(f'''
        **Style Analysis:**
        - Dialogue: {dialogue_count // 2} exchanges  
        - Action Level: {'High' if action_indicators > 5 else 'Medium' if action_indicators > 2 else 'Low'}
        - Pacing: {'Fast' if len(story.split()) / story.count('.') < 15 else 'Moderate'}
        ''')
    
    def get_reading_difficulty(self, story: str) -> str:
        words = story.split()
        sentences = story.count('.') + story.count('!') + story.count('?')
        avg_word_length = sum(len(word) for word in words) / len(words)
        avg_sentence_length = len(words) / max(sentences, 1)
        
        if avg_word_length > 5 and avg_sentence_length > 20:
            return "Advanced"
        elif avg_word_length > 4 and avg_sentence_length > 15:
            return "Intermediate"
        else:
            return "Easy"