class UndergroundSystem(object):
    idd = None
    journey = None

    def get(self):
        return []

    def __init__(self):
        self.idd = {}
        self.journey = defaultdict(self.get)

    def checkIn(self, id, stationName, t):
        """
        :type id: int
        :type stationName: str
        :type t: int
        :rtype: None
        """
        self.idd[id] = [stationName, t]

    def checkOut(self, id, stationName, t):
        """
        :type id: int
        :type stationName: str
        :type t: int
        :rtype: None
        """
        f = self.idd[id][0]
        time = self.idd[id][1]
        self.idd.pop(id)
        self.journey[(f, stationName)].append(t - time)

    def getAverageTime(self, startStation, endStation):
        """
        :type startStation: str
        :type endStation: str
        :rtype: float
        """

        s = sum(self.journey[(startStation, endStation)])
        l = len(self.journey[(startStation, endStation)])
        # print(startStation,endStation,s,l)
        if l == 0:
            return 0
        else:
            return float(s) / float(l)


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)
