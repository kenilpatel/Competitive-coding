class Solution(object):
    def get(self):
        return -1

    def findMinFibonacciNumbers(self, k):
        """
        :type k: int
        :rtype: int
        """
        choices = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711, 28657, 46368, 75025, 121393, 196418, 317811,
                   514229, 832040, 1346269, 2178309, 3524578, 5702887, 9227465, 14930352, 24157817, 39088169, 63245986, 102334155, 165580141, 267914296, 433494437, 701408733]
        new_t = k
        step = 0
        while True:
            idx = bisect.bisect(choices, new_t)
            new_t = new_t - choices[idx - 1]
            step += 1
            if new_t == 0:
                break
        return step
