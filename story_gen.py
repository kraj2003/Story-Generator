import streamlit as st
import time
import random

# Configure page
st.set_page_config(
    page_title="AI Story Generator",
    page_icon="📚",
    layout="wide"
)

# App title and description
st.title("📚 AI Story Generator")
st.markdown("Generate creative stories based on your ideas and preferred themes!")

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

# Main content area
col1, col2 = st.columns([2, 1])

with col1:
    st.header("Your Story Prompt")
    
    # Story prompt input
    prompt = st.text_area(
        "Describe your story idea:",
        placeholder="Example: A detective finds a mysterious letter that leads to an ancient secret...",
        height=100
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
        word_counts = {"Short": "300-500", "Medium": "800-1200", "Long": "1500-2500"}
        st.success(f"**Est. Words:** {word_counts[length]}")

# Story generation and display
if generate_button:
    if not prompt:
        st.error("Please enter a story prompt!")
    else:
        # Show loading spinner
        with st.spinner(f"Generating your {theme.lower()} story..."):
            # Simulate AI processing time
            time.sleep(2)
        
        # Display generated story
        st.header("📖 Your Generated Story")
        
        # Sample stories based on theme (for demonstration)
        sample_stories = {
            "Fantasy": """The ancient oak whispered secrets that only Elara could understand. As she pressed her palm against its gnarled bark, visions of a forgotten realm flooded her mind. Dragons soared through crystalline skies, their scales catching light like scattered diamonds.

"You have been chosen," the tree's voice echoed in her thoughts. "The realm of Aethermoor needs its guardian."

Elara stepped back, her heart racing. The ordinary forest around her began to shimmer, revealing hidden pathways lined with luminescent flowers. Magic thrummed in the air, calling to something deep within her soul.

She had always felt different, but now she understood why. This was her destiny – to bridge two worlds and restore the balance between magic and reality.""",
            
            "Science Fiction": """Captain Nova Chen stared at the anomalous readings on her console. The wormhole shouldn't exist here, not in this sector of space. Yet there it was, pulsing with an energy signature unlike anything in the databases.

"Proximity alert," her AI companion, ARIA, announced. "Unknown vessel approaching through the anomaly."

The ship that emerged defied physics as Nova understood it. Its hull seemed to bend light around itself, creating ripples in space-time. Then, impossibly, a transmission came through on ancient Earth frequencies.

"This is Terra Ship Odyssey, calling any Earth vessel. We've been lost for three hundred years. What year is it?"

Nova's hands trembled as she reached for the communications array. The Odyssey was legend – the first deep space exploration vessel, lost to history. How could it have survived? And what had it discovered in those three centuries of wandering?""",
            
            "Mystery/Thriller": """Detective Sarah Mills examined the cryptic letter one more time. The paper was aged, the ink faded, but the message was clear: "The truth about the Blackwood family lies beneath the thirteenth step."

The Blackwood mansion had been abandoned for decades, ever since the mysterious disappearance of the entire family during a thunderstorm in 1987. Local police had closed the case, citing lack of evidence, but Sarah had always suspected there was more to the story.

As she climbed the mansion's grand staircase, counting each step, her flashlight beam danced across portraits of long-dead Blackwoods. Their eyes seemed to follow her progress. Twelve steps. Thirteen.

She knelt and examined the thirteenth step closely. There – a barely visible seam in the wood. As she pried it open, a hidden compartment revealed a collection of documents that would change everything she thought she knew about that fateful night.""",
            
            "Romance": """Emma had always believed that love at first sight was just a fairy tale, until she collided with a stranger at the coffee shop on Fifth Street. Books scattered everywhere, coffee splashed, and in that moment of chaos, their eyes met.

"I'm so sorry," he said, his voice warm despite the embarrassment. "Let me help you with those."

As they gathered her scattered novels, their hands brushed, sending an unexpected spark through Emma's fingers. She noticed how carefully he handled her books, reading the titles with genuine interest.

"Jane Austen and Gabriel García Márquez," he observed with a smile. "Interesting combination."

"You know literature?" Emma asked, surprised.

"I teach it," he replied, extending his hand. "I'm David. And you've just destroyed my morning coffee with the most beautiful book collection I've ever seen scattered on a coffee shop floor."

Emma laughed, accepting his hand. "Emma. And I think I owe you a coffee.""",
            
            "Horror": """The old music box had been in the attic for as long as anyone could remember. When Lisa finally decided to clean out her grandmother's house, she found it tucked behind decades of forgotten memories.

The melody it played was hauntingly beautiful, but there was something wrong with it. The ballerina inside spun too slowly, and her painted smile seemed to shift when Lisa wasn't looking directly at it.

That first night, Lisa woke to the sound of the music box playing downstairs. But she had left it in the attic. Hadn't she?

As she crept down the stairs, the melody grew louder, more distorted. The living room was empty, but the music box sat open on the coffee table, the ballerina spinning in the moonlight.

And then Lisa noticed the footprints – small, delicate prints leading from the coffee table to the basement door. Prints that looked like they belonged to a porcelain dancer.""",
            
            "Adventure": """The treasure map had been in Jake's family for generations, dismissed as a child's drawing until the earthquake revealed the hidden cave system beneath their property. Now, standing at the entrance with his backpack and headlamp, Jake realized his great-grandfather might not have been the dreamer everyone thought he was.

The cave stretched deeper than his light could reach, and the air carried a hint of salt – impossible, considering they were hundreds of miles from the ocean. Following the crude drawings on the map, Jake navigated through narrow passages and vast underground chambers.

Hours into his journey, he heard it: the sound of rushing water. The passage opened into a massive cavern containing an underground river, and there, half-buried in the sandy shore, was the bow of an ancient ship.

Pirates, Jake realized with growing excitement. This wasn't just any treasure hunt – he had stumbled upon a piece of history that would rewrite everything they knew about their quiet mountain town.""",
            
            "Comedy": """Margaret had always prided herself on being organized. Her life ran like clockwork: coffee at 7 AM, emails at 7:30, gym at 6 PM. So when she woke up to find a llama in her backyard, her carefully structured world took a decidedly surreal turn.

"Excuse me," she called out to the llama, feeling ridiculous. "You can't be here."

The llama, who seemed remarkably unconcerned by her protest, continued munching on her prize-winning roses. Margaret grabbed her phone to call animal control, only to discover that the llama was wearing a tiny hat with her address embroidered on it.

A knock at the door interrupted her confusion. Standing on her porch was her elderly neighbor, Mr. Peterson, holding a leash and looking sheepish.

"Have you seen Frederick?" he asked. "He's my emotional support llama. I may have forgotten to mention him when I moved in last week.""",
            
            "Drama": """The phone call came at 3 AM, the way life-changing news always seems to. Rachel stared at the screen, her sister's name flashing insistently. They hadn't spoken in two years, not since the fight that had torn their family apart.

"Rachel?" Jenny's voice was small, scared. "It's Mom. She's in the hospital, and... they don't think she has much time."

The drive to the hospital felt endless and too short all at once. Rachel's mind raced through years of memories – childhood summers, family dinners, and then the bitter words that had driven them apart. Their mother had tried to reconcile them, but pride had kept both sisters stubborn and silent.

Now, standing outside the ICU, Rachel realized how meaningless their fight had become. Through the window, she could see her mother, fragile and still, connected to machines that beeped softly in the sterile air.

Jenny appeared beside her, tears streaming down her face. Without a word, the sisters embraced, their shared grief finally breaking down the walls they had built between them."""
        }
        
        # Display the sample story based on selected theme
        story_text = sample_stories.get(theme, "Story generation coming soon!")
        
        # Add some styling to the story display
        st.markdown(f"""
        <div style="
            background-color: #f8f9fa;
            padding: 20px;
            border-radius: 10px;
            border-left: 4px solid #007acc;
            margin: 20px 0;
        ">
        {story_text}
        </div>
        """, unsafe_allow_html=True)
        
        # Story stats
        col1, col2, col3 = st.columns(3)
        with col1:
            word_count = len(story_text.split())
            st.metric("Word Count", word_count)
        with col2:
            read_time = max(1, word_count // 200)  # Average reading speed
            st.metric("Read Time", f"{read_time} min")
        with col3:
            st.metric("Theme", theme)
        
        # Action buttons
        st.subheader("Actions")
        col1, col2, col3 = st.columns(3)
        
        with col1:
            if st.button("📝 Edit Story"):
                st.info("Story editing feature coming soon!")
        
        with col2:
            if st.button("🔄 Generate Another"):
                st.rerun()
        
        with col3:
            if st.button("🔊 Text-to-Speech"):
                st.info("Text-to-speech feature will be added in the next version!")

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #666;">
    <p>Built with Streamlit | AI Story Generator v1.0</p>
    <p><small>This is a prototype - actual AI integration coming soon!</small></p>
</div>
""", unsafe_allow_html=True)