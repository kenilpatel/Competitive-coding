class FirstUnique(object):
    count_dict = None
    q = None

    def get(self):
        return 0

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.q = []
        self.count_dict = defaultdict(self.get)
        for i in nums:
            self.count_dict[i] += 1
            self.q.append(i)

    def showFirstUnique(self):
        """
        :rtype: int
        """
        while self.q and self.count_dict[self.q[0]] != 1:
            self.q.pop(0)
        if self.q:
            return self.q[0]
        else:
            return -1

    def add(self, value):
        """
        :type value: int
        :rtype: None
        """
        self.count_dict[value] += 1
        self.q.append(value)


# Your FirstUnique object will be instantiated and called as such:
# obj = FirstUnique(nums)
# param_1 = obj.showFirstUnique()
# obj.add(value)
