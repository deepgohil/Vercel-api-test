from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import pymongo
import json
import logging

app = FastAPI()

# Enable CORS for all origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods
    allow_headers=["*"],  # Allow all headers
)

# MongoDB connection
myclient = pymongo.MongoClient("mongodb+srv://ipd:virat@ipd.bervskx.mongodb.net/")
mydb = myclient["Atharva"]
mycol = mydb["seller"]

@app.post("/clogin")
async def clogin(data: dict):
    try:
        query = {
            "email": data.get('mail'),
            "password": data.get('password')
        }

        result = mycol.find_one(query)

        if result:
            return {
                "statusCode": 200,
                "message": "success"
            }
        else:
            raise HTTPException(status_code=401, detail="Unauthorized: Login failed")

    except Exception as e:
        logging.error(f"An error occurred: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")
