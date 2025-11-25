import os
import requests
import time
from .base_agent import BaseAgent

class ImageAgent(BaseAgent):
    def __init__(self):
        # Using Pollinations.ai which doesn't require an API key or model initialization
        pass

    def generate_image(self, prompt, output_path):
        # Truncate prompt to avoid URL length issues
        safe_prompt = prompt[:100] if prompt else "presentation image"
        
        # Retry logic
        for attempt in range(3):
            try:
                print(f"Generating image for prompt: {safe_prompt} (Attempt {attempt+1})")
                
                encoded_prompt = requests.utils.quote(safe_prompt)
                url = f"https://image.pollinations.ai/prompt/{encoded_prompt}?width=800&height=600&nologo=true"
                
                response = requests.get(url, timeout=10)
                if response.status_code == 200:
                    with open(output_path, 'wb') as f:
                        f.write(response.content)
                    print(f"Image saved to {output_path}")
                    return output_path
                else:
                    print(f"Failed to generate image. Status code: {response.status_code}")
                    time.sleep(2) # Wait before retry
            except Exception as e:
                print(f"Error generating image: {e}")
                time.sleep(2)

        # Fallback to local placeholder
        print("Falling back to local placeholder image.")
        return self._generate_placeholder(prompt, output_path)

    def _generate_placeholder(self, prompt, output_path):
        try:
            from PIL import Image, ImageDraw, ImageFont
            img = Image.new('RGB', (800, 600), color = (73, 109, 137))
            d = ImageDraw.Draw(img)
            try:
                font = ImageFont.truetype("arial.ttf", 20)
            except IOError:
                font = ImageFont.load_default()
            d.text((50, 250), "Image Generation Failed", font=font, fill=(255, 255, 255))
            d.text((50, 300), prompt[:50] + "...", font=font, fill=(255, 255, 255))
            img.save(output_path)
            return output_path
        except Exception as e:
            print(f"Error generating placeholder: {e}")
            return None
