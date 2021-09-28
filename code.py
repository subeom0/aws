import uvicorn
from fastapi import FastAPI
from pydantic.main import BaseModel

try:
    app = FastAPI()
    app.router.redirect_slashes = False

    class id(BaseModel):
        userID : str
        userPassword : str

    class sign_up(BaseModel):
        UserEmail : str
        UserPwd : str
        Username : str


    @app.post("/sign_up")
    async def sign_up(id : sign_up):
        print(id.UserEmail,id.UserPwd,id.UserName)
        return "success sign up"

    @app.post("/sign_in")
    async def sign_up(id: id):
        print(id.userID, id.userPassword)
        return "success sign up"

    if __name__ == "__main__":
        #172.31.12.238
        uvicorn.run(app, host='172.26.0.86', port=8080, debug='true')

except KeyboardInterrupt:
    print("down")