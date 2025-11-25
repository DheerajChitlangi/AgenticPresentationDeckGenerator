import os
import argparse
import json
from src.agents.outline_agent import OutlineAgent
from src.agents.content_agent import ContentAgent
from src.agents.critic_agent import CriticAgent
from src.utils.pptx_generator import PPTXGenerator

def main():
    parser = argparse.ArgumentParser(description="Agentic Presentation Deck Generator")
    parser.add_argument("--topic", type=str, required=True, help="Topic of the presentation")
    parser.add_argument("--output", type=str, default="presentation.pptx", help="Output filename")
    parser.add_argument("--audience", type=str, default="General", help="Target audience")
    parser.add_argument("--tone", type=str, default="Professional", help="Presentation tone")
    parser.add_argument("--context_file", type=str, help="Path to a text file with additional context")
    parser.add_argument("--slides", type=int, help="Desired number of slides")
    parser.add_argument("--images", action="store_true", help="Generate images for slides")
    parser.add_argument("--instructions", type=str, help="Custom instructions for the agents")
    args = parser.parse_args()

    context = ""
    if args.context_file:
        try:
            with open(args.context_file, 'r') as f:
                context = f.read()
            print(f"Loaded context from {args.context_file}")
        except Exception as e:
            print(f"Error reading context file: {e}")

    print(f"Starting generation for topic: {args.topic}")
    print(f"Audience: {args.audience}, Tone: {args.tone}")
    if args.instructions:
        print(f"Custom Instructions: {args.instructions}")

    # 1. Outline Agent
    print("\n--- Step 1: Generating Outline ---")
    outline_agent = OutlineAgent()
    outline = outline_agent.create_outline(args.topic, args.audience, args.tone, context, args.slides, args.instructions)
    if not outline:
        print("Failed to generate outline.")
        return
    print("Outline generated successfully.")

    # 2. Content Agent
    print("\n--- Step 2: Generating Content ---")
    content_agent = ContentAgent()
    content = content_agent.generate_content(outline, args.audience, args.tone, context, args.instructions)
    if not content:
        print("Failed to generate content.")
        return
    print("Content generated successfully.")

    # 3. Critic Agent
    print("\n--- Step 3: Reviewing and Refining ---")
    critic_agent = CriticAgent()
    refined_content = critic_agent.critique_presentation(content, args.audience, args.tone, context, args.instructions)
    if not refined_content:
        print("Failed to refine content. Using original content.")
        refined_content = content
    else:
        print("Content refined successfully.")
        print(f"Quality Score: {refined_content.get('overall_quality_score', 'N/A')}")

    # 3.5 Generate Images
    if args.images:
        print("\n--- Step 3.5: Generating Images ---")
        from src.agents.image_agent import ImageAgent
        image_agent = ImageAgent()
        
        # Create images directory
        os.makedirs("images", exist_ok=True)
        
        slides = refined_content.get("refined_slides", refined_content.get("slides", []))
        for i, slide in enumerate(slides):
            if "image_prompt" in slide and slide["image_prompt"]:
                print(f"Generating image for slide {i+1}...")
                image_path = os.path.join("images", f"slide_{i+1}.png")
                generated_path = image_agent.generate_image(slide["image_prompt"], image_path)
                if generated_path:
                    slide["image_path"] = generated_path
    else:
        print("\n--- Skipping Image Generation (use --images to enable) ---")

    # 4. Generate PPTX
    print("\n--- Step 4: Creating PowerPoint ---")
    generator = PPTXGenerator()
    generator.create_presentation(refined_content, output_file=args.output)
    print("\nDone!")

if __name__ == "__main__":
    main()
