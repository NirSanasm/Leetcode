1class MyHashSet:
2
3    def __init__(self):
4        self.items = set()
5        
6
7    def add(self, key: int) -> None:
8        self.items.add(key)
9        
10
11    def remove(self, key: int) -> None:
12        if key not in self.items:
13            return None
14        self.items.remove(key)
15        
16
17    def contains(self, key: int) -> bool:
18        if key in self.items:
19            return True
20        return False
21        
22
23
24# Your MyHashSet object will be instantiated and called as such:
25# obj = MyHashSet()
26# obj.add(key)
27# obj.remove(key)
28# param_3 = obj.contains(key)