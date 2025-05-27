from src.recommenders.content_based import recommend_content_based

def chatbot_response(user_message, user_profile, plans_db):
    if "recommend" in user_message.lower():
        recs = recommend_content_based(user_profile, plans_db)
        return f"Recommended plans: {[p['name'] for p in recs]}"
    return "I'm here to help with your healthcare recommendations."