import streamlit as st
from typing import Optional
from config.settings import AppSettings

class StoryEngine:
    def __init__(self, client):
        self.client = client
        self.settings = AppSettings()
    
    def generate_story(self, prompt: str, creativity_level: float) -> Optional[str]:
        try:
            chat_completion = self.client.chat.completions.create(
                messages=[
                    {
                        "role": "system",
                        "content": "You are a world-class storyteller known for creating deeply engaging, emotionally resonant narratives."
                    },
                    {
                        "role": "user",
                        "content": prompt
                    }
                ],
                model=self.settings.DEFAULT_MODEL,
                temperature=creativity_level,
                max_tokens=self.settings.MAX_TOKENS,
                top_p=self.settings.TOP_P,
                frequency_penalty=self.settings.FREQUENCY_PENALTY,
                presence_penalty=self.settings.PRESENCE_PENALTY,
                stream=False
            )
            
            return chat_completion.choices[0].message.content
            
        except Exception as e:
            st.error(f"Error generating story: {str(e)}")
            return None
    
    def generate_with_progress(self, prompt: str, creativity_level: float) -> Optional[str]:
        import time
        
        # Progress tracking
        progress_bar = st.progress(0)
        status_text = st.empty()
        
        status_text.text("🧠 Analyzing your concept...")
        progress_bar.progress(25)
        time.sleep(0.5)
        
        status_text.text("🎨 Crafting characters and setting...")
        progress_bar.progress(50)
        time.sleep(0.5)
        
        status_text.text("📝 Weaving your masterpiece...")
        progress_bar.progress(75)
        
        story = self.generate_story(prompt, creativity_level)
        
        progress_bar.progress(100)
        status_text.text("✨ Story complete!")
        time.sleep(0.5)
        
        # Clear progress indicators
        progress_bar.empty()
        status_text.empty()
        
        return story