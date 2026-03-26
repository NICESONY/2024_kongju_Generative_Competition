import torch
from diffusers import I2VGenXLPipeline
from diffusers.utils import export_to_gif, load_image
from .trans import translate_ko2en
import langdetect
import random
from PIL import Image
import os

pipeline = I2VGenXLPipeline.from_pretrained(
    "ali-vilab/i2vgen-xl", torch_dtype=torch.float16, variant="fp16"
)
pipeline.enable_model_cpu_offload()
generator = torch.manual_seed(0)

NEGATIVE_PROMPT = (
    "Distorted, gray, discontinuous, Ugly, blurry, low resolution, "
    "motionless, static, disfigured, disconnected limbs, "
    "Ugly faces, incomplete arms"
)


def vid_generate(recommended_img, user_prompt, steps, scale, output_dir):
    random_number = int(random.random() * 100)
    prompt = user_prompt
    orig_size = Image.open(recommended_img).size

    if orig_size[1] < orig_size[0]:
        swapped = (orig_size[1], orig_size[0])
        image = load_image(recommended_img).convert("RGB").resize(swapped)
    else:
        image = load_image(recommended_img).convert("RGB")

    if langdetect.detect(prompt) == "ko":
        prompt = translate_ko2en(prompt).split(".")[0].lower()
    else:
        prompt = prompt.lower()

    frames = pipeline(
        prompt=prompt,
        image=image,
        num_inference_steps=steps,
        negative_prompt=NEGATIVE_PROMPT,
        guidance_scale=scale,
        generator=generator,
    ).frames[0]

    name = os.path.splitext(os.path.basename(recommended_img))[0]
    parent = os.path.basename(os.path.dirname(recommended_img))
    gif_dir = os.path.join(output_dir, "gifs")
    os.makedirs(gif_dir, exist_ok=True)

    gif_path = os.path.join(gif_dir, f"{prompt}__{parent}__{random_number}.gif")
    export_to_gif(frames, gif_path)
    print(f"GIF 저장 완료: {gif_path}")
    return gif_path
