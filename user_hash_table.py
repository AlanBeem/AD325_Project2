import time
from experimental_hash_table import ExperimentalHashTable


class UserHashTable(ExperimentalHashTable):
    """UserHashTable modifies insert behavior in order to build value lists associated with particular keys,
    and this causes an empty-after-removal value (True) to be placed where the updated value was."""
    def insert(self, key, value: any) -> None:
        start_time = time.time()
        if self.contains(key):
            # self.collision_count += 1
            retrieved = self.retrieve(key)
            retrieved[1].append(value)
            value = retrieved[1]
        elif not isinstance(value, list):
                value = [value]
        self.insert_time += time.time() - start_time
        super().insert(key, value)  # (int, any) or (int, list[any])

