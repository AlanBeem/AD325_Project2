from rec_sys import RecommendationSystem


def main() -> None:
    #
    print("\n\nRecommendations using 'sum' update technique, and biasing as a function of game popularity, and game similarity:")
    recommendation_system = RecommendationSystem('user_item_data.csv')
    recommendation_system.build_recommendation_system('sepa', 'sum')
    user_keys, all_user_recs = recommendation_system.recommend_for_all_users_with_jaccard(3)
    # returns user_keys, recommendations_for_users
    print(f"Using collision avoidance technique: {recommendation_system.users.collision_avoidance_string}")
    for user, recs in zip(user_keys, all_user_recs):
        print(f"Recommendations for {user}: {recs}")
    print(f"Insertion Time: {recommendation_system.all_table_insertion_time()}")
    print(f"Retrieval Time: {recommendation_system.all_table_retrieval_time()}")
    print(f"UserHashTable collisions since last rehash: {recommendation_system.users.collision_count}")
    print(f"Total collisions since last rehashes: {recommendation_system.all_table_collisions()} (this includes all HashTables used in comparisons of users' games lists)")
    print(f"Probe time: {recommendation_system.all_table_probe_time()}")

def demonstration() -> None:
    # print output to display hash table contents for some probing methods
    probing_functions_list = ['separate chaining', 'linear', 'quadratic', 'double', 'prime', 'rand']
    for each in probing_functions_list:
        recommendation_system = RecommendationSystem('user_item_data.csv')
        recommendation_system.build_recommendation_system(each, 'sum')
        # recommendation_system.users.de_tombstone_table()
        recommendation_system.users.display()
        print(f"collisions since last rehash: {recommendation_system.users.collision_count}")
        if each != 'rand':
            print(f"collisions by hash_size: {recommendation_system.users.collision_count_by_hashsize}")  # for some reason doesn't work with rand
        print('')