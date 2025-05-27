import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

def recommend_collaborative(user_id, ratings_matrix, k=3):
    user_vector = ratings_matrix[user_id]
    similarities = cosine_similarity([user_vector], ratings_matrix)[0]
    similar_users = np.argsort(similarities)[-k-1:-1][::-1]
    recommendations = []
    for idx in similar_users:
        recommendations.extend(np.where(ratings_matrix[idx] > 0)[0])
    return list(set(recommendations))