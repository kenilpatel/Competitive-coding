class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        top = " "
        size = 0
        cnt = 1
        for char in chars:
            if char != top:
                if top != " ":
                    chars[size] = top
                    size += 1
                    if cnt != 1:
                        for x in str(cnt):
                            chars[size] = x
                            size += 1
                    top = char
                    cnt = 1
                else:
                    top = char
                    cnt = 1
            else:
                cnt += 1
        if top != " ":
            chars[size] = top
            size += 1
            if cnt != 1:
                for x in str(cnt):
                    chars[size] = x
                    size += 1
        return size
