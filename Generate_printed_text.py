from PIL import Image, ImageDraw, ImageFont
import arabic_reshaper

def generate_arabic_text_image(text, font_path, image_size=(800, 100), font_size=40, output_path="output.png"):
    # Only reshape the text, don't reorder
    reshaped_text = arabic_reshaper.reshape(text)
    
    # Create image canvas
    img = Image.new("RGB", image_size, "white")
    draw = ImageDraw.Draw(img)
    
    # Load font
    font = ImageFont.truetype(font_path, font_size)
    
    # Center text
    bbox = font.getbbox(reshaped_text)
    text_width, text_height = bbox[2] - bbox[0], bbox[3] - bbox[1]
    text_x = (image_size[0] - text_width) // 2
    text_y = (image_size[1] - text_height) // 2
    
    # Draw text
    draw.text((text_x, text_y), reshaped_text, fill="black", font=font)
    
    img.save(output_path)
    print(f"Image saved to {output_path}")

# Example usage
text = "السلام عليكم و رحمة الله و بركاته"
font_path = "/content/Amiri-Regular.ttf"
generate_arabic_text_image(text, font_path)