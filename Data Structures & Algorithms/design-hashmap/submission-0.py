class MyHashMap:
    def __init__(self):
        # Create an array of size 1,000,001 initialized with -1
        self.map = [-1] * 1000001

    def put(self, key: int, value: int) -> None:
        # Just update the value at the specific index
        self.map[key] = value

    def get(self, key: int) -> int:
        # Since empty slots are already -1, this perfectly satisfies the rules
        return self.map[key]

    def remove(self, key: int) -> None:
        # To "remove" it, we just reset that index back to -1
        self.map[key] = -1