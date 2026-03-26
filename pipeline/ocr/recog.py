import easyocr
from openai import OpenAI
import os

client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))
reader = easyocr.Reader(["ko", "en"])


def chat_gpt(system_msg, user_msg):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": system_msg},
            {"role": "user", "content": user_msg},
        ],
    )
    return response.choices[0].message.content.strip()


def ocr_img(path):
    result = reader.readtext(path, detail=0)

    prompt = f"""리스트안의 요소중에서 제목, 해시태그, 게시글을 추출하고
    정리하시오, 정리는 '제목: , 해시태그: , 게시글: ' 왼쪽 탬플릿의 빈칸을 채우는 식으로 한다.
    제목안에는 숫자가 들어가지 않는다. 제목안에는 대전과 관련된 장소가 들어가야 하며 대전 내 어느구에 있는지 까지 적으시오.
    다음은 리스트 이다.

    {result}"""

    return chat_gpt("당신은 한국어를 잘하는 모델입니다", prompt)
