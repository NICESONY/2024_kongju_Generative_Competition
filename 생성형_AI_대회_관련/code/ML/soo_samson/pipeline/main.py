from fastapi import FastAPI, File, UploadFile, Form
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.staticfiles import StaticFiles
import os
import shutil

app = FastAPI()

# Define the path to the frontend folder containing static assets
frontend_path = "/root/naver/members/soo/pipeline/frontend"

# Mount the static files for css, js, and icon
app.mount("/css", StaticFiles(directory=os.path.join(frontend_path, "css")), name="css")
app.mount("/js", StaticFiles(directory=os.path.join(frontend_path, "js")), name="js")
app.mount("/icon", StaticFiles(directory=os.path.join(frontend_path, "icon")), name="icon")

# Serve the HTML page
@app.get("/", response_class=HTMLResponse)
async def get_writing_record():
    with open(os.path.join(frontend_path, "Writingrecord.html"), "r", encoding="utf-8") as file:
        html_content = file.read()
    return HTMLResponse(content=html_content, status_code=200)

# Endpoint for handling the data submission
@app.post("/submit/")
async def submit_record(
    title: str = Form(...),
    hashtag: str = Form(...),
    content: str = Form(...),
):
    record_path = "/root/naver/members/soo/pipeline/records2.txt"
    with open(record_path, "a", encoding="utf-8") as file:
        file.write(f"제목: {title}, 해쉬태그: {hashtag}, 게시글: {content}\n")
    return {"message": "Record saved successfully"}


