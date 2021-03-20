class Solution(object):
    def validSquare(self, p1, p2, p3, p4):
        """
        :type p1: List[int]
        :type p2: List[int]
        :type p3: List[int]
        :type p4: List[int]
        :rtype: bool
        """
        dist = []
        p1p2 = float(((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2) ** 0.5)
        p1p3 = float(((p1[0] - p3[0]) ** 2 + (p1[1] - p3[1]) ** 2) ** 0.5)
        p1p4 = float(((p1[0] - p4[0]) ** 2 + (p1[1] - p4[1]) ** 2) ** 0.5)
        p2p3 = float(((p2[0] - p3[0]) ** 2 + (p2[1] - p3[1]) ** 2) ** 0.5)
        p2p4 = float(((p2[0] - p4[0]) ** 2 + (p2[1] - p4[1]) ** 2) ** 0.5)
        p3p4 = float(((p3[0] - p4[0]) ** 2 + (p3[1] - p4[1]) ** 2) ** 0.5)
        size = set((p1p2, p1p3, p1p4, p2p3, p2p4, p3p4))
        print(size)
        if len(size) != 2:
            return False
        x, y = size
        if x > y:
            x, y = y, x
        if abs(float((x ** 2 + x ** 2) ** 0.5) - float(y)) <= 0.00001:
            return True
        else:
            return False
