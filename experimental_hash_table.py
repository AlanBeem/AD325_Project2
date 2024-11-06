import time
from hash_table import HashTable
from random import SystemRandom


class ExperimentalHashTable(HashTable):
   ## not static, but similar to those functions in super
    def rand_hash(self, key: int) -> int:
        if not self.rand_key_dict.contains(key):
            rand_16bits = SystemRandom().getrandbits(16)
            self.rand_key_set.insert(rand_16bits, rand_16bits)
            self.rand_key_dict.insert(key, rand_16bits)
        dicted_tuple = self.rand_key_dict.retrieve(key)
        self.rand_key_dict.insert(dicted_tuple[0], dicted_tuple[1])
        return dicted_tuple[1]  # a value of rand_16bits
    
    def rand_hash_probing(self, hash1: int, probe: int, hash_size: int) -> int:
        hash2 = self.rand_hash(probe)
        return (hash1 + hash2) % hash_size
   ##
    def __init__(self, size: int, collision_avoidance: str ='separate chaining', initial_data: list[tuple[any, any]] =[]):
        super().__init__(size, collision_avoidance, initial_data)
        if collision_avoidance.lower().count('rand') > 0:
            self.probe_function = self.rand_hash_probing
        self.rand_key_dict = HashTable(1)
        self.rand_key_set = HashTable(1)
        self.rehash_report = [len(self.hash_table)]
    
    def probe(self, hash_key: int, probe: int) -> int:
        start_time = time.time()
        if self.probe_function == self.rand_hash_probing:
            self.collision_count_by_hashsize.append(len(self.hash_table))
            self.collision_count += 1
            self.probe_time += time.time() - start_time
            return self.probe_function(hash_key, probe, len(self.hash_table))
        else:
            return super().probe(hash_key, probe)
    
    def rehash_table(self, force_rehash = False):
        if super().rehash_table(force_rehash):
            self.rehash_report.append(len(self.hash_table))

