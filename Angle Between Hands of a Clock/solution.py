class Solution(object):
    def angleClock(self, hour, minutes):
        """
        :type hour: int
        :type minutes: int
        :rtype: float
        """
        ini_dis = [0, 30, 60, 90, 120, 150, 180, 210, 240, 270, 300, 330]
        angle = abs(5.5 * minutes - ini_dis[hour % 12])
        return min(angle, 360 - angleClock)
