from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def get_root():
    return {"hello","world"}

# 执行
# uvicorn main:app --reload

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app="main:app",host="127.0.0.1",port=8000,reload=True,workers=3)

