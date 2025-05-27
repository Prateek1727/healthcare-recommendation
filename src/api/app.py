from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from src.recommenders.content_based import recommend_content_based

app = FastAPI()

# Allow frontend (Streamlit/React) to communicate
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/recommend")
async def recommend(request: Request):
    body = await request.json()
    user_profile = body.get("user_profile", {})
    plans_db = body.get("plans_db", [])
    recommendations = recommend_content_based(user_profile, plans_db)
    return {"recommendations": recommendations}