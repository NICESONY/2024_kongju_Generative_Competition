from fastapi import FastAPI
app = FastAPI()

# 다른 파일 불러오기
from fastapi.staticfiles import StaticFiles

#fast_api test
## HTML 파일을 띄우고 싶을때 사용

from fastapi.responses import FileResponse



app.mount("/css", StaticFiles(directory="css"), name="css")
app.mount("/js", StaticFiles(directory="js"), name="js")
app.mount("/icon", StaticFiles(directory="icon"), name="icon")
app.mount("/Logo", StaticFiles(directory="Logo"), name="Logo")
app.mount("/assets", StaticFiles(directory="assets"), name="assets")





# 1.HOME
@app.get("/")
def HOME():
   return FileResponse("index.html")



# 2. 추천
@app.get("/recomedation")
def recomedation():
   return FileResponse("recomedation.html")



# 3. 기록 배경(완료)
@app.get("/recordhome")
def recordhome():
   return FileResponse("recordhome.html")



# 4. 기록 디테일(완료)
@app.get("/record_update")
def record_update():
   return FileResponse("record_update.html")



# 5. 기록 업데이트(완료)
@app.get("/Writingrecord")
def Writingrecord():
   return FileResponse("Writingrecord.html")


# 6. 티셋(1)
@app.get("/ticket")
def resume():
   return FileResponse("ticket.html")


# 7. 티셋(2)
@app.get("/ticketsave")
def resume():
   return FileResponse("ticketsave.html")




# 8. 마이 페이지(사진 추가)
@app.get("/mypage")
def resume():
   return FileResponse("mypage.html")







