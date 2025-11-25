import json
from .base_agent import BaseAgent

class ContentAgent(BaseAgent):
    def __init__(self):
        super().__init__()
        self.metaprompt = """
You are an expert presentation content writer. Your task is to transform an outline into detailed, engaging slide content.

INPUTS:
- Structured outline from Outline Agent
- Target Audience
- Tone
- Context/Notes

OUTPUT: Fully developed slide content

Guidelines:
- Write concise, impactful bullet points (5-7 words per bullet).
- Include speaker notes for each slide (2-3 sentences).
- Suggest visual elements (charts, images, icons) where appropriate.
- Use action-oriented language matching the desired tone.
- Ensure consistency in tone and style.
- Add data points or statistics where relevant.
- IMPORTANT: Return ONLY valid JSON. No markdown formatting or code blocks.

Output format:
{
  "slides": [
    {
      "slide_number": 1,
      "title": "Introduction to AI",
      "layout": "Title and Content",
      "bullet_points": ["Point 1", "Point 2"],
      "speaker_notes": "Welcome everyone...",
      "image_prompt": "A detailed description of an image..."
    },
    ...
  ]
}
"""

    def generate_content(self, outline, audience="General", tone="Professional", context=""):
        prompt = f"{self.metaprompt}\n\nOUTLINE: {json.dumps(outline, indent=2)}\nTARGET AUDIENCE: {audience}\nTONE: {tone}\nCONTEXT: {context}"
        response = self.generate(prompt)
        if response:
            try:
                cleaned_response = response.replace("```json", "").replace("```", "").strip()
                return json.loads(cleaned_response)
            except json.JSONDecodeError:
                print("Error decoding JSON from Content Agent")
                print(response)
                return None
        return None
