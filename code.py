import io
import os
import requests
import shutil
import uvicorn
from fastapi import FastAPI, Request, File, UploadFile
from fastapi.responses import HTMLResponse, RedirectResponse, FileResponse,StreamingResponse
from pydantic.main import BaseModel
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

try:
    app = FastAPI()
    app.router.redirect_slashes = False

    class id(BaseModel):
        UserEmail : str
        UserPwd : str

    class sign_up(BaseModel):
        UserEmail : str
        UserPwd : str
        Username : str
    @app.post('/upload')
    async def upload(file: UploadFile = File(...)):
        with open('test.mp4', 'wb') as buffer:
            shutil.copyfileobj(file.file, buffer)
            exec(open("video_cut.py").read('--input_file test.mp4 --output_file output.mp4'))
        return "ok"

    @app.get("/download")
    async def main():
        file_path = 'output.mp4'
        return FileResponse(file_path, media_type='video/mp4', filename='divised_file.mp4')

    @app.post("/sign_up")
    async def sign_up(id : sign_up):
        print(id.UserEmail,id.UserPwd,id.UserName)
        return "success sign up"


    @app.post("/sign_in")
    async def sign_up(id: id):
        print(id.UserEmail, id.UserPwd)
        return "success sign up"

    if __name__ == "__main__":
        #172.31.12.238
        uvicorn.run(app, host='0.0.0.0', port=80, debug='true')

except KeyboardInterrupt:
    print("down")