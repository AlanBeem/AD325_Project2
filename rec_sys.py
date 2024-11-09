import csv
from hash_table import HashTable
from user_hash_table import UserHashTable
# from max_heap import MaxHeap
from user_max_heap import UserMaxHeap


class RecommendationSystem:  # this could be used with further synthetic data, such as incorporating time-series s (for example for some avg gaming time, what is number of times stopped playing something else and played this - number of times stopped playing this and played something else) # they may be wanting something but not finding it in the game, after trying- so maybe [recommend] similar # the games could be grouped by Jaccard similarity x Jaccard similarity (pairs of co-purchasing) and ranked lists ? [Clustering]
                             # for time series, use a multiset where games have multiplicity according to how 'liked' they are by each user (as estimated by such as above consideration). Additionally, 
    # for this Project, for example, an 8-bit width for strings is sufficient (but not for hundreds of users)
    # however, specifically, using the digit portion of the user string guarantees no key-collisions (clusters)
    #     # Variable string exclusive-or method (described: https://www.eecs.umich.edu/courses/eecs380/ALG/niemann/s_has.htm)
    # # @staticmethod
    # # def string_xor_hash(input: str) -> int:
    # #     hash_value = 0
    # #     for each in input:
    # #         hash_value ^= ord(each)
    # #     return hash_value
    # def string_xor_hash(self, input: str) -> int:
    #     hash_value = input.count(' ') * len(input)  # only this line, 8 collisions with user_data.txt titles
    #     for each in input:  # can use [0::2] or something somewhat shell-sort like; any hashing over the ordered sequence would work
    #         hash_value = hash_value ^ self.rand_array[ord(each)]
    #     return hash_value
    
    def __init__(self, user_item_file: str) -> None:
        self.maxheap_update_technique = 'max'
        self.users = None  # will be a UserHashTable after setup (build_recommendation_system)
        self.user_item_file = user_item_file
        self.user_maxheaps = []
        self.comparison_tables = []  # for all user comparisons, count number of collisions (doesn't include adding duplicates)
        self.games_cumulative_list = []
        self.games_list = []
        self.minimum_similarity = 0
        self.games_similarity_matrix = []

    def load_data(self) -> None:
        """if load_data is run immediately following initialization, an exception will result because self.users == None"""
        with open(self.user_item_file, newline='') as csvfile:
            data_reader = csv.DictReader(csvfile, fieldnames=['user_id', 'item_id'])
            next(data_reader)
            for row in data_reader:
                user = row['user_id']
                game = row['item_id']
                self.games_cumulative_list.append(game)
                self.users.insert(user, game)
        csvfile.close()
        self.users.de_tombstone_table()  # when using open addressing the table accumulates a large number of True entries (empty after removal)
        # self.users.display()

    def build_recommendation_system(self, technique, update_technique) -> None:
        self.users = UserHashTable(11, technique)  # collision avoidance technique (defaults to separate chaining)
        # sets up table to first prime after 11
        #
        self.load_data()
        #
        all_users = self.users.get_all()
        all_users.sort(key=lambda p: p[0])
        self.user_maxheaps = [UserMaxHeap(f"{each[0]}", update_technique) for each in all_users]
        #
        # this addition made to promote consistent ordering upon heaping values from a hashed order (ties would be in any order)
        #
        for each_game in set(self.games_cumulative_list):
            game_bias = (self.games_cumulative_list.count(each_game) / len(self.games_cumulative_list)) * 0.00000000000001
            for each_heap in self.user_maxheaps:
                each_heap.push(game_bias, each_game)
        self.games_list = list(set(self.games_cumulative_list))
        self.games_similarity_matrix = [[0 for g in self.games_list] for l in self.games_list]
        game_pairs = set()
        for i, game_i in zip(range(len(self.games_list)), self.games_list):
            for j, game_j in zip(range(len(self.games_list)), self.games_list):
                game_pairs.add((game_i, game_j))
                for each_user in all_users:
                    self.games_similarity_matrix[i][j] += 1 if (game_i in each_user[1] and game_j in each_user[1]) else 0
        for k in range(len(self.games_similarity_matrix)):
            for L in range(len(self.games_similarity_matrix)):
                self.games_similarity_matrix[k][L] /= len(game_pairs)
        # Jaccard similarity:
        self.minimum_similarity = 1
        for i in range(len(all_users)):         #
            for j in range(len(all_users)):     # # Cartesian product of Users x Users
                if i != j:  # don't calcualte J(A,A)
                    similarity = self.get_jaccard_similarity(all_users[i], all_users[j])
                    if similarity < self.minimum_similarity:
                        self.minimum_similarity = similarity
                    for game in all_users[j][1]:
                        if not game in all_users[i][1]:
                            self.user_maxheaps[i].push(similarity, game)

    def get_jaccard_similarity(self, user_i: tuple[any, list], user_j: tuple[any, list]) -> float:
        """calling this without first setting up self.users (using self.load_data(filename)) will cause an exception."""
        self.comparison_tables.append(HashTable(31, self.users.collision_avoidance_string))  # tests for equality of input keys
        # self.comparison_tables.append(HashTable(31, 'separate'))  # tests for equality of input keys
        union = 0                   ### these provide a count of the union of these two sets (lines 85, 88, 95, 97)
        intersection = 0                  ## these provide a count of the intersection of these two sets (lines 86, 94)
        for each in user_i[1]:
            union += 1              ###
            self.comparison_tables[-1].insert(each, '')
        for each in user_j[1]:
            if self.comparison_tables[-1].contains(each):
                intersection += 1         ##
            else:
                union += 1          ###
        calc1 = intersection / union  # return 
        
        user_i_set = set(user_i[1])
        user_j_set = set(user_j[1])
        
        calc2 = len(user_i_set.intersection(user_j_set)) / len(user_i_set.union(user_j_set))

        if calc1 != calc2:
            print(f"calc1: {calc1}")
            print(f"calc2: {calc2}")

        return len(user_i_set.intersection(user_j_set)) / len(user_i_set.union(user_j_set))
    
    def recommend_items_with_jaccard(self, target_user, technique, update_technique, top_n) -> list[str]:
        if self.users is None:
            self.build_recommendation_system(technique, update_technique)
        # games from UserMaxHeap  # could add a reset to heap to keep space complexity to requirements for one user at a time
        recommendations_for_user = None
        # user_rec_games = []
        user = self.users.retrieve(target_user)
        # user_purchased_games = user[1]
        self.users.insert(user[0], user[1])
        for user_heap in self.user_maxheaps:
            if user_heap.name == target_user:
                # heap_items = user_heap.top_n(len(user_heap.array))  # contains user recommended games and priority
                # for h_item in heap_items:
                #     # game = h_item[1]
                #     game_similarity = 0
                #     similarity_row = self.games_similarity_matrix[self.games_list.index(h_item[1])]
                #     for each_similarity, listed_game in zip(similarity_row, self.games_list):
                #         if listed_game in user_rec_games:
                #             game_similarity += each_similarity
                #     game_similarity *= self.minimum_similarity
                #     game_similarity /= 100
                #     user_heap.push(h_item[0] + game_similarity, h_item[1])
                user_top_n = user_heap.top_n(top_n)
                for each in user_top_n:
                    user_heap.push(each[0], each[1])
                recommendations_for_user = [each_tuple[1] for each_tuple in user_top_n]
        return recommendations_for_user
    
    def recommend_for_all_users_with_jaccard(self, top_n) -> tuple[list[str], list[list[str]]]:
        recommendations_for_users = []
        user_keys = []
        
        for user_heap in self.user_maxheaps:
            user_keys.append(user_heap.name)
            recommendations_for_users.append(self.recommend_items_with_jaccard(user_heap.name, self.users.collision_avoidance_string, 'sum', top_n))
        return user_keys, recommendations_for_users
    
    def all_table_insertion_time(self) -> float:
        insertion_time = 0
        for each in [self.users] + self.comparison_tables:
            insertion_time += each.insert_time
        return insertion_time
    
    def all_table_retrieval_time(self) -> float:
        retrieval_time = 0
        for each in [self.users] + self.comparison_tables:
            retrieval_time += each.insert_time
        return retrieval_time

    def all_table_collisions(self) -> int:
        collisions = 0
        for each in [self.users] + self.comparison_tables:
            collisions += each.collision_count
        return collisions

    def all_table_probe_time(self) -> float:
        probe_time = 0
        for each in [self.users] + self.comparison_tables:
            probe_time += each.probe_time
        return probe_time
