## 로직 아이디어 : 현재 생성은 이클립스를 이용해서 백앤드와 프론트 앤드 작업 + 이후에는 AWS를 이용해서 데이터베이스 + 스토리지 + 서버 이용해서 VSCODE 에서 작업한 모델을 연결하는거지 백앤드에서 작성하면 -> DB로 들어가고 -> 이후 DB에서 값 받아서 모델의 입력을 주면 영상을 만들고 -> 홈페이지에 주던가 또는 VSCODE에서 홈페이지로 바로 다운로드 가능하게 만들기???





#  개발 로직

# RAG 사용해서 추가적으로 할 수 있어야할 듯

## 여기서 먼저 생성형 모델(chat gpt 4o mini)들 불러와 여기서 프롬포트 입력 -> 입력에 맞게 이미지 검색 - > 이후 생성형 모델(gen model)을 이용해서 이미지 생성



### ==========================================================================

# backend 연결 후 

## 프롬포트 입력 -> DB에 넣어주기 -> DB에서 값 읽어오기 -> 해당 입력을 받아서 영상 생성


## 현재 상황

## 이미지로 부터 영상 생성하는 모델 저장해야함 + key값 받아야함




## ==========================================================================================



### text 입력하면 그거와 관련된 영상을 만들어주는거임?? -> 왜 필요한데?? -> 우리는 이제 유트브 or 인스타의 숏츠에 중독이 되었다고 할 수 있기 때문에 이런 단기적인 영상이 몰입도를 가져오므로 교욱관련 이미지도 변화가 필요함 -> 이미지를 영상으로 만들어서 교육을 질 향상 