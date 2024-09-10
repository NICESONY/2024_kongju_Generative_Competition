from fastapi import FastAPI
app = FastAPI()

from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse




app.mount("/frontend/css", StaticFiles(directory="frontend/css"), name="css")
app.mount("/frontend/js", StaticFiles(directory="frontend/js"), name="js")
app.mount("/frontend/assets", StaticFiles(directory="frontend/assets"), name="assets")


@app.get("/")
def index():
   return FileResponse("Writingrecord.html")


# @app.get("/record")
# def record():
#    return FileResponse("frontend/record.html")
