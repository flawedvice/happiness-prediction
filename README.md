# Happiness Prediction

This repository contains a small project to predict national happiness (or a happiness-related score) from country-level socioeconomic and environmental indicators. The project includes data, preprocessing, a trained ONNX model, and a FastAPI-based inference server.

**Key features:**

- Data processing and feature engineering used for model inputs
- An ONNX model for inference ([models/model_2026-07-15.onnx](models/model_2026-07-15.onnx))
- A FastAPI app exposing a `/inference` endpoint for predictions
- A Dockerfile for running the API in a container

**Project Structure**

- `api/` — FastAPI service, Dockerfile and app code (see `api/app`)
- `models/` — exported ONNX model artifacts
- `data/` — raw and processed data and CSV exports
- `analysis.ipynb` — exploratory analysis / notebook
- `requirements.txt` / `pyproject.toml` — Python dependencies

## Getting started

Prerequisites: Python 3.13+, or Docker.

1. Create and activate a virtual environment (recommended):

```bash
python -m venv .venv
source .venv/Scripts/activate
```

2. Install dependencies:

```bash
pip install . # uses pyproject.toml
```

## Running the API locally

Start the FastAPI app using the library's CLI:

```bash
fastapi dev api/app/main.py
```

The service exposes:

- `GET /` — health / hello endpoint
- `POST /inference` — run a prediction

## Example inference request

Send a JSON payload matching the `Data` model schema (see `api/app/custom_types.py`). Example:

```bash
curl -s -X POST "http://localhost:8000/inference" \
	-H "Content-Type: application/json" \
	-d '{
		"electricity": 99.4,
		"agricultural_land": 44.270761,
		"alternative_energy": 6.005,
		"food_production": 101.965455,
		"forest_area": 31.738011,
		"gdp_growth": 3.402213,
		"gdp_per_capita_growth": 1.943356,
		"government_expenditure": 4.17541,
		"inflation_prices": 3.34438,
		"life_expectancy": 74.0055,
		"net_migration": -3851.5,
		"population_growth": 1.21159,
		"urban_agglomeration": 19.846357,
		"hiv_prevalence": 0.3,
		"urban_population": 36.20459,
		"rural_population": 14.5,
		"protected_areas": 5.15,
		"unemployment": 63.79541
	}'
```

Response example:

```json
{ "prediction": 3.8 }
```

## Notes on inputs and preprocessing

- The API expects a JSON object that matches the `Data` Pydantic model in `api/app/custom_types.py`.
- Incoming data is preprocessed and engineered (see `api/app/processing.py`) to compute additional features used by the model.
- The ONNX runtime session is configured via `api/app/config.py` and looks for the model at the path configured by environment variables (the Dockerfile sets `MODEL_PATH=models/model_2026-07-15.onnx`).

## Docker

Build and run the API container using the provided `api/Dockerfile`:

```bash
docker build -t happiness-api ./api
docker run -p 80:80 happiness-api
```

## Data

Source CSVs and cleaned tables are in the `data/` folder. Datasets were obtained both manually and dynamically from the World Happiness Report and the World Bank Data Bank, respectively. Details about the data sources and the data collection process can be found at the beginning of the Jupyter notebook `analysis.ipynb`.

## Results

| Metric | Value (Test Set) |
| ------ | ---------------- |
| R²     | $0.9577$         |
| RMSE   | $0.2242$         |

The model explains ~$96$% of the variance in national happiness scores, with an average prediction error of $±0.22$ points on the happiness scale (range: $0.0$ - $10.0$). Key predictive features include education, health, and access to basic services related indicators.
