# This is a sample Python script.
# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI,UploadFile,File,Request
import pandas
import json
from pydantic import BaseModel

app = FastAPI()

# add cors middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class DataUrl(BaseModel):
    url: str


@app.get("/")
async def root():
    return "Welcome to Maca api"

# Api to upload csv file
@app.post("/upload")
def upload(defaulturl: DataUrl):
    df = pandas.read_csv(defaulturl.url,sep=',')
    jsonoutput="output.json"
    df.to_json(jsonoutput,indent=1,orient='records')
    f = open('output.json')
    data = json.load(f)
    return data


# Api to upload excel file
@app.post("/uploadexcel")
def upload_excel(defaulturl: DataUrl):
    jsonoutput="outputexcel.json"
    df = pandas.read_excel(defaulturl.url)
    df.to_json(jsonoutput,indent=1,orient='records')
    f = open('outputexcel.json')
    data = json.load(f)
    return data



