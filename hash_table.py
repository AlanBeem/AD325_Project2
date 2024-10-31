from sympy import primerange
import math
# TODO Make HashTable work with strings as keys

class HashTable:
    """def linear_probing(hash1: int, probe: int, hash_size: int) -> int:
    return (hash1 + probe) % hash_size

    def quadratic_probing(hash1: int, probe: int, hash_size: int) -> int:
        return (hash1 + probe**2) % hash_size

    def double_hashing(hash1: int, probe: int, hash_size: int) -> int:
        hash2 = 1 + (hash1 % (hash_size - 1))  # so this goes at least 1, where hash2 is multiplied by probe
        return (hash1 + probe * hash2) % hash_size

    def prime_probing(hash1: int, probe: int, hash_size: int) -> int:
        current_prime = self.get_next_prime(2)
        for p in range(probe):
            current_prime = self.get_next_prime(current_prime)
        return (hash1 + current_prime) % hash_size

    def separate_chaining(...

    class SeparateNode:
        def __init__(self, key: int, value: any, next=None) -> None:"""
    #
    # Traverse pseudomethod:
    #  while current index and not key == key:
    #   get next index
    #  else:
    #   if current index and key == key:
    #    return current index (element)
    #
    @staticmethod
    def get_next_prime(current_prime: int) -> int:
        # from AD315 Homework 2:
        def isPrime(n: int) -> bool:
            """evaluates primeness of n (n is only evenly divisible by itself and 1)"""
            prime_bool = True
            for n_i in range(2,int(math.sqrt(n)) + 1):
                if n % n_i == 0:
                    prime_bool = False
                    break
            return prime_bool
        def isMersenne(n: int) -> bool:
            """evaluates Mersenne primeness (isPrime(n) and n == 2^k - 1 for k in setN)\n
            n == 2^k - 1\n
            n + 1 == 2^k\n
            log2(n + 1) ≈ k, where in N = {0,1,2,...}, with a cutoff of 0.0000000001
            """
            return isPrime(n) and math.log2(n + 1) % 1.0 < 1E-10  # 1E-15, same output
        #
        current_prime += 1
        while not isPrime(current_prime) or isMersenne(current_prime):
            current_prime += 1
        return current_prime
    
    # static?
    def linear_probing(self, hash1: int, probe: int, hash_size: int) -> int:
        return (hash1 + probe) % hash_size

    def quadratic_probing(self, hash1: int, probe: int, hash_size: int) -> int:
        return (hash1 + probe**2) % hash_size

    def double_hashing(self, hash1: int, probe: int, hash_size: int) -> int:
        hash2 = 1 + (hash1 % (hash_size - 1))  # so this goes at least 1, where hash2 is multiplied by probe
        return (hash1 + probe * hash2) % hash_size

    def separate_chaining(self, hash1: int, probe: int, hash_size: int) -> int:
        pass

    def prime_probing(self, hash1: int, probe: int, hash_size: int) -> int:
        current_prime = self.get_next_prime(2)
        for p in range(probe):
            current_prime = self.get_next_prime(current_prime)
        return (hash1 + current_prime) % hash_size
# ## # # #  #  #  #
    def __init__(self, size, collision_avoidance: str = 'separate chaining', initial_data: list[any] = []) -> None:
        # False represents never filled, True represents removed; filled: tuple (key, value) or SeparateNode
        # This behavior is consistent across all collision avoidance techniques, were a method to be implemented to switch techniques, it would work, but that wouldn't matter, as the table would need to be rehashed
        self.collision_count_by_hashsize = []
        self.hash_table = [False for i in range(size)]  # self.insert: self.hash_table[current] = (key, value)
        # match ca:=collision_avoidance.lower():
        #     case ca.startswith('linear'):
        #         self.probe_function = self.linear_probing
        #     case ca.startswith('quad'):
        #         self.probe_function = self.quadratic_probing
        #     case ca.startswith('double'):
        #         self.probe_function = self.double_hashing
        #     case ca.startswith('sep'):
        #         self.probe_function = self.separate_chaining
        #     case ca.startswith('prime'):
        #         self.probe_function = self.prime_probing
        if collision_avoidance.lower().startswith('linear'):
            self.probe_function = self.linear_probing
        elif collision_avoidance.lower().startswith('quad'):
            self.probe_function = self.quadratic_probing
        elif collision_avoidance.lower().startswith('double'):
            self.probe_function = self.double_hashing
        elif collision_avoidance.lower().startswith('sep'):
            self.probe_function = self.separate_chaining
        elif collision_avoidance.lower().startswith('prime'):
            self.probe_function = self.prime_probing
        for each in initial_data:
            self.insert(each)
    
    def get_all(self):
        all_tuples = []
        for each in self.hash_table:
            if isinstance(each, HashTable.SeparateNode):
                all_tuples.extend([every.node_tuple for every in each.get_sub_list()])
            else:
                if each and not each is True:
                    all_tuples.append(each)
        return all_tuples

    def get_keys(self) -> list[int]:
        return [each[0] for each in self.get_all()]

    def rehash_table(self) -> None:  # -> float ? # return time for each function
        current_data = self.get_all()
        self.hash_table = [False for r in range(self.get_next_prime(len(self.hash_table)))]
        for each in current_data:
            self.insert(each[0], each[1])

    def hash(self, key) -> int:
        if isinstance(key, int):
            return key % len(self.hash_table)
        else:
            return hash(key) % len(self.hash_table)
    
    def probe(self, hash_key, probe) -> int:
        self.collision_count_by_hashsize.append(len(self.hash_table))  # maintains data that can be used to construct a per hashsize view of collisions, which can be compared across techniques
        return self.probe_function(hash_key, probe, len(self.hash_table))
    
    def insert(self, key: int, value: any) -> None:
        hash_key = self.hash(key)
        if self.probe_function == self.separate_chaining:
            if not isinstance(self.hash_table[hash_key], HashTable.SeparateNode):
                self.hash_table[hash_key] = HashTable.SeparateNode((key, value))
            else:
                self.hash_table[hash_key].add(key, value)
        else:
            current = hash_key
            probe = 0
            while not self.hash_table[current] or self.hash_table[current][0] == key:
                probe += 1
                current = self.probe(hash_key, probe)
                if probe >= len(self.hash_table) // 2:  # TODO adjust to load factor
                    self.rehash_table()  #              # whats expected probe distance per lambda? put plot in ipynb
                    self.insert(key, value)
                    break
            else:
                self.hash_table[current] = (key, value)

    def retrieve(self, key: int) -> any:   # retrieves a value from (key, value) (removes the tuple)
        hash_key = self.hash(key)
        if self.probe_function == self.separate_chaining:
            current = self.hash_table[hash_key]
            if not isinstance(current, bool):
                if current.node_tuple[0] == key:
                    self.hash_table[hash_key] = current.next
                else:
                    retrieval = preceding = None
                    while current.node_tuple[0] != key:  # traverse to equal node or placeholder value
                        preceding = current              #
                        current = current.next         # #
                    else:
                        if current.node_tuple[0] == key:
                            retrieval = current.node_tuple
                            if preceding is not None:
                                preceding.next = current.next
                            else:
                                self.hash_table[hash_key] = current.next
        else:
            current = hash_key
            probe = 0
            while self.hash_table[current] and self.hash_table[current][0] != key:
                probe += 1
                current = self.probe(hash_key, probe)
            # either probing ended on a False, or a value with key == key
            retrieval = None if not self.hash_table[current] else self.hash_table[current][1] # value
            if retrieval:
                self.hash_table[current] = True  # represents empty after removal
            return retrieval
        
    def contains(self, key: int) -> bool:  # such as for computing intersection of items
        hash_key = self.hash(key)
        if self.probe_function == self.separate_chaining:
            current = self.hash_table[hash_key]
            if not isinstance(current, bool):
                return current.contains(key)
        else:
            current = hash_key
            probe = 0
            while self.hash_table[current] and self.hash_table[current][0] != key:
                probe += 1
                current = self.probe(hash_key, probe)
            # either probing ended on a False, or a tuple (key, value) with key == key
            # that is, probing will not end on a True, therefore:
            return False if not self.hash_table[current] else True  # True == (key == key)

    class SeparateNode:
        def __init__(self, node_tuple: tuple[int, any], next=True) -> None:  # True as next placeholder makes structures resulting from use of this consistent with containing class behavior 
            self.node_tuple = node_tuple
            self.next = next

        def add(self, key: int, value: any) -> None:
            current = self
            # self.subkeys.add(key)  # but, would be a hash table in a hash table
            while not isinstance(current.next, bool|None):
                current = current.next
                # current.subkeys.add(key)
            current.next = HashTable.SeparateNode((key, value))  # Doesn't update- TODO
        
        def get_sub_list(self) -> list[tuple[int,any]]:
            """includes self"""
            sub_list = [self]
            if not isinstance(self.next, bool|None):
                sub_list.extend(self.next.get_sub_list())
            return sub_list

        def get_keys(self) -> list[int]:
            keys_list = [self.node_tuple[0]]
            if not isinstance(self.next, bool|None):
                keys_list.extend(self.next.get_keys())
            return keys_list
        
        def contains(self, key: int) -> bool:
            if self.node_tuple[0] == key:
                return True
            else:
                if not isinstance(self.next, bool|None):
                    return self.next.contains(key)
                else:
                    return False

