class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.hashmap = {}
        self.q = collections.deque()

    def get(self, key: int) -> int:
        if key not in self.q:
            return -1
        if key in self.q:
            self.q.remove(key)
        self.q.append(key)
        if len(self.q) > self.capacity:
            self.q.popleft()
        return self.hashmap[key]

    def put(self, key: int, value: int) -> None:
        if key in self.hashmap:
            self.q.remove(key)
        elif len(self.q) >= self.capacity:
            lru = self.q.popleft()
            del self.hashmap[lru]

        self.q.append(key)
        self.hashmap[key] = value
    
    # {1:10, 2:20, 3:30}
    # [3,2]
