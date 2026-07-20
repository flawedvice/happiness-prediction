FROM python:3.13-trixie

WORKDIR /app

RUN pip install --no-cache-dir --upgrade fastapi[standard] pandas numpy python-dotenv pydantic onnxruntime

COPY ./app .

COPY ./models /app/models

ENV FASTAPI_ENV="PROD"
ENV MODEL_PATH="models/model_2026-07-15.onnx"

CMD ["fastapi", "run", "./main.py", "--port", "80"]
