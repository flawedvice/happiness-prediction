from config import config_env, config_session
from fastapi import FastAPI, HTTPException
from processing import preprocess
from custom_types import Data
from typing import List
import numpy as np
import logging

# Configurate logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger(__name__)


app = FastAPI()

config_env(logger, "DEV")

session = config_session(logger)


@app.get("/")
def hello():
    logger.info("Testing root route")
    return {"message": "Hello World!"}


@app.post("/inference")
def predict(data: Data):
    if session is None:
        logger.critical("ONNX session object is undefined.")
        raise HTTPException(500, "Cannot use inference model.")

    input_meta = session.get_inputs()[0]

    prepared_data = preprocess(data)
    if prepared_data is None:
        logger.error(
            f"Incorrect data format. Must comply with {input_meta.shape}. Received {prepared_data} instead."
        )
        raise HTTPException(500, "Internal server error")

    input_feed = {input_meta.name: prepared_data}
    predictions = session.run(None, input_feed=input_feed)

    response = predictions[0].tolist()[0][0]

    logger.info(f"Got preddiction: {response}")

    return {"prediction": response}
