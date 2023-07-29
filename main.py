from fastapi import FastAPI
import uvicorn
import psycopg2

app = FastAPI()

@app.get("/")
async def root():
    onn = psycopg2.connect(database = "customer123",
                        user = "ngoc",
                        password = "CpNdfzvhEQCXVmL8RgssqscmohAKbzGe",
                        host = "dpg-cj26rq98g3n1jki0gkj0-a",
                        port = "5432")
    return {"message": "Hello from FastAPI!"}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
