from PIL import Image, ImageDraw
import os

def create_gold_orchids_placeholder():
    # Image size
    width, height = 1920, 1080
    background_color = (0, 0, 0)  # Black
    gold_color = (255, 215, 0)    # Gold
    
    img = Image.new('RGB', (width, height), color=background_color)
    draw = ImageDraw.Draw(img)
    
    # Draw some "orchid" shapes (circles/ellipses for now)
    # Center
    cx, cy = width // 2, height // 2
    
    # Draw simple flower patterns
    for i in range(5):
        offset_x = (i - 2) * 300
        draw.ellipse([cx + offset_x - 100, cy - 100, cx + offset_x + 100, cy + 100], outline=gold_color, width=5)
        draw.ellipse([cx + offset_x - 50, cy - 150, cx + offset_x + 50, cy + 150], outline=gold_color, width=5)
        draw.ellipse([cx + offset_x - 150, cy - 50, cx + offset_x + 150, cy + 50], outline=gold_color, width=5)
    
    # Draw text
    draw.text((50, 50), "Gold Orchids Placeholder", fill=gold_color)
    
    # Save
    output_path = os.path.join(os.getcwd(), 'media', 'gold_orchids_wallpaper.png')
    img.save(output_path)
    print(f"Created placeholder at {output_path}")

if __name__ == "__main__":
    create_gold_orchids_placeholder()
