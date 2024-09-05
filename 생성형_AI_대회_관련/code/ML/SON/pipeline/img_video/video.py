import torch
from diffusers import I2VGenXLPipeline
from diffusers.utils import export_to_gif, load_image
from .trans import translate_ko2en
import langdetect
import random
from PIL import Image 
import os 


pipeline = I2VGenXLPipeline.from_pretrained("ali-vilab/i2vgen-xl", torch_dtype=torch.float16, variant="fp16")
pipeline.enable_model_cpu_offload()
generator = torch.manual_seed(0)


def vid_generate(recommended_img:str,user_prompt:str,steps,scale,user):
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
        
        
    else:
        
        prompt=prompt.lower()
        

    negative_prompt = """Distorted, gray, discontinuous, Ugly, 
    blurry, low resolution, motionless, 
    static, disfigured, disconnected limbs, 
    Ugly faces, incomplete arms"""

    frames = pipeline(
        prompt = prompt,
        image = image,
        num_inference_steps=steps, #95
        negative_prompt=negative_prompt,
        guidance_scale=scale,
        # 9.0 , 1.0
        generator=generator
    ).frames[0]


    name=path.split(".")[0]
    if name.find("/")>-1:
        name=name.split("/")[-2]
        
        
    os.makedirs(f"{user}/gifs",exist_ok=True)
    export_to_gif(frames, f"{user}/gifs/{prompt}__{name}__{random_number}.gif")
    print("Gif Saved")
    
    return f"{user}/gifs/{prompt}__{name}__{random_number}.gif"