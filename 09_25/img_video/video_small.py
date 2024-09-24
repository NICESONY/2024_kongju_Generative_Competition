import torch
from diffusers import I2VGenXLPipeline
from diffusers.utils import export_to_gif, load_image
from .trans import translate_ko2en
import langdetect
import random
from PIL import Image 
import os 

from diffusers import DiffusionPipeline
# help(DiffusionPipeline)



# from diffusers import StableVideoDiffusionPipeline
# help(StableVideoDiffusionPipeline)



## 아니 그럼 text2video엿던거야??


# pipeline = DiffusionPipeline.from_pretrained("stabilityai/stable-video-diffusion-img2vid-xt")


pipeline = DiffusionPipeline.from_pretrained("damo-vilab/text-to-video-ms-1.7b", torch_dtype=torch.float16, variant="fp16")


# prompt = "Astronaut in a jungle, cold color palette, muted colors, detailed, 8k"


# image = pipeline(prompt).images[0]

pipeline.enable_model_cpu_offload()
generator = torch.manual_seed(0)


def vid_generate(recommended_img:str, user_prompt:str, steps, scale,user):
    #recommend img is path
    path = recommended_img
    print(path)
    random_number = int(random.random()*100)
    prompt = user_prompt
    orig_size = Image.open(recommended_img).size


    if orig_size[1]<orig_size[0]:
        orig_size2=(orig_size[1],orig_size[0])
        image = load_image(path).convert("RGB")
        image=image.resize(orig_size2)
    else:
        image = load_image(path).convert("RGB")

    if langdetect.detect(prompt)=="ko":

        prompt=translate_ko2en(prompt)
        prompt=prompt.split(".")[0]
        prompt=prompt.lower()
        print('01')
        
    # else:
        
    #     prompt=prompt.lower()
        
    print('02')
        
    negative_prompt = """Distorted, gray, discontinuous, Ugly, 
    blurry, low resolution, motionless, 
    static, disfigured, disconnected limbs, 
    Ugly faces, incomplete arms"""
    print('03')
        


    image = pipeline(
        prompt = prompt,
        image = image,
        num_inference_steps=steps, #95
        negative_prompt=negative_prompt,
        guidance_scale=scale,
        # 9.0 , 1.0
        generator=generator
    ).images[0]

    print('04')
        
    name=path.split(".")[0]
    if name.find("/")>-1:
        name=name.split("/")[-2]
        
        
    os.makedirs(f"{user}/gifs",exist_ok=True)
    export_to_gif(image, f"{user}/gifs/{prompt}__{name}__{random_number}.gif")
    print("Gif Saved")
    print('05')
        
    return f"{user}/gifs/{prompt}__{name}__{random_number}.gif"



# output_path = vid_generate("path/to/image.jpg", "미래 도시 풍경", 95, 9.0, "username")
# print(f"GIF 저장 경로: {output_path}")
