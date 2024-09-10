import gradio as gr
from PIL import Image, ImageDraw, ImageFont
from pipe import main_pipe

def create_text_image(title, hash_tag, post, save_path):
    hash_tag_list=hash_tag.split(",")
    hash_tag_list=list(map(lambda x:"#"+x,hash_tag_list))
    hash_tag=",".join(hash_tag_list)

    width, height = 800, 400
    background_color = (255, 255, 255)
    text_color = (0, 0, 0)

    image = Image.new('RGB', (width, height), background_color)
    draw = ImageDraw.Draw(image)
   
    font_path = "/root/naver/members/soo/pipeline2/Nanum.ttf"
    font_size = 30
    font = ImageFont.truetype(font_path, font_size)
    
    combined_text = f"제목: {title}\n\n해쉬태그: {hash_tag}\n\n게시글: {post}"
    
    bbox = draw.textbbox((0, 0), combined_text, font=font)
    text_width, text_height = bbox[2] - bbox[0], bbox[3] - bbox[1]
    x = (width - text_width) / 2
    y = (height - text_height) / 2
    
    draw.multiline_text((x, y), combined_text, fill=text_color, font=font, align="center")
    
    image.save(save_path)

def final(user_name, video_style, title, hash_tag, post, img=None):
    save_path = "/root/naver/members/soo/pipeline2/user_input/gradio_input.png"
    
    if img is not None:
        img.save("/root/naver/members/soo/pipeline2/user_input/gradio_input2.png")
    else:
        create_text_image(title, hash_tag, post, save_path)
    
    out, out2, location = main_pipe(user_name, save_path, video_style)
    return out, out2, location

def interface():
    with gr.Blocks() as demo:
        with gr.Row():
            with gr.Column(scale=1):
                img = gr.Image(label="이미지", type="pil",scale=1)
            with gr.Column(scale=3):
                title = gr.Textbox(label="제목", lines=1,scale=1)
                hash_tag = gr.Textbox(label="해시태그 ('행복, 즐거움' 이런식으로 ',' 은 쓰고 '#' 은 안쓰면서 쓰시오)", lines=1,scale=1)
                post = gr.Textbox(label="게시물", lines=3,scale=1)
                user_name = gr.Textbox(label="아이디",  lines=1,scale=1)
                video_style = gr.Textbox(label="비디오 스타일",  lines=1,scale=1)

        with gr.Row():
            with gr.Column(scale=1): 
                output_name = gr.Textbox(label="추천된 장소 이름", interactive=False,scale=3)
            with gr.Column(scale=2): 
                image_output = gr.Image(label="추천된 장소 사진",scale=3)
            with gr.Column(scale=2):
                video_output = gr.Video(label="추천된 장소 영상", loop=True,scale=3)

        with gr.Row():
            btn_submit = gr.Button("장소를 추천해드리겠습니다", scale=1)
            btn_submit.click(final, [user_name, video_style, title, hash_tag, post, img], [video_output, image_output, output_name])

    return demo

demo = interface()
demo.launch()
