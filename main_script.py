from rec_sys import RecommendationSystem

# would recommendation clusters be lists according to original users for recommendations calculated over a large number of pairwise permutations of users?

def main() -> None:
    print("\nRecommendations using 'keep maximum' update technique:")
    recommendation_system = RecommendationSystem('user_data_csv.csv')
    recommendation_system.build_recommendation_system('sep')
    # recommendation_system.users.display()
    user_keys, all_user_recs = recommendation_system.recommend_for_all_users_with_jaccard(5)
    # returns user_keys, recommendations_for_users
    print(f"Using collision avoidance technique: {recommendation_system.users.collision_avoidance_string}\n")
    for user, recs in zip(user_keys, all_user_recs):
        print(f"Recommendations for {user}: {recs}\n")
    print(f"Insertion Time: {recommendation_system.all_table_insertion_time()}\n")
    print(f"Retrieval Time: {recommendation_system.all_table_retrieval_time()}\n")
    print(f"Collisions: {recommendation_system.all_table_collisions()}\n")
    print(f"Probe time: {recommendation_system.all_table_probe_time()}\n")
    print("\n\nRecommendations using 'sum' update technique:")
    recommendation_system = RecommendationSystem('user_data_csv.csv')
    recommendation_system.maxheap_update_technique = 'sum'
    recommendation_system.build_recommendation_system('sep')
    user_keys, all_user_recs = recommendation_system.recommend_for_all_users_with_jaccard(5)
    # returns user_keys, recommendations_for_users
    print(f"Using collision avoidance technique: {recommendation_system.users.collision_avoidance_string}\n")
    for user, recs in zip(user_keys, all_user_recs):
        print(f"Recommendations for {user}: {recs}\n")
    print(f"Insertion Time: {recommendation_system.all_table_insertion_time()}\n")
    print(f"Retrieval Time: {recommendation_system.all_table_retrieval_time()}\n")
    print(f"Collisions: {recommendation_system.all_table_collisions()} (this includes all HashTables used in comparisons of users' games lists)\n")
    print(f"Probe time: {recommendation_system.all_table_probe_time()}\n")
    #
    print("\nRecommendations using 'keep maximum' update technique:")
    recommendation_system = RecommendationSystem('user_data_csv.csv')
    recommendation_system.build_recommendation_system('linear')
    # recommendation_system.users.display()
    user_keys, all_user_recs = recommendation_system.recommend_for_all_users_with_jaccard(5)
    # returns user_keys, recommendations_for_users
    print(f"Using collision avoidance technique: {recommendation_system.users.collision_avoidance_string}\n")
    for user, recs in zip(user_keys, all_user_recs):
        print(f"Recommendations for {user}: {recs}\n")
    print(f"Insertion Time: {recommendation_system.all_table_insertion_time()}\n")
    print(f"Retrieval Time: {recommendation_system.all_table_retrieval_time()}\n")
    print(f"Collisions: {recommendation_system.all_table_collisions()}\n")
    print(f"Probe time: {recommendation_system.all_table_probe_time()}\n")
    print("\n\nRecommendations using 'sum' update technique:")
    recommendation_system = RecommendationSystem('user_data_csv.csv')
    recommendation_system.maxheap_update_technique = 'sum'
    recommendation_system.build_recommendation_system('linear')
    user_keys, all_user_recs = recommendation_system.recommend_for_all_users_with_jaccard(5)
    # returns user_keys, recommendations_for_users
    print(f"Using collision avoidance technique: {recommendation_system.users.collision_avoidance_string}\n")
    for user, recs in zip(user_keys, all_user_recs):
        print(f"Recommendations for {user}: {recs}\n")
    print(f"Insertion Time: {recommendation_system.all_table_insertion_time()}\n")
    print(f"Retrieval Time: {recommendation_system.all_table_retrieval_time()}\n")
    print(f"Collisions: {recommendation_system.all_table_collisions()} (this includes all HashTables used in comparisons of users' games lists)\n")
    print(f"Probe time: {recommendation_system.all_table_probe_time()}\n")


def demonstration() -> None:
    # print output to display hash table contents for some probing methods
    probing_functions_list = ['separate chaining', 'linear', 'quadratic', 'double', 'prime', 'rand']
    for each in probing_functions_list:
        recommendation_system = RecommendationSystem('user_data_csv.csv')
        recommendation_system.maxheap_update_technique = 'sum'
        recommendation_system.build_recommendation_system(each)
        # recommendation_system.users.de_tombstone_table()
        recommendation_system.users.display()
        print('\n')