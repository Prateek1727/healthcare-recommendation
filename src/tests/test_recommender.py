from src.recommenders.content_based import recommend_content_based

def test_simple_recommendation():
    user_profile = {"conditions": ["hypertension"]}
    plans_db = [{"name": "Low Salt Diet", "condition": "hypertension"}]
    recs = recommend_content_based(user_profile, plans_db)
    assert len(recs) == 1