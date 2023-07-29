from fastapi import FastAPI
import uvicorn
import psycopg2
from urlparse import urlparse

app = FastAPI()

@app.get("/")
async def root():
        result = urlparse("postgresql://postgres:postgres@localhost/postgres")
	username = result.username
	password = result.password
	database = result.path[1:]
	hostname = result.hostname
	port = result.port
	connection = psycopg2.connect(
    		database = database,
    		user = username,
    		password = password,
    		host = hostname,
    		port = port
		)
    	return {"message": "Hello from FastAPI!"}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
