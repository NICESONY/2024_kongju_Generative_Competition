from openai import OpenAI
from ocr.recog import ocr_img
from crawl.crawling import retrieve, extract_locations
from img_video.video import vid_generate
from utils import create_text_image
import os
import random

client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT_DIR = os.path.join(BASE_DIR, "outputs")


def chat_gpt(system_msg, user_msg):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": system_msg},
            {"role": "user", "content": user_msg},
        ],
    )
    return response.choices[0].message.content.strip()


def recommending(script):
    prompt = f"""
    추천 장소: 갤러리 청람
    주소: 대전광역시 서구 만년동 393
    특징: 좋다

    ==> 위와 같은 템플릿 형태로 제목: , 해시태그: , 게시물: 이 적혀있는 아래 문서를 읽고 문서내 분위기와
    내용을 파악하여 아래 문서를 작성한 유저가 갈만한 실제 대전광역시와 관련된 장소(음식점이나 관광지)를 3곳을 추천하시오,
    추천된 장소와 아래 문서내의 제목에 있는 장소와 같아서는 안된다. 그리고 출력은 추천 장소이름과 주소만 하도록한다.
    추천한 장소의 특징도 짧은 1줄로 간략히 설명한다. 해당 추천된 장소는 실제로 대전에 있는곳이어야한다. 주소도
    실제로 존재하는 대전 내의 주소여야한다. 추천장소기준은 아래 문서의 제목에 해당 하는 장소를 유저가 떠난 후에 바로 갈만한곳으로 추천하시오.
    음식점과 음식점아닌 관광지 등 다양히 추천하시오. 추천장소명에는 대전 이라는 단어가 있도록해야하고 그장소는
    실제로 대전에 있는 장소여야한다.

    다음은 아래 문서 내용이다.

    --->

    {script}
    """
    return chat_gpt("당신은 한국어를 잘하는 모델입니다", prompt)


def main_pipe(user_name="user", title=None, hashtag=None, content=None, input_prompt="관광 홍보 영상"):
    # 1. 텍스트 이미지 생성
    input_dir = os.path.join(BASE_DIR, "user_input")
    os.makedirs(input_dir, exist_ok=True)
    input_path = os.path.join(input_dir, "input.png")
    create_text_image(title, hashtag, content, save_path=input_path)

    # 2. 사용자 출력 디렉토리 생성
    num = int(random.random() * 100)
    user_dir = os.path.join(OUTPUT_DIR, user_name)
    if os.path.exists(user_dir):
        user_dir = f"{user_dir}_{num}"
    os.makedirs(user_dir, exist_ok=True)

    # 3. 프롬프트 마침표 처리
    if "." not in input_prompt:
        input_prompt += "."

    # 4. OCR로 텍스트 추출
    texts = ocr_img(input_path)

    # 5. GPT로 대전 장소 추천
    texts2 = recommending(texts)

    # 6. 추천 장소 파싱
    locations, tmis = extract_locations(texts2)

    # 7. 로그 저장
    name = os.path.basename(user_dir)
    log_path = os.path.join(user_dir, f"log_{name}.txt")
    with open(log_path, "w", encoding="utf-8") as log:
        log.write(f"{name} 의 게시글\n\n{texts}\n\n")
        log.write(f"{name} 위한 추천장소들\n\n{locations}\n\n")

    # 8. 첫 번째 추천 장소 이미지 검색 + 영상 생성
    print(f"추천 장소: {locations[0]}, 특징: {tmis[0]}")
    recommend_img_path = retrieve(locations[0], user_dir)

    steps = 5
    scale = 9.0
    gif_path = vid_generate(recommend_img_path, input_prompt, steps, scale, user_dir)

    # 9. 입력 이미지 정리
    if os.path.exists(input_path):
        os.remove(input_path)

    return gif_path, recommend_img_path, locations[0], tmis[0]


if __name__ == "__main__":
    gif_path, img_path, rec_title, rec_tmi = main_pipe(
        user_name="user_test",
        title="대전 카페 1호점",
        hashtag="카페,대전,분위기",
        content="대전 서구에 있는 분위기 좋은 카페를 다녀왔습니다.",
        input_prompt="관광 홍보위한 동영상",
    )
    print(f"GIF: {gif_path}")
    print(f"추천 장소: {rec_title}")
    print(f"특징: {rec_tmi}")
