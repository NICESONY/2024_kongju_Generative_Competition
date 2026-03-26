from PIL import Image, ImageDraw, ImageFont
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DEFAULT_FONT_PATH = os.path.join(BASE_DIR, "Nanum.ttf")


def create_text_image(title, hash_tag, post, save_path=None, font_path=None):
    if save_path is None:
        save_path = os.path.join(BASE_DIR, "user_input", "input.png")
    if font_path is None:
        font_path = DEFAULT_FONT_PATH

    hash_tag_list = ["#" + tag.strip() for tag in hash_tag.split(",")]
    hash_tag_str = ", ".join(hash_tag_list)

    width, height = 800, 400
    image = Image.new("RGB", (width, height), (255, 255, 255))
    draw = ImageDraw.Draw(image)

    try:
        font = ImageFont.truetype(font_path, 30)
    except OSError:
        font = ImageFont.load_default()

    combined_text = f"제목: {title}\n\n해쉬태그: {hash_tag_str}\n\n게시글: {post}"

    bbox = draw.textbbox((0, 0), combined_text, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]
    x = (width - text_width) / 2
    y = (height - text_height) / 2

    draw.multiline_text((x, y), combined_text, fill=(0, 0, 0), font=font, align="center")

    os.makedirs(os.path.dirname(save_path), exist_ok=True)
    image.save(save_path)
    return save_path
