#  chat gpt 4o API 사용


import os
os.environ["OPENAI_API_KEY"] = "<your OpenAI API key>"



import openai

client = openai.OpenAI()

response = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role": "system", "content": "나의 학습자료 검색을 위한 키워드 제공해줘."},
        {"role": "user", "content": "나는 딥러닝 관련 영상을 만들고 싶어"}
    ]
)

print("Assistant: " + response.choices[0].message.content)





