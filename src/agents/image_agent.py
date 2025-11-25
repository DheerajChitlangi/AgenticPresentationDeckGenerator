import os
import requests
import time
from .base_agent import BaseAgent

class ImageAgent(BaseAgent):
    def __init__(self):
        # Initialize Google GenAI for Imagen
        import google.generativeai as genai
        api_key = os.getenv("GOOGLE_API_KEY")
        if api_key:
            genai.configure(api_key=api_key)
            # Check if ImageGenerationModel is available (newer versions)
            if hasattr(genai, "ImageGenerationModel"):
                self.imagen_model = genai.ImageGenerationModel("imagen-3.0-generate-001")
            else:
                self.imagen_model = None
                print("Warning: google.generativeai version does not support ImageGenerationModel. Using fallback.")
        else:
            self.imagen_model = None

    def generate_image(self, prompt, output_path):
        # 1. Try Google Imagen First
        if self.imagen_model:
            try:
                print("Attempting to generate with Google Imagen...")
                result = self.imagen_model.generate_images(
                    prompt=prompt,
                    number_of_images=1,
                )
                if result and result.images:
                    result.images[0].save(output_path)
                    print(f"Imagen generated image saved to {output_path}")
                    return output_path
            except Exception as e:
                print(f"Imagen generation failed (likely due to billing/quota): {e}")
                print("Falling back to Pollinations.ai...")

        # 2. Fallback to Pollinations.ai
        # Enhance prompt for better quality
        enhanced_prompt = f"{prompt}, professional, high quality, 4k, detailed, presentation style"
        
        # Truncate to avoid URL issues (Pollinations handles up to ~1000 chars usually, but safe limit)
        safe_prompt = enhanced_prompt[:500]
        encoded_prompt = requests.utils.quote(safe_prompt)
        
        url = f"https://image.pollinations.ai/prompt/{encoded_prompt}?width=800&height=600&nologo=true"
        
        print(f"Requesting image from: {url[:50]}...") # Log partial URL

        for attempt in range(3):
            try:
                response = requests.get(url, timeout=30)
                if response.status_code == 200:
                    with open(output_path, "wb") as f:
                        f.write(response.content)
                    print(f"Pollinations image saved to {output_path}")
                    return output_path
                else:
                    print(f"Attempt {attempt+1} failed: Status {response.status_code}")
            except Exception as e:
                print(f"Attempt {attempt+1} error: {e}")
            
            time.sleep(2) # Wait before retry

        print("Falling back to local placeholder image.")
        return self._create_placeholder_image(prompt, output_path)

    def _create_placeholder_image(self, prompt, output_path):
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
