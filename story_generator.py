import streamlit as st
import time
import os
from groq import Groq

# Configure page
st.set_page_config(
    page_title="AI Story Generator",
    page_icon="📚",
    layout="wide"
)

# Initialize Groq client
@st.cache_resource
def init_groq_client():
    api_key = st.secrets.get("GROQ_API_KEY") or os.getenv("GROQ_API_KEY")
    if not api_key:
        st.error("Please set your GROQ_API_KEY in Streamlit secrets or environment variables")
        st.stop()
    return Groq(api_key=api_key)

def create_story_prompt(user_prompt, theme, length, tone, pov):
    """Create optimized prompt for story generation"""
    
    # Word count mapping
    word_counts = {
        "Short": "400-600 words",
        "Medium": "800-1200 words", 
        "Long": "1500-2000 words"
    }
    
    # Theme-specific guidelines
    theme_guidelines = {
        "Fantasy": "Include magical elements, mythical creatures, or supernatural powers. Create vivid fantasy worlds with unique magic systems.",
        "Science Fiction": "Incorporate futuristic technology, space exploration, or scientific concepts. Focus on 'what if' scenarios and technological implications.",
        "Mystery/Thriller": "Build suspense and tension. Include clues, red herrings, and unexpected twists. Keep readers guessing until the reveal.",
        "Romance": "Focus on emotional connections and relationship development. Include meaningful dialogue and romantic tension.",
        "Horror": "Create atmosphere of fear and dread. Use suspense, psychological tension, and unsettling imagery.",
        "Adventure": "Include exciting journeys, challenges to overcome, and dynamic action sequences. Focus on exploration and discovery.",
        "Comedy": "Use humor, witty dialogue, and amusing situations. Include comedic misunderstandings or funny character interactions.",
        "Drama": "Focus on emotional depth, character development, and realistic human conflicts. Explore complex relationships and personal growth."
    }
    
    # Tone adjustments
    tone_adjustments = {
        "Dark": "Use a serious, somber tone with mature themes and complex moral questions.",
        "Light-hearted": "Keep the tone upbeat, optimistic, and fun. Focus on positive emotions and happy outcomes.",
        "Dramatic": "Emphasize emotional intensity, high stakes, and powerful character moments.",
        "Humorous": "Include wit, clever dialogue, and amusing situations throughout the story.",
        "Neutral": "Maintain a balanced tone appropriate to the story's natural flow."
    }
    
    # POV instructions
    pov_instruction = "first person (using 'I', 'me', 'my')" if pov == "First Person" else "third person (using 'he', 'she', 'they')"
    
    prompt = f"""You are a master storyteller. Write a compelling {theme.lower()} story based on the following requirements:

**Story Concept:** {user_prompt}

**Requirements:**
- **Genre:** {theme} - {theme_guidelines.get(theme, '')}
- **Length:** {word_counts[length]}
- **Tone:** {tone_adjustments.get(tone, 'Maintain an appropriate tone for the story.')}
- **Point of View:** Write in {pov_instruction}
- **Structure:** Include a clear beginning, middle, and end with proper story arc

**Writing Guidelines:**
1. Create engaging, well-developed characters with distinct personalities
2. Use vivid, descriptive language to paint clear scenes
3. Include meaningful dialogue that advances the plot and reveals character
4. Build appropriate pacing with tension and release
5. Show don't tell - use actions and dialogue to convey emotions and plot points
6. Create a satisfying conclusion that resolves the main conflict
7. Ensure the story flows naturally and maintains reader engagement throughout

**Style Notes:**
- Use paragraph breaks for readability
- Vary sentence length and structure for engaging prose
- Include sensory details to immerse the reader
- Maintain consistency in tone and voice throughout

Write a complete, polished story that brings this concept to life. Make it memorable and engaging for the reader."""

    return prompt

def generate_story(client, prompt):
    """Generate story using Groq API"""
    try:
        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            model="llama-3.1-70b-versatile",  # You can also use "mixtral-8x7b-32768" or other models
            temperature=0.7,  # Creative but not too random
            max_tokens=2048,  # Adjust based on desired story length
            top_p=0.9,
            stream=False
        )
        return chat_completion.choices[0].message.content
    except Exception as e:
        st.error(f"Error generating story: {str(e)}")
        return None

# App title and description
st.title("📚 AI Story Generator")
st.markdown("Generate creative stories powered by Groq AI based on your ideas and preferred themes!")

# API Key input (if not in secrets)
if not (st.secrets.get("GROQ_API_KEY") or os.getenv("GROQ_API_KEY")):
    with st.expander("🔑 API Configuration", expanded=True):
        api_key_input = st.text_input(
            "Enter your Groq API Key:",
            type="password",
            help="Get your free API key from https://console.groq.com/"
        )
        if api_key_input:
            os.environ["GROQ_API_KEY"] = api_key_input
            st.success("API Key set! You can now generate stories.")
            st.rerun()

# Only show the main app if API key is available
if st.secrets.get("GROQ_API_KEY") or os.getenv("GROQ_API_KEY"):
    client = init_groq_client()
    
    # Sidebar for controls
    with st.sidebar:
        st.header("Story Settings")
        
        # Theme selection
        theme = st.selectbox(
            "Choose a Theme/Genre:",
            [
                "Fantasy",
                "Science Fiction", 
                "Mystery/Thriller",
                "Romance",
                "Horror",
                "Adventure",
                "Comedy",
                "Drama"
            ]
        )
        
        # Story length
        length = st.select_slider(
            "Story Length:",
            options=["Short", "Medium", "Long"],
            value="Medium"
        )
        
        # Additional options
        st.subheader("Additional Options")
        
        tone = st.selectbox(
            "Story Tone:",
            ["Neutral", "Dark", "Light-hearted", "Dramatic", "Humorous"]
        )
        
        pov = st.radio(
            "Point of View:",
            ["First Person", "Third Person"]
        )
        
        # Advanced settings
        with st.expander("⚙️ Advanced Settings"):
            temperature = st.slider(
                "Creativity Level:",
                min_value=0.1,
                max_value=1.0,
                value=0.7,
                step=0.1,
                help="Higher values = more creative but less predictable"
            )

    # Main content area
    col1, col2 = st.columns([2, 1])

    with col1:
        st.header("Your Story Prompt")
        
        # Story prompt input with examples
        example_prompts = {
            "Fantasy": "A young mage discovers an ancient spellbook that writes itself",
            "Science Fiction": "Humans receive a mysterious signal from deep space containing blueprints",
            "Mystery/Thriller": "A detective finds their own fingerprints at a crime scene they've never visited",
            "Romance": "Two rival coffee shop owners are forced to work together during a city festival",
            "Horror": "A family moves into a house where the previous owners never actually left",
            "Adventure": "An archaeologist discovers a map leading to a lost civilization",
            "Comedy": "A person's autocorrect starts changing their texts to increasingly ridiculous messages",
            "Drama": "A parent and child reconnect after years apart when they're both stranded at an airport"
        }
        
        prompt = st.text_area(
            "Describe your story idea:",
            placeholder=f"Example: {example_prompts.get(theme, 'A mysterious event changes everything...')}",
            height=120,
            help="Be specific! Include characters, settings, or conflicts you want to explore."
        )
        
        # Generate button
        generate_button = st.button("🎭 Generate Story", type="primary", use_container_width=True)

    with col2:
        st.header("Story Details")
        if prompt and theme:
            st.info(f"**Theme:** {theme}")
            st.info(f"**Length:** {length}")
            st.info(f"**Tone:** {tone}")
            st.info(f"**POV:** {pov}")
            
            # Word count estimate
            word_counts = {"Short": "400-600", "Medium": "800-1200", "Long": "1500-2000"}
            st.success(f"**Est. Words:** {word_counts[length]}")

    # Story generation and display
    if generate_button:
        if not prompt:
            st.error("Please enter a story prompt!")
        else:
            # Create the optimized prompt
            story_prompt = create_story_prompt(prompt, theme, length, tone, pov)
            
            # Show loading spinner
            with st.spinner(f"🤖 Generating your {theme.lower()} story with Groq AI..."):
                generated_story = generate_story(client, story_prompt)
            
            if generated_story:
                # Display generated story
                st.header("📖 Your Generated Story")
                
                # Add some styling to the story display
                st.markdown(f"""
                <div style="
                    background-color: #f8f9fa;
                    padding: 25px;
                    border-radius: 10px;
                    border-left: 4px solid #007acc;
                    margin: 20px 0;
                    line-height: 1.6;
                    font-family: Georgia, serif;
                ">
                {generated_story.replace(chr(10), '<br><br>')}
                </div>
                """, unsafe_allow_html=True)
                
                # Story stats
                col1, col2, col3, col4 = st.columns(4)
                with col1:
                    word_count = len(generated_story.split())
                    st.metric("Word Count", word_count)
                with col2:
                    read_time = max(1, word_count // 200)  # Average reading speed
                    st.metric("Read Time", f"{read_time} min")
                with col3:
                    st.metric("Theme", theme)
                with col4:
                    st.metric("Model", "Llama-3.1-70B")
                
                # Action buttons
                st.subheader("Actions")
                col1, col2, col3, col4 = st.columns(4)
                
                with col1:
                    if st.button("📋 Copy Story"):
                        st.write("```")
                        st.write(generated_story)
                        st.write("```")
                        st.success("Story displayed in copyable format above!")
                
                with col2:
                    if st.button("🔄 Generate Another"):
                        st.rerun()
                
                with col3:
                    if st.button("🔊 Text-to-Speech"):
                        st.info("Text-to-speech feature will be added in the next version!")
                
                with col4:
                    # Save to session state for future reference
                    if "generated_stories" not in st.session_state:
                        st.session_state.generated_stories = []
                    
                    if st.button("💾 Save Story"):
                        story_data = {
                            "prompt": prompt,
                            "theme": theme,
                            "story": generated_story,
                            "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
                        }
                        st.session_state.generated_stories.append(story_data)
                        st.success("Story saved to session!")

    # Show saved stories
    if "generated_stories" in st.session_state and st.session_state.generated_stories:
        with st.expander(f"📚 Saved Stories ({len(st.session_state.generated_stories)})"):
            for i, story_data in enumerate(reversed(st.session_state.generated_stories)):
                st.markdown(f"**{story_data['theme']}** - {story_data['timestamp']}")
                st.markdown(f"*Prompt: {story_data['prompt'][:100]}...*")
                if st.button(f"View Story {len(st.session_state.generated_stories)-i}", key=f"view_{i}"):
                    st.markdown("---")
                    st.markdown(story_data['story'])

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #666;">
    <p>Built with Streamlit & Groq AI | AI Story Generator v2.0</p>
    <p><small>Powered by Llama-3.1-70B for fast, creative story generation</small></p>
</div>
""", unsafe_allow_html=True)