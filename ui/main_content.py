import streamlit as st
from ui.components import render_header, render_story_display
from core.story_engine import StoryEngine
from core.prompt_builder import PromptBuilder
from utils.analytics import StoryAnalytics
from utils.storage import StoryStorage
from data.examples import get_example_prompts
from config.settings import AppSettings

def render_main_content(client, story_params: dict):
    render_header()
    
    settings = AppSettings()
    
    # Create main columns
    col1, col2 = st.columns([3, 1])
    
    with col1:
        render_story_input_section(story_params)
    
    with col2:
        render_story_profile(story_params)
    
    # Handle story generation
    if 'generate_story' in st.session_state and st.session_state.generate_story:
        handle_story_generation(client, story_params)
        st.session_state.generate_story = False

def render_story_input_section(story_params: dict):
    st.header("✨ Your Story Vision")
    
    # Get example prompts
    example_prompts = get_example_prompts()
    
    # Story concept input
    prompt = st.text_area(
        "Describe your story concept:",
        placeholder=f"Inspiration: {example_prompts.get(story_params['theme'], 'A moment that changes everything...')}",
        height=150,
        help="The more specific and unique your concept, the more engaging your story will be."
    )
    
    # Advanced options
    with st.expander("🔧 Advanced Story Elements"):
        col_a, col_b = st.columns(2)
        
        with col_a:
            setting_era = st.selectbox("Time Period:", AppSettings.TIME_PERIODS)
            emotional_core = st.selectbox("Emotional Core:", AppSettings.EMOTIONAL_CORES, index=2)
        
        with col_b:
            story_structure = st.selectbox("Narrative Structure:", AppSettings.NARRATIVE_STRUCTURES)
            include_twist = st.checkbox("Include Plot Twist", value=True)
    
    # Generate button
    if st.button("🎭 Create Masterpiece", type="primary", use_container_width=True):
        if not prompt:
            st.error("Please provide a story concept to bring to life!")
        else:
            st.session_state.generate_story = True
            st.session_state.current_prompt = prompt
            st.session_state.advanced_options = {
                'setting_era': setting_era,
                'emotional_core': emotional_core,
                'story_structure': story_structure,
                'include_twist': include_twist
            }

def render_story_profile(story_params: dict):
    st.header("📊 Story Profile")
    
    settings = AppSettings()
    word_estimates = settings.WORD_TARGETS
    
    st.markdown(f'''
    **Genre:** {story_params['theme']}  
    **Length:** {story_params['length']} ({word_estimates[story_params['length']]})  
    **Tone:** {story_params['tone']}  
    **Perspective:** {story_params['pov']}  
    **Creativity:** {int(story_params['creativity_level'] * 100)}%  
    **Complexity:** {story_params['complexity']}  
    ''')
    
    # Estimated reading time
    avg_words = settings.WORD_ESTIMATES
    read_time = max(1, avg_words[story_params['length']] // 200)
    st.success(f"📖 Est. Reading Time: {read_time}-{read_time+1} min")

def handle_story_generation(client, story_params: dict):
    if 'current_prompt' not in st.session_state:
        return
    
    # Initialize components
    story_engine = StoryEngine(client)
    prompt_builder = PromptBuilder()
    analytics = StoryAnalytics()
    storage = StoryStorage()
    
    # Build the master prompt
    prompt_params = {
        'user_prompt': st.session_state.current_prompt,
        **story_params
    }
    
    master_prompt = prompt_builder.build_master_prompt(prompt_params)
    
    # Generate story with progress
    generated_story = story_engine.generate_with_progress(
        master_prompt, 
        story_params['creativity_level']
    )
    
    if generated_story:
        # Display the story
        render_story_display(generated_story)
        
        # Show analytics
        analytics_data = analytics.analyze_story(generated_story)
        analytics.display_analytics(analytics_data)
        
        # Story actions
        render_story_actions(generated_story, prompt_params, analytics_data, storage)

def render_story_actions(story: str, prompt_params: dict, analytics_data: dict, storage):
    st.subheader("🔧 Story Actions")
    col1, col2, col3, col4, col5 = st.columns(5)
    
    with col1:
        if st.button("📋 Copy Text"):
            st.code(story, language='text')
            st.success("Story formatted for copying!")
    
    with col2:
        if st.button("🔄 New Variation"):
            st.rerun()
    
    with col3:
        if st.button("📊 Style Analysis"):
            analytics = StoryAnalytics()
            analytics.display_style_analysis(story)
    
    with col4:
        if st.button("💾 Save Story"):
            storage.save_story(story, prompt_params, analytics_data)
            st.success("Masterpiece saved!")
    
    with col5:
        if st.button("🎨 Export"):
            storage.export_story(story, prompt_params)