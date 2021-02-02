class TimeMap(object):
    tdict = None

    def getd(self):
        return []

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.tdict = defaultdict(self.getd)

    def set(self, key, value, timestamp):
        """
        :type key: str
        :type value: str
        :type timestamp: int
        :rtype: None
        """
        self.tdict[key].append((timestamp, value))

    def get(self, key, timestamp):
        """
        :type key: str
        :type timestamp: int
        :rtype: str
        """
        x = self.tdict[key]
        if len(x) == 0:
            return ""
        else:
            i = bisect.bisect(x, (timestamp, chr(127)))
            return x[i - 1][1] if i else ""


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
