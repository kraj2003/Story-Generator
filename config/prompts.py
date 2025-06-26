from typing import Dict

class PromptTemplates:
    
    SENSORY_DETAILS = {
        "Fantasy": "ancient stone corridors echoing with whispers, the metallic taste of magic in the air, glowing runes that pulse with warmth, the musty scent of old grimoires, silk robes rustling against skin",
        "Science Fiction": "the sterile hum of life support systems, cold metal surfaces under fingertips, the acrid smell of ozone after energy discharge, holographic displays casting blue light on faces, synthetic air recycling through vents",
        "Mystery/Thriller": "creaking floorboards in empty houses, the weight of eyes watching from shadows, coffee growing cold in forgotten cups, rain pattering against windows, the sharp scent of fear-induced adrenaline",
        "Romance": "the warmth of intertwined fingers, soft candlelight dancing across skin, the lingering scent of perfume on clothes, whispered words that make hearts race, silk sheets cool against bare skin",
        "Horror": "the suffocating silence before something terrible happens, cold sweat beading on trembling skin, the metallic taste of fear, shadows that seem to move in peripheral vision, the smell of decay and forgotten time",
        "Adventure": "wind whipping through hair on mountain peaks, the burn of muscles pushed to their limit, exotic spices filling marketplace air, leather worn smooth by countless journeys, the sound of waves against wooden hulls",
        "Comedy": "the uncontrollable giggle that starts in the belly, coffee spilling in perfectly timed disasters, the ridiculous squeak of rubber shoes on polished floors, the warm feeling of shared laughter, absurd coincidences that defy logic",
        "Drama": "tears that blur vision and salt the lips, the hollow ache of words left unsaid, trembling hands reaching for connection, the weight of silence in hospital waiting rooms, rain that mirrors inner storms"
    }
    
    GENRE_MASTERY = {
        "Fantasy": '''Master these fantasy elements:
        - Create magic systems with clear rules, limitations, and costs
        - Build cultures with unique customs, languages, and belief systems
        - Design creatures that feel both wondrous and believable
        - Weave mythology naturally into the plot without info-dumping
        - Balance familiar fantasy tropes with fresh, unexpected twists
        - Show the impact of magic on society, economy, and daily life
        - Use archaic or formal language sparingly for atmosphere without alienating readers''',
        
        "Science Fiction": '''Execute advanced sci-fi techniques:
        - Ground futuristic technology in believable scientific principles
        - Explore the social and ethical implications of technological advancement
        - Create future societies that feel like natural progressions of current trends
        - Use scientific concepts to drive plot rather than just provide backdrop
        - Balance technical details with human storytelling
        - Address how technology changes human relationships and identity
        - Incorporate current scientific discoveries and theories authentically''',
        
        # ... (continue with other genres)
    }
    
    TONE_STYLES = {
        "Dark": "Use precise, evocative language with underlying tension. Employ shorter sentences during intense moments, longer flowing sentences for reflection. Choose words that carry emotional weight.",
        "Light-hearted": "Write with buoyant rhythm and playful language. Use varied sentence structures that feel musical. Include precise details that spark joy or amusement.",
        "Dramatic": "Employ powerful, emotional language with strong imagery. Use sentence rhythm to match emotional intensity. Choose words that resonate with deeper meaning.",
        "Humorous": "Craft sentences with comedic timing. Use unexpected word choices and juxtaposition. Vary rhythm for comedic effect - quick builds, perfect pauses.",
        "Neutral": "Use clear, engaging prose that serves the story. Vary sentence length naturally. Choose precise words that create vivid imagery without calling attention to themselves."
    }
    
    POV_MASTERY = {
        "First Person": '''FIRST PERSON MASTERY:
        - Create an authentic, distinctive narrative voice
        - Use introspection naturally without over-explaining
        - Show the narrator's personality through word choice and observation
        - Reveal information as the narrator discovers or remembers it
        - Balance internal thoughts with external action and dialogue''',
        
        "Third Person": '''THIRD PERSON MASTERY:
        - Maintain consistent point of view (limited or omniscient)
        - Use selective focus to control reader attention and emotion
        - Reveal character thoughts and motivations through action and dialogue
        - Create intimacy through close psychological distance when needed
        - Balance multiple character perspectives if using multiple viewpoints'''
    }
    
    SYSTEM_PROMPT = "You are a world-class storyteller known for creating deeply engaging, emotionally resonant narratives. Your stories are praised for their authentic characters, immersive settings, and compelling plots that stay with readers long after they finish reading."
    
    MASTER_TEMPLATE = '''You are a master storyteller with decades of experience across all genres. Your stories are published in prestigious magazines, win awards, and leave readers breathless. You understand the deep craft of storytelling at a level that few achieve.

STORY MISSION: Transform this concept into a masterpiece: "{user_prompt}"

{creativity_instructions}

GENRE EXPERTISE REQUIRED:
{genre_prompt}

CHARACTER MASTERY:
{character_prompt}

{pov_prompt}

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

Now craft your masterpiece.'''
