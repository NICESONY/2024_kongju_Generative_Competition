from fastapi import FastAPI, Form
from fastapi.responses import JSONResponse
from pipe import main_pipe

app = FastAPI(title="대전 관광 홍보 영상 생성기")


@app.post("/generate")
async def generate_video(
    user_name: str = Form(default="user"),
    title: str = Form(...),
    hashtag: str = Form(...),
    content: str = Form(...),
    style_prompt: str = Form(default="관광 홍보 영상"),
):
    gif_path, img_path, rec_title, rec_tmi = main_pipe(
        user_name=user_name,
        title=title,
        hashtag=hashtag,
        content=content,
        input_prompt=style_prompt,
    )
    return JSONResponse(
        content={
            "gif_path": gif_path,
            "image_path": img_path,
            "recommended_place": rec_title,
            "feature": rec_tmi,
        }
    )


@app.get("/health")
async def health():
    return {"status": "ok"}
