from fastapi import FastAPI
app = FastAPI()

from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse




app.mount("/css", StaticFiles(directory="css"), name="css")
app.mount("/js", StaticFiles(directory="js"), name="js")
app.mount("/icon", StaticFiles(directory="icon"), name="icon")
app.mount("/Logo", StaticFiles(directory="Logo"), name="Logo")
app.mount("/illust", StaticFiles(directory="illust"), name="illust")
app.mount("/photo", StaticFiles(directory="photo"), name="photo")
app.mount("/assets", StaticFiles(directory="assets"), name="assets")




@app.get("/")
def record():
   return FileResponse("create_record.html")

