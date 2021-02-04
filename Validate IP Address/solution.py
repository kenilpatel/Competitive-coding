class Solution(object):
    s = None

    def validIPAddress(self, IP):
        """
        :type IP: str
        :rtype: str
        """
        s = set(('A', 'B', 'C', 'D', 'E', 'F', 'a', 'b', 'c', 'd', 'e',
                 'f', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'))
        segment = IP.split(".")
        if len(segment) == 1:
            segment = IP.split(":")
        if len(segment) == 4:
            try:
                for i in segment:
                    x = int(i)
                    if x >= 0 and x <= 255 and len(str(x)) == len(i):
                        pass
                    else:
                        return "Neither"
                return "IPv4"
            except:
                return "Neither"
        elif len(segment) == 8:
            for seg in segment:
                if len(seg) >= 1 and len(seg) <= 4:
                    pass
                else:
                    return "Neither"
                for char in seg:
                    if char not in s:
                        return "Neither"
            return "IPv6"
        else:
            return "Neither"
