from config import config_env, config_session
from fastapi import FastAPI, HTTPException
from processing import preprocess
from custom_types import Data
import json

app = FastAPI()

config_env("DEV")

session = config_session()


@app.get("/")
def hello():
    return {"message": "Hello World!"}


@app.post("/inference")
def predict(data: Data):
    if session is None:
        raise HTTPException(500, "Cannot use inference model.")

    input_meta = session.get_inputs()[0]

    prepared_data = preprocess(data)
    if prepared_data is None:
        print(
            f"Incorrect data format. Must comply with {input_meta.shape}. Received {prepared_data} instead."
        )
        raise HTTPException(500, "Internal server error")

    input_feed = {input_meta.name: prepared_data}
    predictions = session.run(None, input_feed=input_feed)

    response = predictions[0].tolist()[0][0]
    return {"prediction": response}
