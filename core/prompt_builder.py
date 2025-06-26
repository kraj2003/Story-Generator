from typing import Dict, Any
from config.prompts import PromptTemplates
from config.settings import AppSettings

class PromptBuilder:
    def __init__(self):
        self.templates = PromptTemplates()
        self.settings = AppSettings()
    
    def get_sensory_details_prompt(self, theme: str) -> str:
        return self.templates.SENSORY_DETAILS.get(
            theme, 
            "rich sensory details that immerse the reader completely"
        )
    
    def get_character_depth_prompt(self, pov: str, theme: str) -> str:
        if pov == "First Person":
            return f'''Develop the narrator as a complex, flawed, relatable human being with:
            - Internal contradictions and realistic psychology
            - A distinct voice with unique speech patterns, thoughts, and reactions
            - Specific background details that influence their worldview
            - Emotional vulnerabilities that make them three-dimensional
            - Skills, knowledge, or quirks relevant to the {theme.lower()} genre
            - A clear character arc that shows growth or change through the story'''
        else:
            return f'''Create multi-dimensional characters with:
            - Each character having distinct dialogue patterns, mannerisms, and motivations
            - Hidden depths revealed through actions rather than exposition
            - Relationships that feel authentic and complex
            - Backstories that inform but don't overwhelm the present action
            - Character flaws that create realistic conflict and growth opportunities
            - Specific expertise or knowledge that serves the {theme.lower()} plot naturally'''
    
    def get_genre_mastery_prompt(self, theme: str) -> str:
        return self.templates.GENRE_MASTERY.get(
            theme, 
            "Apply expert storytelling techniques for maximum emotional impact"
        )
    
    def get_prose_excellence_prompt(self, tone: str, length: str) -> str:
        word_targets = self.settings.WORD_TARGETS
        tone_styles = self.templates.TONE_STYLES
        
        return f'''Create exceptional prose with these techniques:
        
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
        - Craft an ending that resolves the plot while resonates emotionally'''
    
    def get_creativity_instructions(self, creativity_level: float) -> str:
        if creativity_level > 0.8:
            return '''MAXIMUM CREATIVITY MODE:
            - Take bold, unexpected narrative risks
            - Subvert genre expectations in surprising ways
            - Create unique narrative structures or perspectives
            - Blend genres if it serves the story
            - Invent fresh metaphors and original imagery'''
        elif creativity_level > 0.6:
            return '''ENHANCED CREATIVITY:
            - Add original twists to familiar elements
            - Create unexpected character connections
            - Use unique angles on common themes
            - Include surprising but logical plot developments'''
        else:
            return '''BALANCED APPROACH:
            - Focus on solid storytelling fundamentals
            - Create engaging but accessible narratives
            - Use proven techniques with personal touches'''
    
    def build_master_prompt(self, params: Dict[str, Any]) -> str:
        user_prompt = params['user_prompt']
        theme = params['theme']
        length = params['length']
        tone = params['tone']
        pov = params['pov']
        creativity_level = params['creativity_level']
        
        # Get all components
        sensory_prompt = self.get_sensory_details_prompt(theme)
        character_prompt = self.get_character_depth_prompt(pov, theme)
        genre_prompt = self.get_genre_mastery_prompt(theme)
        prose_prompt = self.get_prose_excellence_prompt(tone, length)
        creativity_instructions = self.get_creativity_instructions(creativity_level)
        pov_prompt = self.templates.POV_MASTERY[pov]
        
        # Build the complete prompt
        return self.templates.MASTER_TEMPLATE.format(
            user_prompt=user_prompt,
            creativity_instructions=creativity_instructions,
            genre_prompt=genre_prompt,
            character_prompt=character_prompt,
            pov_prompt=pov_prompt,
            sensory_prompt=sensory_prompt,
            prose_prompt=prose_prompt
        )
