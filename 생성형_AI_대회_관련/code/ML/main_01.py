## Image2Video


## stable-video-diffusion-img2vid-xt 저장 후 사용 방법


import torch
from safetensors.torch import load_file

# safetensors 파일 경로
model_path = "./stable-video-diffusion-img2vid-xt/svd_xt.safetensors"


# 모델 가중치 로드
model_state_dict = load_file(model_path)

