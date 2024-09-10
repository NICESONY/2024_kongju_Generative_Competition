from fastapi import FastAPI, Request, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import time

app = FastAPI()

# Static file mounting
app.mount("/css", StaticFiles(directory="frontend/css"), name="css")
app.mount("/icon", StaticFiles(directory="frontend/icon"), name="icon")

@app.get("/")
def index():
    return FileResponse("frontend/Writingrecord.html")

def take_screenshot(url, output_path):
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--window-size=1920,1080")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    
    driver.get(url)
    time.sleep(2)  # 페이지가 완전히 로드될 때까지 대기
    driver.save_screenshot(output_path)
  

@app.post("/capture_screenshot")
async def capture_screenshot(request: Request):#http://127.0.0.1:8015/
    
        url = str(request.url_for('index')).replace('http://', 'https://')  # 필요한 경우 HTTP를 HTTPS로 변경
        url="http://127.0.0.1:8015"
        output_path = "/root/naver/members/soo/pipeline/user_input/input.png"
        take_screenshot(url, output_path)
        return {"message": "스크린샷이 성공적으로 저장되었습니다."}
    
