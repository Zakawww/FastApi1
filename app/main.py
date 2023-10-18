import uvicorn
from fastapi import FastAPI
from fastapi.responses import FileResponse

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}
    # return FileResponse('html/index.html')


if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=80)
