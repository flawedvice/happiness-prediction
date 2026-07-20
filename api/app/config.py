from dotenv import load_dotenv
from typing import Literal
import onnxruntime as rt
import logging
import os


def config_env(logger: logging.Logger, env: Literal["DEV", "PROD"] = "DEV"):

    env_origin = "SET_ENV" if os.getenv("FASTAPI_ENV") else "CODE"
    logger.info(f"Using env from {env_origin}.")

    defined_env = os.getenv("FASTAPI_ENV") or env
    logger.info(f"Environment: {defined_env}")

    if defined_env == "DEV":
        load_dotenv("../.env.development")
    else:
        load_dotenv("../.env.production")


def config_session(logger: logging.Logger):
    MODEL_PATH = os.environ.get("MODEL_PATH")
    if MODEL_PATH is not None:
        session = rt.InferenceSession(MODEL_PATH)
        logger.info("Instantiated ONNX session.")
        return session
    else:
        logger.critical("No MODEL_PATH env defined.")
        return None
