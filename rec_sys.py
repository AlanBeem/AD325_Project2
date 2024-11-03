# from hash_table import HashTable
from experimental_hash_table import ExperimentalHashTable
from max_heap import MaxHeap
# from user_max_heap import UserMaxHeap
# from Eric_Lloyd_max_heap import MaxHeap
from random import SystemRandom


class RecommendationSystem:  # this could be used with further synthetic data, such as incorporating time-series s (for example for some avg gaming time, what is number of times stopped playing something else and played this - number of times stopped playing this and played something else) # they may be wanting something but not finding it in the game, after trying- so maybe [recommend] similar # the games could be grouped by Jaccard similarity x Jaccard similarity and ranked lists ? [Clustering]
                             # for time series, use a multiset where games have multiplicity according to how 'liked' they are by each user (as estimated by such as above consideration). Additionally, 
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
    
    # @staticmethod
    # def string_xor_hash(input: str) -> int:
    #     hash_value = 0
    #     for each in input:
    #         hash_value ^= ord(each)
    #     return hash_value
    
    # experimentation idea: show collisions for schemes of hashing:
    def string_xor_hash(self, input: str) -> int:
        hash_value = input.count(' ') * len(input)  # only this line, 8 collisions with user_data.txt titles
        for each in input:  # can use [0::2] or something somewhat shell-sort like [could use relationships between different positions in string, such as the Cartesian product of less-than for each pair of positions encoded as a bit string, as an integer]
            hash_value = hash_value ^ self.rand_array[ord(each)]
        return hash_value
    #
    
    def __init__(self, user_item_file: str, priority_update_technique: str ='max') -> None:
        self.users = None
        self.user_item_file = user_item_file
        self.user_maxheaps = []
        self.rand_array = [SystemRandom().getrandbits(16) for i in range(128)]  # Use of this structure helps minimize collisions in hashing of game titles; 10 bits is sufficient to represent 999
        self.priority_update_technique = priority_update_technique

    def load_data(self):
        # * if load_data is run immediately following initialization, an exception will result because self.users == None
        open_file = open(self.user_item_file, 'r')  # ex: user6 Ghost of Tsushima
        next(open_file)  # headers, disregard as we're hardcoding the format interpretation into this method
        for each in open_file:  # like Java's BufferedReader.readLine()
            # usage: from docs.oracle.com     BufferedReader in = new BufferedReader(new FileReader("foo.in"));
            #                                  then,  ?
            # could also pre-formulate the hash table entries as clustered data
            line_list = each.strip('\n').split(' ')  # TODO use csv reader
            user_key = self.get_user_key(line_list[0])
            game = ' '.join(line_list[1:])
            user_tuple = self.users.retrieve(user_key)
            if user_tuple is None:
                self.users.insert(user_key, [line_list[0], game])  # *
            else:
                self.users.insert(user_key, user_tuple[1] + [game])
                self.users = ExperimentalHashTable(2, self.users.collision_avoidance_string, initial_data=self.users.get_all())

        open_file.close()

    def build_recommendation_system(self, technique):  # O(N^2)
        self.users = ExperimentalHashTable(2, technique)  # collision avoidance technique (defaults to separate chaining)
        #
        self.load_data()
        #
        all_users = self.users.get_all()
        print(all_users)
        self.user_maxheaps = [MaxHeap(each[1][0]) for each in all_users]
        for i in range(len(all_users)):         #
            for j in range(len(all_users)):     # # Cartesian product of Users x Users
                if i != j:  #   #   #   #   #   # without this condition, the top recommended games would be games that the user has played (J(A,A)==1)
                    for game in all_users[j][1][1:]:  # don't push the username ### data format: [(1, ['user1', 'League of Legends', 'Bayonetta', 'Fire Emblem', 'Uncharted', 'Animal Crossing', 'Far Cry', 'Portal', 'Dragon Age', 'Grand Theft Auto V', 'Red Dead Redemption 2', 'Super Mario Bros', 'Metal Gear Solid', 'Ghost of Tsushima', 'World of Warcraft', 'Dragon Age']), (2, ['user2', 'Diablo', 'League of Legends', 'Silent Hill', 'Sekiro', 'The Legend of Zelda', 'Mass Effect', 'Battlefield', 'Half-Life', 'Red Dead Redemption 2', 'Metroid', 'The Last of Us', 'Spider-Man', 'The Elder Scrolls V: Skyrim', 'Fortnite', 'Resident Evil', 'Bioshock', 'The Legend of Zelda']), (3, ['user3', 'Half-Life', 'Metal Gear Solid', 'Cyberpunk 2077', 'Call of Duty', 'Persona 5', 'Bloodborne', 'Diablo', 'Fortnite', 'The Legend of Zelda', 'Dark Souls', 'Gears of War', 'Spider-Man', 'God of War', 'Dragon Age', 'World of Warcraft', 'The Last of Us', 'Splatoon', 'Battlefield', 'Spider-Man', 'The Legend of Zelda', 'The Witcher 3']), (4, ['user4', 'Fallout', 'Elden Ring', 'Bioshock', 'Bayonetta', 'Resident Evil', 'The Witcher 3', 'Minecraft', 'Cyberpunk 2077', 'The Legend of Zelda']), (5, ['user5', 'Super Mario Bros', 'Silent Hill', 'Splatoon', 'Bioshock', 'Forza Horizon', 'Dota 2', 'Minecraft', 'Animal Crossing', 'StarCraft', 'Forza Horizon', 'Animal Crossing', 'Minecraft']), (6, ['user6', 'Ghost of Tsushima', 'Bloodborne', 'Super Mario Bros', 'Horizon Zero Dawn', 'League of Legends', 'Bayonetta', 'Far Cry', 'Gears of War', "Assassin's Creed", 'The Last of Us', 'Sekiro', 'Bayonetta', 'The Last of Us', 'Battlefield']), (7, ['user7', 'Portal', 'Minecraft', 'Splatoon', 'Final Fantasy', 'Silent Hill', 'Resident Evil', 'Dota 2', 'Half-Life', 'Fire Emblem', 'Resident Evil', 'Portal', 'Bayonetta'])]
                        if not game in all_users[i][1][1:]:  # don't exclude games named e.g. 'user1'
                            self.user_maxheaps[i].push(self.get_jaccard_similarity(all_users[i], all_users[j]), game)  # Could weight J by how similar games are that the uses have in their intersection and union ### or make a 2D space out of it (weighted intersection x weighted union) (could even subtract the sum of intra-intersection similarity from intra-union similarity; but I'm not sure how the values would work out)


    def recommend_items_with_jaccard(self, target_user, technique, top_n):
        if self.users is None:
            self.build_recommendation_system(technique)
        elif self.users.collision_avoidance_string != technique:
            self.users = ExperimentalHashTable(2, technique, initial_data=self.users.get_all())
        print(f"Recommendations for {target_user}")
        for user_heap in self.user_maxheaps:
            if user_heap.name == target_user:
                print([each_tuple for each_tuple in user_heap.top_n(top_n)])  # each_tuple[1]
    
    def recommend_for_all_users_with_jaccard(self, technique, top_n) -> None:
        if self.users is None:
            self.build_recommendation_system(technique)
        elif self.users.collision_avoidance_string != technique:
            self.users = ExperimentalHashTable(2, technique, initial_data=self.users.get_all())
        for user_heap in self.user_maxheaps:
            print(f"Recommendations for {user_heap.name}")
            print([each_tuple for each_tuple in user_heap.top_n(top_n)])  # each_tuple[1]
    
    def get_jaccard_similarity(self, user_i: tuple[int, list], user_j: tuple[int, list]) -> float:  # O(N)
        comparison_table = ExperimentalHashTable(31)
        union = 0                   ###
        intersection = 0                ##
        for each in user_i[1][1:]:
            union += 1              ### these provide a count of the union of these two sets
            game_string_hash = self.string_xor_hash(each)
            comparison_table.insert(game_string_hash, each)
        for each in user_j[1][1:]:
            game_string_hash = self.string_xor_hash(each)
            if comparison_table.contains(game_string_hash):
                intersection += 1       ## these provide a count of the intersection
                union -= 1          ###
            else:
                union += 1          ###
        return intersection / union
    
