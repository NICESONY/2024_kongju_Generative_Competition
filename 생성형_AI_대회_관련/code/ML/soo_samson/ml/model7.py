#import gradio.helpers
import torch


from diffusers import StableVideoDiffusionPipeline
from diffusers.utils import load_image, export_to_video

from huggingface_hub import hf_hub_download
#gradio.helpers.CACHED_FOLDER = '/data/cache'

pipe = StableVideoDiffusionPipeline.from_pretrained(
    "multimodalart/stable-video-diffusion", torch_dtype=torch.float16, variant="fp16"
)
pipe.to("cuda")

