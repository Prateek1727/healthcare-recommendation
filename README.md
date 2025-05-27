# MediRecs: Personalized Healthcare Recommendation System

## Project Structure

```
medi-recs/
├── src/               
│   ├── api/
│   ├── chatbox/
│   ├── config.py
│   ├── data_ingestion/
│   ├── explainability/
│   ├── nlp/
│   ├── recommenders/
│   ├── security/
│   ├── tests/
│   └── utils/
├── frontend/         
│   ├── app.py
│   └── requirements.txt
├── data/            
├── docker/           
│   ├── Dockerfile.api
├── requirements.txt
├── README.md
```

## Quick Start

### Backend

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn src.api.app:app --reload
```

### Frontend

```bash
cd frontend
pip install -r requirements.txt
streamlit run app.py
```

- Open [http://localhost:8501](http://localhost:8501) in your browser.

### Docker (Full Stack)

From project root:

```bash
docker-compose -f docker/docker-compose.yml up --build
```

- API: [http://localhost:8000](http://localhost:8000)
- Frontend: [http://localhost:8501](http://localhost:8501)

## Usage

1. Enter comma-separated patient conditions in the frontend.
2. Click "Get Recommendations" to see tailored plans.

## API

- POST `/recommend`
  - **Body:** `{ "user_profile": { "conditions": [...] }, "plans_db": [...] }`
  - **Returns:** `{ "recommendations": [...] }`

## Testing

```bash
pytest src/tests/
```

## Extend

- Add more recommendation algorithms in `src/recommenders/`
- Enhance NLP in `src/nlp/`
- Connect to real patient data in `src/data_ingestion/`
- Build richer UI in `frontend/app.py`
