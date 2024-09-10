import easyocr 
import openai
import sys 
sys.path.append("/root/naver/members/soo/pipeline2")
from clova_ocr import ocr_clova


openai.api_key = 'sk-None-NCV6Mi3LXlruoTpnq8ADT3BlbkFJXGyWTSQdVhcy0SFiNpAb'

reader = easyocr.Reader(['ko','en']) # this needs to run only once to load the model into memory

def chat_gpt(contents,prompt):

    conversation=[]
    conversation.append({"role": "system", "content": contents})
    conversation.append({"role": "user", "content": prompt})
    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=conversation
    )
    answer = response.choices[0].message.content.strip()
    

    return answer


def ocr_img(path):

    result=ocr_clova(path)
    #result = reader.readtext(path,detail=0)
    conversation=f"""리스트안의 요소중에서 제목, 해시태그, 게시글을 추출하고 

    정리하시오, 정리는 '제목: , 해시태그: , 게시글:   ' 왼쪽 탬플릿의 빈칸을 채우는 식으로 한다. 

    제목안에는 숫자가 들어가지 않는다. 제목안에는 대전과 관련된 장소가 들어가야 하며 대전 내 어느구에 있는지 까지 적으시오.
    다음은 리스트 이다. 

    {result}

    """

    result2=chat_gpt("당신은 한국어를 잘하는 모델입니다",conversation)

    return result2

