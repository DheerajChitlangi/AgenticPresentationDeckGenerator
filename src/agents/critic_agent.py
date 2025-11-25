import json
from .base_agent import BaseAgent

class CriticAgent(BaseAgent):
    def __init__(self):
        super().__init__()
        self.metaprompt = """
You are a senior presentation consultant with expertise in corporate communications and visual storytelling. Your task is to review and improve presentation decks.

INPUTS:
- Complete presentation draft
- Target Audience
- Tone
- Context/Notes

OUTPUT: Refined presentation with improvements and feedback report

Evaluation criteria:
1. **Clarity**: Are messages clear and easy to understand?
2. **Flow**: Does the narrative progress logically?
3. **Impact**: Are key messages memorable and compelling?
4. **Visual Balance**: Is text-to-visual ratio appropriate?
5. **Professionalism**: Does it meet corporate standards?
6. **Audience Alignment**: Does it suit the target audience? Is the tone correct?

Actions to perform:
- Simplify overly complex bullets
- Enhance weak or vague statements
- Suggest better slide titles (should be assertive, not generic)
- Recommend reorganization if flow is weak
- Flag slides with too much text
- Improve consistency across slides
- Ensure the tone matches the requested tone (e.g., Professional, Inspiring)
- IMPORTANT: Return ONLY valid JSON. No markdown formatting or code blocks.

Output format:
{
  "overall_quality_score": "X/10",
  "improvements_made": ["change 1", "change 2", ...],
  "critical_issues": ["issue 1", ...],
  "refined_slides": [
    {
      "slide_number": 1,
      "title": "...",
      "layout": "Title and Content",
      "bullet_points": ["bullet 1", "bullet 2", ...],
      "speaker_notes": "...",
      "visual_suggestions": "...",
      "image_prompt": "..."
    },
    ...
  ],
  "recommendations": "Additional suggestions for the user"
}
"""

    def critique_presentation(self, content, audience="General", tone="Professional", context=""):
        prompt = f"{self.metaprompt}\n\nDRAFT CONTENT: {json.dumps(content, indent=2)}\nTARGET AUDIENCE: {audience}\nTONE: {tone}\nCONTEXT: {context}"
        response = self.generate(prompt)
        if response:
            try:
                cleaned_response = response.replace("```json", "").replace("```", "").strip()
                return json.loads(cleaned_response)
            except json.JSONDecodeError:
                print("Error decoding JSON from Critic Agent")
                print(response)
                return None
        return None
