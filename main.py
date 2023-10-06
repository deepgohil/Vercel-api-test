# from typing import Union
# from fastapi import FastAPI
# import requests
# from bs4 import BeautifulSoup
import pymongo
from pydantic import BaseModel

# app = FastAPI()

class FormData(BaseModel):
    username: str
    lastname: str
    email: str
    phoneno: str
    address: str
    country: str
    state: str
    zip: str


# myclient = pymongo.MongoClient("mongodb+srv://ipd:virat@ipd.bervskx.mongodb.net/")
# #use database named "organisation"
# mydb = myclient["aagamhacks"]

# # #use collection named "developers"
# mycol = mydb["users"]


# url = "https://leetcode.com/deepgohil/"  

# @app.get("/")
# def read_root():
#         response = requests.get(url)

#         if response.status_code == 200:

#             soup = BeautifulSoup(response.text, "html.parser")

#             target_div = soup.find("div", class_="text-[24px] font-medium text-label-1 dark:text-dark-label-1")

#             if target_div:
#                 element_text = target_div.get_text()
#                 print("Scraped element text:", element_text)
#             else:
#                 print("Desired div element not found.")
#         else:
#             print("Failed to fetch the page:", response.status_code)

#         return {"Hello":element_text}


# @app.get("/count")
# def read_root():
#     try:
#         count = mycol.count_documents({})
#         return count
#     except Exception as e:
#         return {"error": "An error occurred while fetching data count."}
    
# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: Union[str, None] = None):
#     return {"item_id": item_id, "q": q}







# @app.post("/submit/")
# async def submit_form(data: FormData):
#     # Here you can handle the form data as needed, for example, store it in a database
#     # For now, let's just return the received data as a response
#     print(data)
#     return {"message": "Form submitted successfully", "data": data}



from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

# Enable CORS for all origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow requests from any origin
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods (GET, POST, etc.)
    allow_headers=["*"],  # Allows all headers
)



@app.post("/submit/")
async def submit_form(data: FormData):
    data_dict = data.dict()

    # Handle form data here
    print(data_dict)  # Print form data dictionary to the server console

    # Here you can save the data to a database (MongoDB in this case)
    myclient = pymongo.MongoClient("mongodb+srv://ipd:virat@ipd.bervskx.mongodb.net/")
    mydb = myclient["aagamhackthon"]
    mycol = mydb["user"]

    # Insert the data dictionary into the MongoDB collection
    mycol.insert_one(data_dict)

    # Return a successful response
    return {"message": "Form submitted successfully!"}


# C:\Users\deepgohil\Desktop\Vercel api test