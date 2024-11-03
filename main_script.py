from rec_sys import RecommendationSystem

# would recommendation clusters be lists according to original users for recommendations calculated over a large number of pairwise permutations of users?

def main() -> None:
    recommendation_system = RecommendationSystem('user_data.txt')
    recommendation_system.build_recommendation_system('sep')
    # recommendation_system.recommend_items_with_jaccard('user6', 'sep', 10)
    recommendation_system.recommend_for_all_users_with_jaccard('sep', 100)

def demonstration() -> None:
    # print output to display hash table contents for each selected probing method
    # probing_functions_list = ['linear', 'quadratic', 'double', 'prime', '3/2', "to Euler's number", "^e 2", 'cubic', 'exponential', 'quartic', 'quintic', 'sextic', 'septic', 'octic', 'nonic', 'decic', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', 'rand']  #, 'rand double hashing']
    probing_functions_list = ['sep', 'linear', 'quadratic', 'prime', "^e 2", 'rand']  # subset of defined functions , 'double'
    for probe_function in probing_functions_list:
        print(f"probe_function: {probe_function}")
        recommendation_system = RecommendationSystem('user_data.txt')
        recommendation_system.build_recommendation_system(probe_function)
        recommendation_system.users.display()