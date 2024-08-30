import torch
from diffusers import I2VGenXLPipeline
from diffusers.utils import export_to_gif, load_image
from model6 import translate_ko2en
import langdetect


path="naver_ex2.jpg"
random_number=1
prompt = "사람들이 의자에 앉아있다."

image = load_image(path).convert("RGB")
#raise ValueError("이미지 크기가 작습니다")
if image.size[0]<1000 or image.size[1]<700:
    raise ValueError("이미지 크기가 작습니다")
else:
    pass 

"""

따뜻한 분위기의 / 차가운 분위기의 / 사람이 북적이는 / 하늘이 맑은( 야외 ) / 
깔끔해보이는 / 고양이가 있는 / 맛있어보이는 / (음식 사진일 경우 ) 음식이 푸짐한 

"""

"""

2. 이미지와 텍스트 넣어서 텍스트 내용에 맞추어서 이미지 관련 비디오 만드는 모델
:소상공인들이 어렵지 않게 홍보용 장소 사진을 생성형 Ai를 통해 꾸미고( 텍스트 내용에 맞춰서 이미지 변경 ) 
+ 저희 서비스 타겟 ( 2030세대 )의 이목을 끌기 위해 비디오로 변환까지 필요하기 때문에 필요합니다.

3. 한국어 -> 영어, 영어 -> 한국어 
: 프롬포트를 넣을 때 소상공인( 장소의 주인 )이 프롬포트를 작성하게 될 것 같은데 타겟인 소상공인이 한국인인 점, 
저희 해커톤 가산점 부분이 한글, 한국의 정서 살리기인 점을 고려했을 때 번역해주는 모델이 필요할 것 같습니다. 
( 소상공인들이 서비스에서 영어로  프롬포트를 입력하게 할 순 없을 것 같습니다. ) 

"""


if langdetect.detect(prompt)=="ko":

    prompt=translate_ko2en(prompt)
    prompt=prompt.split(".")[0]
    print(prompt)
    
else:
    pass

negative_prompt = """Distorted, gray, discontinuous, Ugly, 
blurry, low resolution, motionless, 
static, disfigured, disconnected limbs, 
Ugly faces, incomplete arms"""

pipeline = I2VGenXLPipeline.from_pretrained("ali-vilab/i2vgen-xl", torch_dtype=torch.float16, variant="fp16")
pipeline.enable_model_cpu_offload()

generator = torch.manual_seed(0)

frames = pipeline(
    prompt=prompt,
    image=image,
    num_inference_steps=95,
    negative_prompt=negative_prompt,
    guidance_scale=9.0,
    # 9.0 , 1.0
    generator=generator
).frames[0]

name=path.split(".")[0]
export_to_gif(frames, f"{prompt}__{name}__{random_number}.gif")