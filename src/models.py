from typing import List, Optional
from pydantic import BaseModel, Field

class Slide(BaseModel):
    slide_number: int = Field(..., description="The sequential number of the slide")
    title: str = Field(..., description="The title of the slide")
    content: List[str] = Field(..., description="Bullet points or main content text")
    speaker_notes: str = Field(..., description="Script for the presenter")
    visual_suggestions: Optional[str] = Field(None, description="Description of suggested charts or diagrams")
    image_prompt: Optional[str] = Field(None, description="Prompt for generating an AI image for this slide")
    layout_type: str = Field("bullets", description="Suggested layout: title, bullets, two-column, visual")

class PresentationOutline(BaseModel):
    presentation_title: str
    target_audience: str
    estimated_duration: str
    slides: List[dict] # Keeping it flexible for the outline stage, or could be strict

class PresentationContent(BaseModel):
    presentation_title: str
    slides: List[Slide]
    overall_quality_score: Optional[str] = None
