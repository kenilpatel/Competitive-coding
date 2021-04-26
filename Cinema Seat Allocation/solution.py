class Solution(object):
    def maxNumberOfFamilies(self, n, reservedSeats):
        """
        :type n: int
        :type reservedSeats: List[List[int]]
        :rtype: int
        """
        used_seat = defaultdict(lambda:set())
        def check(rownum,i,j):
            used = used_seat[rownum]
            for no in range(i,j + 1):
                if no in used:
                    return False
            return True
                
        cur = 2 * n 
        check_set = set() 
        for row,seat in reservedSeats:
            check_set.add(row)
            used_seat[row].add(seat)
        for rn in check_set:
            b25 = check(rn,2,5)
            b47 = check(rn,4,7)
            b69 = check(rn,6,9)
            if b25 and b69:
                pass
            elif b25 and not(b69):
                cur -= 1
            elif not(b25) and b69:
                cur -= 1
            elif not(b25) and not(b69):
                if b47:
                    cur -= 1
                else:
                    cur -= 2
        return cur
