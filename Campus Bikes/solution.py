import heapq


class Solution(object):
    def assignBikes(self, workers, bikes):
        """
        :type workers: List[List[int]]
        :type bikes: List[List[int]]
        :rtype: List[int]
        """
        n = len(workers)
        m = len(bikes)
        pairs = []
        heapq.heapify(pairs)
        bike_used = set()
        ans = [-1] * n
        for worker_i in range(0, n):
            for bike_i in range(0, m):
                a, b = workers[worker_i]
                x, y = bikes[bike_i]
                new_dist = abs(a - x) + abs(y - b)
                pairs.append((new_dist, worker_i, bike_i))
        pairs = sorted(pairs)
        i = 0
        while n > 0:
            top = pairs[i]
            worker = top[1]
            bike = top[2]
            if ans[worker] == -1 and bike not in bike_used:
                ans[worker] = bike
                bike_used.add(bike)
                n -= 1
            i += 1
        return ans
