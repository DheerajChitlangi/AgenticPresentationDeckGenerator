import json
from .base_agent import BaseAgent

class OutlineAgent(BaseAgent):
    def __init__(self):
        super().__init__()
        self.metaprompt = """
You are an expert presentation strategist. Your task is to create a comprehensive outline for a presentation deck.

INPUTS:
- Topic: The main subject.
- Target Audience: Who the presentation is for.
- Tone: The desired style (e.g., Professional, Inspiring, Educational).
- Context/Notes: Additional background information or requirements.
- Slide Count: Desired number of slides.

OUTPUT: Structured JSON outline

Guidelines:
- Create the requested number of slides (default 8-12 if unspecified).
- Include: Title slide, agenda, content slides, conclusion, Q&A.
- Each slide should have: slide_number, title, key_points (3-5 bullets), slide_type.
- Ensure logical flow and narrative arc suitable for the audience.
- Adapt the language and depth to the target audience.
- IMPORTANT: Return ONLY valid JSON. No markdown formatting or code blocks.

Output format:
{
  "presentation_title": "...",
  "estimated_duration": "X minutes",
  "target_audience": "...",
  "slides": [
    {
      "slide_number": 1,
      "title": "...",
      "slide_type": "title",
      "key_points": []
    },
    ...
  ]
}
"""

    def create_outline(self, topic, audience="General", tone="Professional", context="", slide_count=None, instructions=""):
        prompt = f"{self.metaprompt}\n\nTOPIC: {topic}\nTARGET AUDIENCE: {audience}\nTONE: {tone}\nCONTEXT: {context}"
        if slide_count:
            prompt += f"\nSLIDE COUNT: {slide_count}"
        if instructions:
            prompt += f"\nCUSTOM INSTRUCTIONS: {instructions}"
            
        response = self.generate(prompt)
        if response:
            try:
                # Clean up potential markdown code blocks
                cleaned_response = response.replace("```json", "").replace("```", "").strip()
                return json.loads(cleaned_response)
            except json.JSONDecodeError:
                print("Error decoding JSON from Outline Agent")
                print(response)
                return None
        return None
