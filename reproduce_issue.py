import json
from src.agents.content_agent import ContentAgent

# Mock outline data
mock_outline = {
  "presentation_title": "Agentic AI for Developers",
  "estimated_duration": "20 minutes",
  "target_audience": "Software Developers",
  "slides": [
    {
      "slide_number": 1,
      "title": "Introduction to Agentic AI",
      "slide_type": "title",
      "key_points": ["Definition", "Evolution", "Importance"]
    },
    {
      "slide_number": 2,
      "title": "Core Concepts",
      "slide_type": "content",
      "key_points": ["Agents", "Tools", "Planning"]
    }
  ]
}

print("Starting content generation reproduction...")
agent = ContentAgent()
try:
    content = agent.generate_content(mock_outline)
    if content:
        print("Content generated successfully.")
        print(json.dumps(content, indent=2))
    else:
        print("Failed to generate content.")
except Exception as e:
    print(f"Exception occurred: {e}")
