def recommend_content_based(user_profile, plans_db):
    recommended = []
    for plan in plans_db:
        if plan['condition'] in user_profile.get('conditions', []):
            recommended.append(plan)
    return recommended