from dotenv import load_dotenv
from typing import Literal
import onnxruntime as rt
import os


def config_env(env: Literal["DEV", "PROD"] = "DEV"):
    if env == "DEV":
        load_dotenv(".env.development")
    else:
        load_dotenv(".env.production")


def config_session():
    MODEL_PATH = os.environ.get("MODEL_PATH")
    if MODEL_PATH is not None:
        session = rt.InferenceSession(MODEL_PATH)
        return session
    else:
        return None
