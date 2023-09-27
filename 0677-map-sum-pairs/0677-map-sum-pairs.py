class MapSum:

    def __init__(self):
        self.map = {}

    def insert(self, key: str, val: int) -> None:
        self.map[key] = val

    def sum(self, prefix: str) -> int:
        total = 0
        # 딕셔너리의 모든 키-값 쌍을 반복
        for key, value in self.map.items():
            if key.startswith(prefix):
                total += value
        return total    


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)