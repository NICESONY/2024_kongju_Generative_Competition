#  chat gpt 4o API 사용


import os
import openai




os.environ["OPENAI_API_KEY"] = "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"



client = openai.OpenAI()

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "나의 학습자료 검색을 위한 키워드 제공해줘."},
        {"role": "user", "content": "나는 딥러닝 관련 영상을 만들고 싶어"}
    ]
)

print("Assistant: " + response.choices[0].message.content)





## 추가적으로 영상의 제목 + 영상의 분위기 + 영상에서 등장인물의 행동 묘사 == 관련 프롬포트를 넣고 해당 관련해서 나온 답변을  -> 영상 생성 AI에 넣어주는거지!! 어때?? 그럼 더 질 좋은 영상이 나오지 않을까?

## 선결제를 먼저 해야함 