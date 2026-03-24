1
2
3class Codec:
4
5    def __init__(self):
6        self.items = {}
7
8    def encode(self, longUrl: str) -> str:
9        """Encodes a URL to a shortened URL.
10        """
11        result = hash(longUrl)
12        self.items[result] = longUrl
13        return result
14
15
16
17
18        
19
20    def decode(self, shortUrl: str) -> str:
21        """Decodes a shortened URL to its original URL.
22        """
23
24        return self.items[shortUrl]
25        
26
27# Your Codec object will be instantiated and called as such:
28# codec = Codec()
29# codec.decode(codec.encode(url))