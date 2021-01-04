class Solution(object):
    def videoStitching(self, clips, T):
        """
        :type clips: List[List[int]]
        :type T: int
        :rtype: int
        """
        clips = sorted(clips, key=lambda x: x[0]*1000 + x[1])
        dictionary = {}
        for c in clips:
            dictionary[c[0]] = c
        uclips = dictionary.values()
        print(uclips)
        start = uclips[0][0]
        end = uclips[0][1]
        if start != 0:
            if T == 0:
                return 0
            return -1
        uclips = uclips[1:]
        tot = end
        count = 1
        while(len(uclips) != 0):
            if tot >= T:
                break
            best_index = -1
            for i in range(0, len(uclips)):
                if uclips[i][0] <= tot:
                    if best_index != -1:
                        if(uclips[i][1] > uclips[best_index][1]):
                            best_index = i
                    else:
                        best_index = i
            if best_index == -1:
                return -1
            print(uclips[best_index])
            end = uclips[best_index][1]
            tot = end
            count = count + 1
            uclips = uclips[best_index + 1:]
        print(tot)
        if tot >= T:
            return count
        else:
            return -1
