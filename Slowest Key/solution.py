class Solution(object):
    def slowestKey(self, releaseTimes, keysPressed):
        """
        :type releaseTimes: List[int]
        :type keysPressed: str
        :rtype: str
        """
        releaseTimes = [0] + releaseTimes
        time = releaseTimes[1]
        key = keysPressed[0]
        for i in range(2, len(releaseTimes)):
            new_t = releaseTimes[i] - releaseTimes[i - 1]
            # print(new_t)
            if time < new_t:
                time = new_t
                key = keysPressed[i - 1]
            if time == new_t:
                if key < keysPressed[i - 1]:
                    key = keysPressed[i - 1]
        return key
