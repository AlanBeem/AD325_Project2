# For future use: This does not update duplicate keys, useful for clustering;
#  if updating is required, subclass or retrieve then insert
# 11/02/2024
# Alan M H Beem
import math  # Euler's constant, exponential function
import time
# from random import SystemRandom  # hash table in hash table


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
        def __init__(self, key, value: any, next=None) -> None:"""
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
        # from AD315 Homework 2:                                                           ##
        def isPrime(n: int) -> bool:
            """evaluates primeness of n (n is only evenly divisible by itself and 1)"""
            prime_bool = True
            for n_i in range(2,int(math.sqrt(n)) + 1):
                if n % n_i == 0:
                    prime_bool = False
                    break
            return prime_bool
        def isMersenne(n: int) -> bool:  # I'd read somewhere that hash table sizes 'near a power of 2' should be avoided, but I also found a reference describing the utility of hash table sizes equal to Mersenne primes
            """evaluates Mersenne primeness (isPrime(n) and n == 2^k - 1 for k in setN)\n
            n == 2^k - 1\n
            n + 1 == 2^k\n
            log2(n + 1) ≈ k, where in N = {0,1,2,...}, with a cutoff of 0.0000000001
            """
            return isPrime(n) and math.log2(n + 1) % 1.0 < 1E-10  # 1E-15, same output
        #                                                                                  ##
        current_prime += 1
        while not isPrime(current_prime):  # or isMersenne(current_prime):
            current_prime += 1
        return current_prime
    
    @staticmethod
    def linear_probing(hash1: int, probe: int, hash_size: int) -> int:
        return (hash1 + probe) % hash_size

    @staticmethod
    def quadratic_probing(hash1: int, probe: int, hash_size: int) -> int:
        return (hash1 + probe**2) % hash_size

    @staticmethod
    def double_hashing(hash1: int, probe: int, hash_size: int) -> int:
        hash2 = 1 + (hash1 % (hash_size - 1))  # so this goes at least 1, where hash2 is multiplied by probe
        return (hash1 + probe * hash2) % hash_size

    @staticmethod
    def separate_chaining(hash1: int, probe: int, hash_size: int) -> int:
        # This is a placeholder method, sufficient for conditional execution of 
        #  class method defined behaviors
        #  (by default, collision_avoidance='separate chaining')
        pass

    @staticmethod
    def prime_probing(hash1: int, probe: int, hash_size: int) -> int:
        current_prime = HashTable.get_next_prime(2)
        for p in range(probe):
            current_prime = HashTable.get_next_prime(current_prime)
        return (hash1 + current_prime) % hash_size
    
    @staticmethod
    def three_halves_probing(hash1: int, probe: int, hash_size: int) -> int:
        return (hash1 + int(probe**(3 / 2))) % hash_size
    
    @staticmethod
    def to_eulers_number(hash1: int, probe: int, hash_size: int) -> int:
        return (hash1 + int(probe**(math.e))) % hash_size
    
    @staticmethod
    def to_eulers_number_non_even(hash1: int, probe: int, hash_size: int) -> int:
        to_e_non_even = (hash1 + int(probe**(math.e))) % hash_size
        return (to_e_non_even if (to_e_non_even % 2 != 0) else (to_e_non_even + 1)) % hash_size
    
    @staticmethod
    def cubic_probing(hash1: int, probe: int, hash_size: int) -> int:
        return (hash1 + probe**3) % hash_size
    
    @staticmethod
    def exponential_probing(hash1: int, probe: int, hash_size: int) -> int:
        return (hash1 + int(math.exp(float(probe)))) % hash_size
    
    @staticmethod
    def quartic_probing(hash1: int, probe: int, hash_size: int) -> int:
        return (hash1 + probe**4) % hash_size
    
    @staticmethod
    def quintic_probing(hash1: int, probe: int, hash_size: int) -> int:
        return (hash1 + probe**5) % hash_size
    
    @staticmethod
    def sextic_probing(hash1: int, probe: int, hash_size: int) -> int:
        return (hash1 + probe**6) % hash_size
    
    @staticmethod
    def septic_probing(hash1: int, probe: int, hash_size: int) -> int:
        return (hash1 + probe**7) % hash_size
    
    @staticmethod
    def octic_probing(hash1: int, probe: int, hash_size: int) -> int:
        return (hash1 + probe**8) % hash_size
    
    @staticmethod
    def nonic_probing(hash1: int, probe: int, hash_size: int) -> int:
        return (hash1 + probe**9) % hash_size
    
    @staticmethod
    def decic_probing(hash1: int, probe: int, hash_size: int) -> int:
        return (hash1 + probe**10) % hash_size
    
    @staticmethod
    def to_11_probing(hash1: int, probe: int, hash_size: int) -> int:
        return (hash1 + probe**11) % hash_size

    @staticmethod
    def to_12_probing(hash1: int, probe: int, hash_size: int) -> int:
        return (hash1 + probe**12) % hash_size

    @staticmethod
    def to_13_probing(hash1: int, probe: int, hash_size: int) -> int:
        return (hash1 + probe**13) % hash_size
    
    @staticmethod
    def to_14_probing(hash1: int, probe: int, hash_size: int) -> int:
        return (hash1 + probe**14) % hash_size
    
    @staticmethod
    def to_15_probing(hash1: int, probe: int, hash_size: int) -> int:
        return (hash1 + probe**15) % hash_size
    
    @staticmethod
    def to_16_probing(hash1: int, probe: int, hash_size: int) -> int:
        return (hash1 + probe**16) % hash_size
    
    @staticmethod
    def to_17_probing(hash1: int, probe: int, hash_size: int) -> int:
        return (hash1 + probe**17) % hash_size
    
    @staticmethod
    def to_18_probing(hash1: int, probe: int, hash_size: int) -> int:
        return (hash1 + probe**18) % hash_size
    
    @staticmethod
    def to_19_probing(hash1: int, probe: int, hash_size: int) -> int:
        return (hash1 + probe**19) % hash_size
    
    @staticmethod
    def to_20_probing(hash1: int, probe: int, hash_size: int) -> int:
        return (hash1 + probe**20) % hash_size
    
# ## # # #  #  #  #
    def __init__(self, size, collision_avoidance: str = 'separate chaining', initial_data: list[tuple] = []) -> None:
        # False represents never filled, True represents removed; filled: tuple (key, value) or SeparateNode
        # This behavior is consistent across all collision avoidance techniques, were a method to be implemented to switch techniques, it would work, but that wouldn't matter, as the table would need to be rehashed
        #  and actually as I think about it further, were the table not reset when rehashing, there would be a loop of rehashing
        if size < 2:
            size = 2
        self.probe_distances = []
        self.retrieve_time = 0
        self.insert_time = 0
        self.probe_time = 0
        self.collision_count_by_hashsize = []
        self.collision_count = 0
        self.rehash_count = 0
        self.hash_table = [None if collision_avoidance.startswith('sepa') else False for i in range(size)]  # self.insert: self.hash_table[current] = (key, value)
        self.load_factor_num = 0
        self.load_factor_div = len(self.hash_table)
        self.rehash_next_size = lambda p: 2 * len(p)  # double the size of the hash table
        # self.rehash_next_size = lambda p: int(len(p)**(3 / 2))
        self.collision_avoidance_string = collision_avoidance
        if collision_avoidance.lower().startswith('linear'):
            self.probe_function = self.linear_probing
        elif collision_avoidance.lower().startswith('quad'):
            self.probe_function = self.quadratic_probing
        elif collision_avoidance.lower().startswith('double'):
            self.probe_function = self.double_hashing
        elif collision_avoidance.lower().startswith('sep') and collision_avoidance.lower() != 'septic':
            self.probe_function = self.separate_chaining
        elif collision_avoidance.lower().startswith('prime'):
            self.probe_function = self.prime_probing
        elif collision_avoidance.lower().startswith('3'):
            self.probe_function = self.three_halves_probing
        elif collision_avoidance.lower().count('euler') > 0 and collision_avoidance.lower().count('even') == 0:
            self.probe_function = self.to_eulers_number
        elif collision_avoidance.lower().count('euler') > 0 and collision_avoidance.lower().count('even') > 0 or collision_avoidance == '^e 2':
            self.probe_function = self.to_eulers_number_non_even
        elif collision_avoidance.lower().count('cubic') > 0:
            self.probe_function = self.cubic_probing
        elif collision_avoidance.lower().count('exp') > 0:
            self.probe_function = self.exponential_probing
        elif collision_avoidance.lower().count('quart') > 0:
            self.probe_function = self.quartic_probing
        elif collision_avoidance.lower().count('quint') > 0:
            self.probe_function = self.quintic_probing
        elif collision_avoidance.lower().count('sextic') > 0:
            self.probe_function = self.sextic_probing
        elif collision_avoidance.lower().count('septic') > 0:
            self.probe_function = self.septic_probing
        elif collision_avoidance.lower().count('octic') > 0:
            self.probe_function = self.octic_probing
        elif collision_avoidance.lower().count('nonic') > 0:
            self.probe_function = self.nonic_probing
        elif collision_avoidance.lower().count('decic') > 0:
            self.probe_function = self.decic_probing
        elif collision_avoidance.lower().count('11') > 0:
            self.probe_function = self.to_11_probing
        elif collision_avoidance.lower().count('12') > 0:
            self.probe_function = self.to_12_probing
        elif collision_avoidance.lower().count('13') > 0:
            self.probe_function = self.to_13_probing
        elif collision_avoidance.lower().count('14') > 0:
            self.probe_function = self.to_14_probing
        elif collision_avoidance.lower().count('15') > 0:
            self.probe_function = self.to_15_probing
        elif collision_avoidance.lower().count('16') > 0:
            self.probe_function = self.to_16_probing
        elif collision_avoidance.lower().count('17') > 0:
            self.probe_function = self.to_17_probing
        elif collision_avoidance.lower().count('18') > 0:
            self.probe_function = self.to_18_probing
        elif collision_avoidance.lower().count('19') > 0:
            self.probe_function = self.to_19_probing
        elif collision_avoidance.lower().count('20') > 0:
            self.probe_function = self.to_20_probing
        # elif collision_avoidance.lower().count('rand') > 0:
        #     self.probe_function = self.rand_hash_probing
        else:
            self.probe_function = self.separate_chaining
        # self.rand_key_dict = HashTable(1)
        # self.rand_key_set = HashTable(1)  # see ExperimentalHashTable
        if initial_data != []:
            for datum in initial_data:
                self.insert(datum[0], datum[1])

    def __str__(self) -> str:
        display_string = f"HashTable, collision_avoidance: {self.collision_avoidance_string}\n"
        for index in range(len(self.hash_table)):
            display_string += f"Index {index}: {str(self.hash_table[index])}\n"
            # detect first occurrence of all remaining values == False, update string accordingly with '...' and last row
            if not self.hash_table[index] and\
                  all(value == self.hash_table[index] for value in self.hash_table[index + 1:]):
                display_string += f"...\nIndex {len(self.hash_table) - 1}: {self.hash_table[-1]}\n"
                break  # the string is complete
        return display_string

    def display(self) -> None:
        print(self)

    def get_all(self) -> list[tuple[any, any]]:
        """returns all_tuples without removing """
        all_tuples = []
        for each in self.hash_table:
            if isinstance(each, HashTable.SeparateNode):  # ignores any type except chains
                all_tuples.extend([every.node_tuple for every in each.get_sub_list()])
            else:
                if each and not each is True:  # an object other than bool(object)->False or True
                    all_tuples.append(each)
        return all_tuples

    def get_keys(self) -> list:
        return [each[0] for each in self.get_all()]

    def rehash_table(self, force_rehash: bool =False) -> bool:  # -> float ? # return time for each function
        if self.probe_function == self.separate_chaining:
            rehash_bool = self.load_factor_num / self.load_factor_div >= 1
        else:
            rehash_bool = self.load_factor_num / self.load_factor_div >= 0.5
        # if self.probe_function == self.separate_chaining:
        #     rehash_bool = sum([0 if not isinstance(each, HashTable.SeparateNode) else len(each) for each in self.hash_table]) / self.load_factor_div >= 1
        # else:
        #     rehash_bool = sum([int(bool(each)) for each in self.hash_table]) / self.load_factor_div >= 0.5
        if rehash_bool or force_rehash:
            self.collision_count_by_hashsize.append((self.load_factor_div, self.collision_count))
            self.collision_count = 0
            # print(f"rehashing from {len(self.hash_table)} to {self.get_next_prime(2 * len(self.hash_table))}")
            current_data = self.get_all()
            # print(f"current_data: {current_data}")
            self.load_factor_num = 0  # count up again from 0 in each .insert()
            self.load_factor_div = self.get_next_prime(self.rehash_next_size(self.hash_table))
            self.hash_table = [None if self.probe_function is self.separate_chaining else False for r in range(self.load_factor_div)]
            for each in current_data:
                self.insert(each[0], each[1])
        return rehash_bool or force_rehash
    
    def de_tombstone_table(self) -> None:
        current_data = self.get_all()
        self.hash_table = [False for i in range(self.get_next_prime(len(current_data)))]
        for each in current_data:
            self.insert(each[0], each[1])

    def hash(self, key) -> int:
        # if isinstance(key, int):
        #     return key % len(self.hash_table)
        # else:
        return hash(key) % len(self.hash_table)  # This should preclude need for string_xor_hash method elsewhere
    
    # def extend_update(self, key, value: any) -> None:
    #     if self.contains(key):
    #         retrieval = self.retrieve(key)  # handled in a subclass UserHashTable(ExperimentalHashTable)


    def probe(self, hash_key, probe) -> int:
        self.collision_count += 1
        return self.probe_function(hash_key, probe, len(self.hash_table))  # TODO Add traversal tracking to SeparateNode (?)
    
    def insert(self, key, value: any) -> None:
        self.probe_distances.append(['insert', 0])
        start_time = time.time()
        self.load_factor_num += 1  # removal leaves a value that must be traversed, so this is not decremented, however rehashing resets this to 0 before inserting all data
        self.rehash_table()  # conditional within method, re λ
        hash_key = self.hash(key)
        start_time_probe = time.time()
        if self.probe_function == self.separate_chaining:
            if not isinstance(self.hash_table[hash_key], HashTable.SeparateNode):
                self.hash_table[hash_key] = HashTable.SeparateNode((key, value))
            else:
                # adds to front of list
                self.collision_count += 1
                self.hash_table[hash_key] = HashTable.SeparateNode((key, value), self.hash_table[hash_key])
            self.probe_time += time.time() - start_time_probe
        else:
            current = hash_key
            probe = 0
            start_time_probe = time.time()
            while self.hash_table[current]:
                probe += 1
                current = self.probe(hash_key, probe)
                if probe >= len(self.hash_table) // 2:  # how often does this happen?
                    print("probe greater than or equal to N // 2")
                    self.rehash_table(True)
                    self.insert(key, value)
                    break
                # if probe >= 0.5*(1 + 1/((1 - self.load_factor_num / self.load_factor_div)**2)):
                # this is a condition from AD325 slides on Hash Tables, regarding the probe cost of a linear search
            else:
                self.hash_table[current] = (key, value)
            self.probe_time += time.time() - start_time_probe
        self.insert_time += time.time() - start_time

    def retrieve(self, key) -> tuple[any, any]:   # retrieves a (key, value) (removes the tuple or containing object from data structure (with garbage collection))
        self.probe_distances.append(['retrieve', 0])
        start_time = time.time()
        hash_key = self.hash(key)
        retrieval = None
        if self.probe_function == self.separate_chaining:
            current = self.hash_table[hash_key]
            if not isinstance(current, bool|None):  #  or not current.contains(key) (not needed)
                if current.node_tuple[0] == key:
                    retrieval = current.node_tuple
                    self.hash_table[hash_key] = current.next
                    self.probe_distances[-1][-1] += 1
                else:
                    preceding = current  # traverse the nodes  #
                    current = current.next
                    while isinstance(current, HashTable.SeparateNode):  # ends when current is not a node
                        self.collision_count += 1
                        self.probe_distances[-1][-1] += 1
                        if current.node_tuple[0] == key:
                            retrieval = current.node_tuple
                            preceding.next = current.next
                            break
                        preceding = current
                        current = current.next  #              #
                # return retrieval  # tabbing this back one indentation resulted in bug fix (all users were getting J==0.0, and no retrieval during loading data resulted in anything but None)
        else:
            current = hash_key
            probe = 0
            while self.hash_table[current]:
                if isinstance(self.hash_table[current], tuple):
                    if self.hash_table[current][0] == key:
                        break
                probe += 1
                self.probe_distances[-1][-1] += 1
                current = self.probe(hash_key, probe)  # collision_count += 1, in probe
            # either probing ended on a False, or a value with key == key
            if self.hash_table[current]:
                retrieval = self.hash_table[current]
                self.hash_table[current] = True  # represents empty after removal
        self.retrieve_time += time.time() - start_time
        return retrieval
        
    def contains(self, key) -> bool:  # such as for computing intersection of items
        self.probe_distances.append(['contains', 0])
        hash_key = self.hash(key)
        if self.probe_function == self.separate_chaining:
            current = self.hash_table[hash_key]
            if not isinstance(current, bool|None):
                # contents_tuple = current.contains(key)
                # self.probe_distances[-1][-1] += contents_tuple[1]
                # return contents_tuple[0]
                return current.contains(key)
        else:
            current = hash_key
            probe = 0
            while self.hash_table[current]:
                if not isinstance(self.hash_table[current], bool|None) and self.hash_table[current][0] == key:
                    break
                probe += 1
                self.probe_distances[-1][-1] += 1
                current = self.probe(hash_key, probe)
            # either probing ended on a False, or a tuple (key, value) with key == key
            # that is, probing will not end on a True, therefore:
            return False if not self.hash_table[current] else True  # True indicates (key == key)

    class SeparateNode:
        """a recursively defined linked list (node)"""
        # separate chaining using simply a list is a good idea- could later make it sorted and add binary search- anyway, here's this
        def __init__(self, node_tuple: tuple[int, any], next=None) -> None:  # True as next placeholder makes structures resulting from use of this consistent with containing class behavior 
            self.node_tuple = node_tuple
            self.next = next
        
        def __len__(self) -> int:
            if not isinstance(self.next, bool|None):
                return 1 + len(self.next)
            else:
                return 1
            
        def __str__(self) -> str:
            return str(self.node_tuple) + ' ⭢ ' + str(self.next)

        def get_sub_list(self) -> list[tuple[int,any]]:
            """includes self"""
            sub_list = [self]
            if not isinstance(self.next, bool|None):
                sub_list.extend(self.next.get_sub_list())
            return sub_list

        def get_keys(self) -> list:
            keys_list = [self.node_tuple[0]]
            if not isinstance(self.next, bool|None):
                keys_list.extend(self.next.get_keys())
            return keys_list
        
        def contains(self, key) -> bool:
            if self.node_tuple[0] == key:
                return True # , 1
            else:
                if self.next is not None:
                    # contains_return = self.next.contains(key)
                    # return contains_return[0], contains_return[1] + 1  # False if contains_return[0] is None else 
                    return self.next.contains(key)
                else:
                    return False  #, 1

