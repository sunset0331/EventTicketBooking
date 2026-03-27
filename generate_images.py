#!/usr/bin/env python3
"""
Image Generation Script for GetTicket Events Django Application
Generates placeholder images for the application if they don't exist.
"""

from PIL import Image, ImageDraw, ImageFont
import os
from pathlib import Path

# Define paths
PROJECT_ROOT = Path(__file__).parent
STATIC_IMG_DIR = PROJECT_ROOT / "gestion_even" / "static" / "img"
MEDIA_EVENT_DIR = PROJECT_ROOT / "gestion_even" / "media" / "event_image"

# Ensure directories exist
STATIC_IMG_DIR.mkdir(parents=True, exist_ok=True)
MEDIA_EVENT_DIR.mkdir(parents=True, exist_ok=True)


def create_hero_background():
    """Create a hero background image (1920x1080)"""
    path = STATIC_IMG_DIR / "BG_HERO.jpg"
    if not path.exists():
        img = Image.new('RGB', (1920, 1080), color=(33, 150, 243))
        draw = ImageDraw.Draw(img)
        
        # Add gradient effect manually
        for i in range(1080):
            color = (
                33 + (i * 30 // 1080),
                150 + (i * 50 // 1080),
                243 - (i * 50 // 1080)
            )
            draw.line([(0, i), (1920, i)], fill=color)
        
        # Add text
        try:
            draw.text((960, 500), "GetTicket Events", fill=(255, 255, 255), 
                     anchor="mm", font=None)
        except:
            pass
        
        img.save(path, 'JPEG', quality=85)
        print(f"✓ Created: {path}")
    else:
        print(f"⊙ Already exists: {path}")


def create_logo():
    """Create a logo image (300x100)"""
    path = STATIC_IMG_DIR / "logo.png"
    if not path.exists():
        img = Image.new('RGBA', (300, 100), color=(255, 255, 255, 0))
        draw = ImageDraw.Draw(img)
        
        # Draw background circle
        draw.ellipse([(10, 10), (90, 90)], fill=(33, 150, 243))
        
        # Add text
        try:
            draw.text((150, 50), "GetTicket", fill=(33, 150, 243), anchor="lm")
        except:
            pass
        
        img.save(path, 'PNG')
        print(f"✓ Created: {path}")
    else:
        print(f"⊙ Already exists: {path}")


def create_event_thumbnails():
    """Create event thumbnail images (400x300)"""
    thumbnails = [
        ("ev1.jpg", (220, 53, 69)),      # Red
        ("ev2.jpg", (40, 167, 69)),      # Green
        ("ev3.jpg", (0, 123, 255)),      # Blue
        ("ev4.jpg", (255, 193, 7)),      # Amber
    ]
    
    for filename, color in thumbnails:
        path = STATIC_IMG_DIR / filename
        if not path.exists():
            img = Image.new('RGB', (400, 300), color=color)
            draw = ImageDraw.Draw(img)
            
            # Add gradient
            for i in range(300):
                factor = i / 300
                r = int(color[0] * (1 - factor * 0.3))
                g = int(color[1] * (1 - factor * 0.3))
                b = int(color[2] * (1 - factor * 0.3))
                draw.line([(0, i), (400, i)], fill=(r, g, b))
            
            img.save(path, 'JPEG', quality=85)
            print(f"✓ Created: {path}")
        else:
            print(f"⊙ Already exists: {path}")


def create_icons():
    """Create icon images"""
    icons = {
        "add-to-cart.png": (64, 64, (76, 175, 80)),
        "userProfile.png": (128, 128, (158, 158, 158)),
        "utilisateur.png": (64, 64, (63, 81, 181)),
        "avatar04.png": (64, 64, (244, 67, 54)),
        "avatar5.png": (64, 64, (233, 30, 99)),
    }
    
    for filename, (width, height, color) in icons.items():
        path = STATIC_IMG_DIR / filename
        if not path.exists():
            img = Image.new('RGBA', (width, height), color=(255, 255, 255, 0))
            draw = ImageDraw.Draw(img)
            
            # Draw circle background
            margin = 5
            draw.ellipse(
                [(margin, margin), (width - margin, height - margin)],
                fill=color
            )
            
            img.save(path, 'PNG')
            print(f"✓ Created: {path}")
        else:
            print(f"⊙ Already exists: {path}")


def create_sample_event_images():
    """Create sample event images for media directory"""
    sample_images = {
        "event_music.jpg": (600, 400, (156, 39, 176)),      # Purple
        "event_sports.jpg": (600, 400, (229, 57, 53)),      # Red
        "event_tech.jpg": (600, 400, (25, 103, 210)),       # Blue
        "event_arts.jpg": (600, 400, (251, 140, 0)),        # Orange
    }
    
    for filename, (width, height, color) in sample_images.items():
        path = MEDIA_EVENT_DIR / filename
        # Always regenerate sample images to show latest
        img = Image.new('RGB', (width, height), color=color)
        draw = ImageDraw.Draw(img)
        
        # Add gradient
        for i in range(height):
            factor = i / height
            r = int(color[0] * (1 - factor * 0.2))
            g = int(color[1] * (1 - factor * 0.2))
            b = int(color[2] * (1 - factor * 0.2))
            draw.line([(0, i), (width, i)], fill=(r, g, b))
        
        img.save(path, 'JPEG', quality=85)
        print(f"✓ Generated: {path}")


def main():
    """Main function to generate all images"""
    print("=" * 60)
    print("GetTicket Events - Image Generation Script")
    print("=" * 60)
    print()
    
    print("Generating static images...")
    create_hero_background()
    create_logo()
    create_event_thumbnails()
    create_icons()
    
    print()
    print("Generating sample event images...")
    create_sample_event_images()
    
    print()
    print("=" * 60)
    print("✅ Image generation complete!")
    print("=" * 60)
    print()
    print("📁 Images created in:")
    print(f"   - Static: {STATIC_IMG_DIR}")
    print(f"   - Media:  {MEDIA_EVENT_DIR}")
    print()


if __name__ == "__main__":
    main()
