# 2024 공주대학교 생성형 AI 대회

> 텍스트 입력으로부터 대전 관광 홍보 영상(GIF)을 자동 생성하는 파이프라인

---

## 처리 파이프라인

```
사용자 입력 (제목, 해시태그, 게시글)
    │
    ▼
[1] 텍스트 → 이미지 변환 (utils.py)
    │
    ▼
[2] OCR + GPT-4o-mini 로 구조화 (ocr/recog.py)
    │
    ▼
[3] GPT-4o-mini 로 대전 관광지 3곳 추천 (pipe.py)
    │
    ▼
[4] Bing 이미지 검색으로 장소 사진 수집 (crawl/crawling.py)
    │
    ▼
[5] I2VGen-XL 로 이미지 → 영상(GIF) 생성 (img_video/video.py)
    │   └── 한국어 프롬프트 → Iris-7B로 영어 번역 (img_video/trans.py)
    │
    ▼
출력: GIF 파일 + 추천 장소 정보
```

---

## 프로젝트 구조

```
pipeline/                  # 메인 파이프라인 코드
├── main.py                # FastAPI 서버 (엔트리포인트)
├── pipe.py                # 파이프라인 오케스트레이터
├── utils.py               # 텍스트-이미지 변환
├── requirements.txt       # Python 의존성
├── ocr/
│   └── recog.py           # EasyOCR + GPT 텍스트 추출
├── crawl/
│   └── crawling.py        # Bing 이미지 검색/다운로드
└── img_video/
    ├── trans.py            # 한영 번역 (Iris-7B)
    └── video.py            # I2VGen-XL 영상 생성
결과물_GIF/                 # 생성된 GIF 결과물 샘플
```

---

## 실행 방법

### 1. 환경 변수 설정

```bash
export OPENAI_API_KEY="your-openai-api-key"
```

### 2. 의존성 설치

```bash
cd pipeline
pip install -r requirements.txt
```

### 3-A. 직접 실행 (CLI)

```bash
cd pipeline
python pipe.py
```

### 3-B. FastAPI 서버 실행

```bash
cd pipeline
uvicorn main:app --host 0.0.0.0 --port 8000
```

API 엔드포인트:
- `POST /generate` — 영상 생성 (title, hashtag, content, style_prompt)
- `GET /health` — 서버 상태 확인

---

## 결과물

### Moving Robot
![moving robot video__80](https://github.com/user-attachments/assets/146fee19-46e6-4b78-977c-af0989a15d80)

### Moving Fish
![video of moving fish__26](https://github.com/user-attachments/assets/e86019b2-b843-428d-98ab-0f8b2e6b6d0d)

### Paper Airplane
![the sky is a paper airplane__25](https://github.com/user-attachments/assets/60c0215e-8d98-4e7f-9b52-3f4af609abd2)

> 추가 결과물은 `결과물_GIF/` 폴더를 참고하세요.

---

## 참고 자료

- [HuggingFace - Text/Image to Video](https://huggingface.co/docs/diffusers/main/en/using-diffusers/text-img2vid)
- [I2VGen-XL (ali-vilab)](https://huggingface.co/ali-vilab/i2vgen-xl)
- [Iris-7B 번역 모델](https://huggingface.co/davidkim205/iris-7b)
