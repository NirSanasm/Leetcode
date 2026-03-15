1class Node:
2    def __init__(self, key, value):
3        self.key = key
4        self.value = value
5        self.prev = None
6        self.next = None
7
8
9class LRUCache:
10
11    def __init__(self, capacity: int):
12        self.capacity = capacity
13        self.cache = {}
14
15        self.head = Node(0,0)
16        self.tail = Node(0,0)
17
18        self.head.next = self.tail
19        self.tail.prev = self.head
20
21
22    def remove(self, node):
23        prev = node.prev
24        nxt = node.next
25
26        prev.next = nxt
27        nxt.prev = prev
28
29
30    def insert(self, node):
31        prev = self.tail.prev
32        nxt = self.tail
33
34        prev.next = node
35        node.prev = prev
36
37        node.next = nxt
38        nxt.prev = node
39
40
41    def get(self, key: int) -> int:
42        if key in self.cache:
43
44            node = self.cache[key]
45            self.remove(node)
46            self.insert(node)
47
48            return node.value
49
50        return -1
51
52
53    def put(self, key: int, value: int) -> None:
54
55        if key in self.cache:
56            self.remove(self.cache[key])
57
58        node = Node(key,value)
59        self.cache[key] = node
60        self.insert(node)
61
62        if len(self.cache) > self.capacity:
63            lru = self.head.next
64            self.remove(lru)
65            del self.cache[lru.key]
66
67# Your LRUCache object will be instantiated and called as such:
68# obj = LRUCache(capacity)
69# param_1 = obj.get(key)
70# obj.put(key,value)