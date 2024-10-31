from rec_sys import RecommendationSystem

def main() -> None:
    recommendation_system = RecommendationSystem('user_data.txt')
    recommendation_system.build_recommendation_system('sep')
    recommendation_system.recommend_items_with_jaccard('user6', 'sep', 10)