# =============================================================================
# AI Story Generator with Advanced Prompting Expertise
# =============================================================================
# This Streamlit application generates exceptionally creative and realistic stories 
# using advanced prompting techniques and Groq's AI models
# Features: Expert-level prompts, advanced genre mechanics, character depth, and more
# =============================================================================

import streamlit as st
import time
import os
import random
from groq import Groq

# =============================================================================
# PAGE CONFIGURATION
# =============================================================================
st.set_page_config(
    page_title="AI Story Generator Pro",
    page_icon="📚",
    layout="wide"
)

# =============================================================================
# GROQ CLIENT INITIALIZATION
# =============================================================================
@st.cache_resource
def init_groq_client():
    """Initialize and cache the Groq client for API calls"""
    api_key = st.secrets.get("GROQ_API_KEY") or os.getenv("GROQ_API_KEY")
    
    if not api_key:
        st.error("Please set your GROQ_API_KEY in Streamlit secrets or environment variables")
        st.stop()
    
    return Groq(api_key=api_key)

# =============================================================================
# ADVANCED PROMPTING SYSTEM
# =============================================================================

def get_sensory_details_prompt(theme):
    """Generate sensory detail instructions based on theme"""
    sensory_mapping = {
        "Fantasy": "ancient stone corridors echoing with whispers, the metallic taste of magic in the air, glowing runes that pulse with warmth, the musty scent of old grimoires, silk robes rustling against skin",
        "Science Fiction": "the sterile hum of life support systems, cold metal surfaces under fingertips, the acrid smell of ozone after energy discharge, holographic displays casting blue light on faces, synthetic air recycling through vents",
        "Mystery/Thriller": "creaking floorboards in empty houses, the weight of eyes watching from shadows, coffee growing cold in forgotten cups, rain pattering against windows, the sharp scent of fear-induced adrenaline",
        "Romance": "the warmth of intertwined fingers, soft candlelight dancing across skin, the lingering scent of perfume on clothes, whispered words that make hearts race, silk sheets cool against bare skin",
        "Horror": "the suffocating silence before something terrible happens, cold sweat beading on trembling skin, the metallic taste of fear, shadows that seem to move in peripheral vision, the smell of decay and forgotten time",
        "Adventure": "wind whipping through hair on mountain peaks, the burn of muscles pushed to their limit, exotic spices filling marketplace air, leather worn smooth by countless journeys, the sound of waves against wooden hulls",
        "Comedy": "the uncontrollable giggle that starts in the belly, coffee spilling in perfectly timed disasters, the ridiculous squeak of rubber shoes on polished floors, the warm feeling of shared laughter, absurd coincidences that defy logic",
        "Drama": "tears that blur vision and salt the lips, the hollow ache of words left unsaid, trembling hands reaching for connection, the weight of silence in hospital waiting rooms, rain that mirrors inner storms"
    }
    return sensory_mapping.get(theme, "rich sensory details that immerse the reader completely")

def get_character_depth_prompt(pov, theme):
    """Generate character development instructions"""
    if pov == "First Person":
        return f"""Develop the narrator as a complex, flawed, relatable human being with:
        - Internal contradictions and realistic psychology
        - A distinct voice with unique speech patterns, thoughts, and reactions
        - Specific background details that influence their worldview
        - Emotional vulnerabilities that make them three-dimensional
        - Skills, knowledge, or quirks relevant to the {theme.lower()} genre
        - A clear character arc that shows growth or change through the story"""
    else:
        return f"""Create multi-dimensional characters with:
        - Each character having distinct dialogue patterns, mannerisms, and motivations
        - Hidden depths revealed through actions rather than exposition
        - Relationships that feel authentic and complex
        - Backstories that inform but don't overwhelm the present action
        - Character flaws that create realistic conflict and growth opportunities
        - Specific expertise or knowledge that serves the {theme.lower()} plot naturally"""

def get_genre_mastery_prompt(theme):
    """Advanced genre-specific storytelling techniques"""
    genre_expertise = {
        "Fantasy": """Master these fantasy elements:
        - Create magic systems with clear rules, limitations, and costs
        - Build cultures with unique customs, languages, and belief systems
        - Design creatures that feel both wondrous and believable
        - Weave mythology naturally into the plot without info-dumping
        - Balance familiar fantasy tropes with fresh, unexpected twists
        - Show the impact of magic on society, economy, and daily life
        - Use archaic or formal language sparingly for atmosphere without alienating readers""",
        
        "Science Fiction": """Execute advanced sci-fi techniques:
        - Ground futuristic technology in believable scientific principles
        - Explore the social and ethical implications of technological advancement
        - Create future societies that feel like natural progressions of current trends
        - Use scientific concepts to drive plot rather than just provide backdrop
        - Balance technical details with human storytelling
        - Address how technology changes human relationships and identity
        - Incorporate current scientific discoveries and theories authentically""",
        
        "Mystery/Thriller": """Deploy expert mystery mechanics:
        - Plant clues that are fair but not obvious, rewarding careful readers
        - Create red herrings that feel natural, not forced
        - Build escalating tension through pacing, stakes, and revelation timing
        - Develop a logical solution that's surprising yet inevitable
        - Use misdirection through character assumptions and biases
        - Create multiple layers of mystery that interconnect meaningfully
        - Balance action with investigation and character development""",
        
        "Romance": """Craft compelling romantic tension:
        - Build emotional intimacy through vulnerability and shared experiences
        - Create obstacles that arise from character flaws, not external manipulation
        - Show attraction through subtle gestures, meaningful looks, and chemistry
        - Develop relationship progression that feels authentic and earned
        - Balance romantic scenes with individual character growth
        - Use dialogue that reveals personality while building romantic tension
        - Create moments of genuine connection that transcend physical attraction""",
        
        "Horror": """Master psychological and atmospheric horror:
        - Build dread through what's not shown rather than graphic descriptions
        - Use familiar settings made sinister through subtle wrongness
        - Create horror that taps into universal fears and anxieties
        - Escalate tension through pacing, building to carefully timed releases
        - Develop threats that represent deeper psychological or social fears
        - Use sensory details to create unsettling atmosphere
        - Balance supernatural elements with psychological realism""",
        
        "Adventure": """Create thrilling adventure elements:
        - Design obstacles that require ingenuity, not just action
        - Build exotic locations that feel authentic and immersive
        - Create stakes that matter personally to the characters
        - Balance action sequences with character moments and plot development
        - Use geography and environment as active elements in the story
        - Design challenges that showcase character strengths and growth
        - Maintain momentum while allowing for emotional and plot development""",
        
        "Comedy": """Execute sophisticated humor techniques:
        - Use character-based humor that arises from personality and situation
        - Create comedy through misunderstandings, timing, and escalation
        - Balance different types of humor: wit, situational, character-based, observational
        - Use callbacks and running gags that build throughout the story
        - Create absurd situations grounded in recognizable human behavior
        - Time comedic beats for maximum impact, using rhythm and pacing
        - Include heart beneath the humor for emotional resonance""",
        
        "Drama": """Craft emotionally powerful drama:
        - Focus on internal conflicts that mirror external situations
        - Create realistic dialogue that reveals character while advancing plot
        - Build emotional stakes through relationships and personal growth
        - Use subtext and what characters don't say as powerfully as what they do
        - Explore universal themes through specific, personal stories
        - Balance hope and struggle for authentic emotional journeys
        - Create moments of quiet revelation alongside dramatic confrontations"""
    }
    
    return genre_expertise.get(theme, "Apply expert storytelling techniques for maximum emotional impact")

def get_prose_excellence_prompt(tone, length):
    """Advanced prose and style instructions"""
    word_targets = {
        "Short": "600-800 words",
        "Medium": "1200-1500 words", 
        "Long": "2000-2500 words"
    }
    
    tone_styles = {
        "Dark": "Use precise, evocative language with underlying tension. Employ shorter sentences during intense moments, longer flowing sentences for reflection. Choose words that carry emotional weight.",
        "Light-hearted": "Write with buoyant rhythm and playful language. Use varied sentence structures that feel musical. Include precise details that spark joy or amusement.",
        "Dramatic": "Employ powerful, emotional language with strong imagery. Use sentence rhythm to match emotional intensity. Choose words that resonate with deeper meaning.",
        "Humorous": "Craft sentences with comedic timing. Use unexpected word choices and juxtaposition. Vary rhythm for comedic effect - quick builds, perfect pauses.",
        "Neutral": "Use clear, engaging prose that serves the story. Vary sentence length naturally. Choose precise words that create vivid imagery without calling attention to themselves."
    }
    
    return f"""Create exceptional prose with these techniques:
    
    TARGET LENGTH: {word_targets[length]} - This is your sweet spot for maximum impact
    
    STYLE MASTERY: {tone_styles.get(tone, 'Craft clear, engaging prose that serves the story perfectly')}
    
    ADVANCED TECHNIQUES:
    - Open with a hook that immediately establishes character, conflict, or atmosphere
    - Use the "show don't tell" principle relentlessly - actions and dialogue over exposition
    - Employ specific, concrete details rather than abstract descriptions
    - Create rhythm through sentence variety - short punchy sentences mixed with flowing longer ones
    - End paragraphs with compelling hooks that pull readers forward
    - Use active voice and strong verbs to create energy and immediacy
    - Weave backstory naturally through action and dialogue, never in information dumps
    - Create transitions that feel seamless and maintain narrative flow
    - Build to a climax that feels both surprising and inevitable
    - Craft an ending that resolves the plot while resonating emotionally"""

def create_master_story_prompt(user_prompt, theme, length, tone, pov, creativity_level):
    """Create an expert-level prompt using advanced techniques"""
    
    # Get specialized components
    sensory_prompt = get_sensory_details_prompt(theme)
    character_prompt = get_character_depth_prompt(pov, theme)
    genre_prompt = get_genre_mastery_prompt(theme)
    prose_prompt = get_prose_excellence_prompt(tone, length)
    
    # Set creativity instructions based on level
    creativity_instructions = ""
    if creativity_level > 0.8:
        creativity_instructions = """MAXIMUM CREATIVITY MODE:
        - Take bold, unexpected narrative risks
        - Subvert genre expectations in surprising ways
        - Create unique narrative structures or perspectives
        - Blend genres if it serves the story
        - Invent fresh metaphors and original imagery"""
    elif creativity_level > 0.6:
        creativity_instructions = """ENHANCED CREATIVITY:
        - Add original twists to familiar elements
        - Create unexpected character connections
        - Use unique angles on common themes
        - Include surprising but logical plot developments"""
    else:
        creativity_instructions = """BALANCED APPROACH:
        - Focus on solid storytelling fundamentals
        - Create engaging but accessible narratives
        - Use proven techniques with personal touches"""
    
    # POV expertise
    pov_mastery = {
        "First Person": """FIRST PERSON MASTERY:
        - Create an authentic, distinctive narrative voice
        - Use introspection naturally without over-explaining
        - Show the narrator's personality through word choice and observation
        - Reveal information as the narrator discovers or remembers it
        - Balance internal thoughts with external action and dialogue""",
        
        "Third Person": """THIRD PERSON MASTERY:
        - Maintain consistent point of view (limited or omniscient)
        - Use selective focus to control reader attention and emotion
        - Reveal character thoughts and motivations through action and dialogue
        - Create intimacy through close psychological distance when needed
        - Balance multiple character perspectives if using multiple viewpoints"""
    }
    
    # Construct the master prompt
    master_prompt = f"""You are a master storyteller with decades of experience across all genres. Your stories are published in prestigious magazines, win awards, and leave readers breathless. You understand the deep craft of storytelling at a level that few achieve.

STORY MISSION: Transform this concept into a masterpiece: "{user_prompt}"

{creativity_instructions}

GENRE EXPERTISE REQUIRED:
{genre_prompt}

CHARACTER MASTERY:
{character_prompt}

{pov_mastery[pov]}

SENSORY IMMERSION:
Paint vivid scenes using: {sensory_prompt}
Every scene should feel tangible and immediate. Readers should feel like they're experiencing, not just reading.

{prose_prompt}

PROFESSIONAL STANDARDS:
- Every sentence must earn its place - cut ruthlessly
- Create subtext in dialogue - characters say one thing, mean another
- Use conflict in every scene, even quiet moments
- Build story questions that make readers unable to stop
- Create emotional resonance that lingers after reading
- Establish clear stakes that matter to both character and reader

NARRATIVE ARCHITECTURE:
- OPENING: Grab immediately with character in motion or conflict
- DEVELOPMENT: Escalate conflict while deepening character
- CLIMAX: Create a moment that changes everything
- RESOLUTION: Satisfy emotionally while leaving some mystery

EXPERT EXECUTION CHECKLIST:
✓ Every character has a clear want and obstacle
✓ Every scene advances plot AND character
✓ Dialogue sounds natural when read aloud
✓ Setting serves mood and theme, not just backdrop
✓ Emotional beats feel earned, not manipulated
✓ Ending feels both surprising and inevitable
✓ Prose flows with natural rhythm and varies in pace
✓ Specific details create universal emotions

Remember: You're not just telling a story - you're creating an experience that will haunt readers long after they finish. Make every word count. Make every moment matter.

Now craft your masterpiece."""

    return master_prompt

# =============================================================================
# STORY GENERATION WITH ADVANCED PARAMETERS
# =============================================================================
def generate_story(client, prompt, creativity_level):
    """Generate a story using advanced parameters"""
    try:
        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "system",
                    "content": "You are a world-class storyteller known for creating deeply engaging, emotionally resonant narratives. Your stories are praised for their authentic characters, immersive settings, and compelling plots that stay with readers long after they finish reading."
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            model="gemma2-9b-it",
            temperature=creativity_level,  # User-controlled creativity
            max_tokens=3000,  # Increased for longer, more detailed stories
            top_p=0.95,      # High diversity for creative responses
            frequency_penalty=0.1,  # Reduce repetition
            presence_penalty=0.1,   # Encourage new topics
            stream=False
        )
        
        return chat_completion.choices[0].message.content
        
    except Exception as e:
        st.error(f"Error generating story: {str(e)}")
        return None

# =============================================================================
# MAIN APPLICATION UI
# =============================================================================

st.title("📚 AI Story Generator Pro")
st.markdown("*Create exceptional stories with advanced AI prompting techniques*")

# =============================================================================
# API KEY CONFIGURATION
# =============================================================================
if not (st.secrets.get("GROQ_API_KEY") or os.getenv("GROQ_API_KEY")):
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

# =============================================================================
# MAIN APPLICATION
# =============================================================================
if st.secrets.get("GROQ_API_KEY") or os.getenv("GROQ_API_KEY"):
    client = init_groq_client()
    
    # =============================================================================
    # SIDEBAR CONTROLS
    # =============================================================================
    with st.sidebar:
        st.header("🎭 Story Mastery Controls")
        
        # Theme selection with descriptions
        theme = st.selectbox(
            "Genre Expertise:",
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
        
        # Advanced length control
        length = st.select_slider(
            "Story Depth:",
            options=["Short", "Medium", "Long"],
            value="Medium",
            help="Short: Focused impact, Medium: Rich development, Long: Epic depth"
        )
        
        st.subheader("🎨 Artistic Direction")
        
        # Enhanced tone options
        tone = st.selectbox(
            "Emotional Tone:",
            ["Neutral", "Dark", "Light-hearted", "Dramatic", "Humorous"],
            help="Sets the emotional atmosphere and word choice"
        )
        
        # POV with expertise
        pov = st.radio(
            "Narrative Perspective:",
            ["First Person", "Third Person"],
            help="First Person: Intimate, personal. Third Person: Versatile, cinematic"
        )
        
        st.subheader("⚡ AI Parameters")
        
        # Creativity slider with detailed help
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
            ["Straightforward", "Layered", "Complex"],
            index=1,
            help="Controls plot intricacy and character development depth"
        )

    # =============================================================================
    # MAIN CONTENT AREA
    # =============================================================================
    col1, col2 = st.columns([3, 1])

    with col1:
        st.header("✨ Your Story Vision")
        
        # Enhanced example prompts
        example_prompts = {
            "Fantasy": "A librarian discovers that every book they touch reveals the true fate of its previous readers",
            "Science Fiction": "Memory merchants sell experiences to the highest bidder, but one memory refuses to be sold",
            "Mystery/Thriller": "A forensic accountant finds their own signature on documents from before they were born",
            "Romance": "Two people keep meeting in dreams before they meet in real life",
            "Horror": "A child's imaginary friend starts leaving physical evidence of their existence",
            "Adventure": "A cartographer discovers their maps are changing to show places that don't exist yet",
            "Comedy": "A professional mourner accidentally attends the wrong funeral and can't escape",
            "Drama": "A parent finds their estranged child's diary and realizes they never knew them at all"
        }
        
        # Story concept input
        prompt = st.text_area(
            "Describe your story concept:",
            placeholder=f"Inspiration: {example_prompts.get(theme, 'A moment that changes everything...')}",
            height=150,
            help="The more specific and unique your concept, the more engaging your story will be. Include characters, conflicts, or intriguing situations."
        )
        
        # Advanced options
        with st.expander("🔧 Advanced Story Elements"):
            col_a, col_b = st.columns(2)
            
            with col_a:
                setting_era = st.selectbox(
                    "Time Period:",
                    ["Contemporary", "Historical", "Future", "Timeless"],
                    help="Influences language, technology, and social context"
                )
                
                emotional_core = st.selectbox(
                    "Emotional Core:",
                    ["Love", "Loss", "Discovery", "Redemption", "Survival", "Growth", "Justice", "Freedom"],
                    index=2,
                    help="The underlying emotional journey"
                )
            
            with col_b:
                story_structure = st.selectbox(
                    "Narrative Structure:",
                    ["Linear", "Flashbacks", "Multiple Timeline", "Circular"],
                    help="How the story unfolds"
                )
                
                include_twist = st.checkbox(
                    "Include Plot Twist",
                    value=True,
                    help="Add an unexpected but logical story revelation"
                )

        # Generate button
        generate_button = st.button("🎭 Create Masterpiece", type="primary", use_container_width=True)

    with col2:
        st.header("📊 Story Profile")
        
        if prompt:
            # Enhanced preview
            word_estimates = {"Short": "600-800", "Medium": "1200-1500", "Long": "2000-2500"}
            
            st.markdown(f"""
            **Genre:** {theme}  
            **Length:** {length} ({word_estimates[length]} words)  
            **Tone:** {tone}  
            **Perspective:** {pov}  
            **Creativity:** {int(creativity_level * 100)}%  
            **Complexity:** {complexity}  
            """)
            
            # Estimated reading time
            avg_words = {"Short": 700, "Medium": 1350, "Long": 2250}
            read_time = max(1, avg_words[length] // 200)
            st.success(f"📖 Est. Reading Time: {read_time}-{read_time+1} min")

    # =============================================================================
    # STORY GENERATION
    # =============================================================================
    if generate_button:
        if not prompt:
            st.error("Please provide a story concept to bring to life!")
        else:
            # Create the master prompt
            story_prompt = create_master_story_prompt(
                prompt, theme, length, tone, pov, creativity_level
            )
            
            # Generation with progress
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
            
            generated_story = generate_story(client, story_prompt, creativity_level)
            
            progress_bar.progress(100)
            status_text.text("✨ Story complete!")
            time.sleep(0.5)
            
            # Clear progress indicators
            progress_bar.empty()
            status_text.empty()
            
            if generated_story:
                st.header("📖 Your Masterpiece")
                
                # Enhanced story display
                st.markdown(f"""
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
                {generated_story.replace(chr(10), '<br><br>')}
                </div>
                """, unsafe_allow_html=True)
                
                # =============================================================================
                # STORY ANALYTICS
                # =============================================================================
                st.subheader("📊 Story Analytics")
                col1, col2, col3, col4, col5 = st.columns(5)
                
                word_count = len(generated_story.split())
                sentence_count = generated_story.count('.') + generated_story.count('!') + generated_story.count('?')
                avg_sentence_length = word_count / max(sentence_count, 1)
                
                with col1:
                    st.metric("Words", word_count)
                with col2:
                    st.metric("Sentences", sentence_count)
                with col3:
                    st.metric("Avg Sentence", f"{avg_sentence_length:.1f}")
                with col4:
                    st.metric("Read Time", f"{max(1, word_count // 200)} min")
                with col5:
                    st.metric("Genre", theme)
                
                # =============================================================================
                # ENHANCED ACTIONS
                # =============================================================================
                st.subheader("🔧 Story Actions")
                col1, col2, col3, col4, col5 = st.columns(5)
                
                with col1:
                    if st.button("📋 Copy Text"):
                        st.code(generated_story, language='text')
                        st.success("Story formatted for copying!")
                
                with col2:
                    if st.button("🔄 New Variation"):
                        st.rerun()
                
                with col3:
                    if st.button("📊 Analyze Style"):
                        # Simple style analysis
                        dialogue_count = generated_story.count('"')
                        action_indicators = generated_story.lower().count(' ran ') + generated_story.lower().count(' walked ') + generated_story.lower().count(' moved ')
                        
                        st.info(f"""
                        **Style Analysis:**
                        - Dialogue: {dialogue_count // 2} exchanges
                        - Action Level: {'High' if action_indicators > 5 else 'Medium' if action_indicators > 2 else 'Low'}
                        - Complexity: {complexity}
                        """)
                
                with col4:
                    if st.button("💾 Save Story"):
                        if "masterpieces" not in st.session_state:
                            st.session_state.masterpieces = []
                        
                        story_data = {
                            "prompt": prompt,
                            "theme": theme,
                            "story": generated_story,
                            "word_count": word_count,
                            "settings": f"{length}/{tone}/{pov}",
                            "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
                        }
                        
                        st.session_state.masterpieces.append(story_data)
                        st.success("Masterpiece saved!")
                
                with col5:
                    if st.button("🎨 Refine Style"):
                        st.info("Style refinement will be available in the next update!")

    # =============================================================================
    # SAVED MASTERPIECES
    # =============================================================================
    if "masterpieces" in st.session_state and st.session_state.masterpieces:
        st.markdown("---")
        with st.expander(f"📚 Your Masterpieces ({len(st.session_state.masterpieces)})"):
            for i, story_data in enumerate(reversed(st.session_state.masterpieces)):
                col1, col2, col3 = st.columns([3, 1, 1])
                
                with col1:
                    st.markdown(f"**{story_data['theme']}** - {story_data['timestamp']}")
                    st.markdown(f"*{story_data['prompt'][:80]}...*")
                
                with col2:
                    st.metric("Words", story_data['word_count'])
                
                with col3:
                    if st.button(f"Read", key=f"read_{i}"):
                        st.markdown("---")
                        st.markdown(story_data['story'])

# =============================================================================
# FOOTER
# =============================================================================
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #666; padding: 20px;">
    <h4>🎭 AI Story Generator Pro</h4>
    <p>Powered by Advanced Prompting Techniques & Groq AI</p>
    <p><small>Creating masterpieces with Llama-3.1-70B • Built with expertise and creativity</small></p>
</div>
""", unsafe_allow_html=True)