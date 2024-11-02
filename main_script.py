from rec_sys import RecommendationSystem

# would recommendation clusters be lists according to original users for recommendations calculated over a large number of pairwise permutations of users?

def main() -> None:
    recommendation_system = RecommendationSystem('user_data.txt')
    recommendation_system.build_recommendation_system('sep')
    # recommendation_system.recommend_items_with_jaccard('user6', 'sep', 10)
    recommendation_system.recommend_for_all_users_with_jaccard(5)

def demonstration() -> None:
    # print output to display hash table contents for each probing method
    pass