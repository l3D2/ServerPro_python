from typing import Union
from fastapi import FastAPI
from mongodb import MongoDB
import threading
import asyncio
import sys

app = FastAPI()

async def initialize():
    global DB
    DB = MongoDB("IoT")
    import uvicorn
    await uvicorn.run(app, host="0.0.0.0", port=8000)

@app.on_event("startup")
async def startup_event():
    await initialize()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

""" @app.on_event("startup")
async def insert_data():
    await asyncio.sleep(2)  # Adjust this delay as needed to ensure DB initialization completes
    if DB:  # Ensuring DB connection is established before insertion
        data = {
            "DeviceName": "esp32-1",
            "WaterLevel": 30,
            "Date-Time": "19/11/2023-10:00:00"
        }
        DB.insertData("tests", data) """

mqtt_thread = threading.Thread(target=run_mqtt)
mqtt_thread.start()

# Asynchronous function to start the application
async def run_app():
    await startup_event()

if __name__ == "__main__":
    try:
        asyncio.run(run_app())
    except KeyboardInterrupt:
        sys.exit()