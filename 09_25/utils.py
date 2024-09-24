from PIL import Image, ImageDraw, ImageFont
import os 



def create_text_image(title, hash_tag, post, save_path="/media/samson/DATA2/dev/workspace/2024_kongju_Generative_Competition/생성형_AI_대회_관련/code/ML/soo_samson/pipeline/user_input/input.png"):
    
    hash_tag_list=hash_tag.split(",")
    hash_tag_list=list(map(lambda x:"#"+x,hash_tag_list))
    hash_tag=",".join(hash_tag_list)

    width, height = 800, 400
    background_color = (255, 255, 255)
    text_color = (0, 0, 0)

    image = Image.new('RGB', (width, height), background_color)
    draw = ImageDraw.Draw(image)
   
    font_path = "/media/samson/DATA2/dev/workspace/2024_kongju_Generative_Competition/생성형_AI_대회_관련/code/ML/soo_samson/pipeline/Nanum.ttf"
    font_size = 30
    font = ImageFont.truetype(font_path, font_size)
    
    combined_text = f"제목: {title}\n\n해쉬태그: {hash_tag}\n\n게시글: {post}"
    
    bbox = draw.textbbox((0, 0), combined_text, font=font)
    text_width, text_height = bbox[2] - bbox[0], bbox[3] - bbox[1]
    x = (width - text_width) / 2
    y = (height - text_height) / 2
    
    draw.multiline_text((x, y), combined_text, fill=text_color, font=font, align="center")
   
    if os.path.exists(save_path):
        pass
    else:
        image.save(save_path)