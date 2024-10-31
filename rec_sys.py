from hash_table import HashTable
from max_heap import MaxHeap


collision_technique = ''


class RecommendationSystem:  # this could be used with further synthetic data, and further techniques, such as incorporating time-series (for example for some avg gaming time, what is number of times stopped playing something else and played this - number of times stopped playing this and played something else) # they may be wanting something but not finding it in the game, after trying- so maybe similar # the games could be grouped by Jaccard similarity x Jaccard similarity and ranked lists ?
    # for this Project, an 8-bit width for strings is sufficient (but not for hundreds of users)
    # def get_user_key(user: str) -> int:
    #     # Variable string exclusive-or method (described: https://www.eecs.umich.edu/courses/eecs380/ALG/niemann/s_has.htm)
    #     key = 0
    #     for each in user:
    #         key = [key ^ ord(each)]
    #     return key
    @staticmethod
    def get_user_key(user: str) -> int:  # could combine user names and random names from Project 2 material
        return int(user[4:])  # ex: user6
    
    def __init__(self, user_item_file: str) -> None:
        self.users = None
        self.user_item_file = user_item_file
        # self.jaccard_matrix = None
        self.user_maxheaps = []

    def load_data(self):
        open_file = open(self.user_item_file, 'r')  # ex: user6 Ghost of Tsushima
        next(open_file)  # headers, disregard as we're hardcoding the format interpretation into this method
        for each in open_file:  # like Java's BufferedReader.readLine()
            # usage: from docs.oracle.com     BufferedReader in = new BufferedReader(new FileReader("foo.in"));
            #                                  then, for each in in ?
            line_list = each.split(' ')
            user_key = self.get_user_key(line_list[0])
            game = ' '.join(line_list[1:])
            user_tuple = self.users.retrieve(user_key)
            if user_tuple is None:
                self.users.insert(user_key, [game])
            else:
                games_list = user_tuple[1]
                games_list.append(game)
                self.users.insert(user_key, games_list)
        open_file.close()

    def build_recommendation_system(self, technique):
        self.users = HashTable(50, technique)  # collision avoidance technique (defaults to separate chaining)
        self.load_data()
        all_users = self.users.get_all()
        self.user_maxheaps = [MaxHeap() for each in all_users]
        for i in range(len(all_users)):
            for j in range(len(all_users)):
                if i != j:
                    for game in all_users[j][1]:
                        if game not in all_users[i][1]:
                            self.user_maxheaps[i].push(self.get_jaccard_similarity(all_users[i], all_users[j], game), game)

    def recommend_items_with_jaccard(self, target_user, technique, top_n):
        # games from MaxHeap
        print(f"Recommendations for {target_user}")
        print(self.user_maxheaps)
    
    def get_jaccard_similarity(self, user_i: tuple[int, list], user_j: tuple[int, list]) -> float:
        card_user_i = len(user_i[1])
        card_user_j = len(user_j[1])
        comparison_table = HashTable(31)
        intersection = 0
        for each in user_i[1]:
            game_string_hash = 0
            for s in each:
                game_string_hash = game_string_hash * 31 + ord(s) & 0b1111111111111111
            comparison_table.insert(game_string_hash, each)
        for each in user_j[1]:
            game_string_hash = 0
            for s in each:
                game_string_hash = game_string_hash * 31 + ord(s) & 0b1111111111111111
            if comparison_table.contains(game_string_hash):
                intersection += 1
        return intersection / (card_user_i + card_user_j - intersection)
    
