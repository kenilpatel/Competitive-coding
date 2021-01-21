class Solution(object):
    def get(self):
        return 0

    def getl(self):
        return []

    def mostVisitedPattern(self, username, timestamp, website):
        """
        :type username: List[str]
        :type timestamp: List[int]
        :type website: List[str]
        :rtype: List[str]
        """
        count_dict = defaultdict(self.get)
        record = []
        s = "home.depot"
        for i in range(0, len(username)):
            record.append([username[i], timestamp[i], website[i]])
        record = sorted(record, key=lambda x: x[1])
        # print(record)
        user_seq = defaultdict(self.getl)
        for r in record:
            user_seq[r[0]].append(r[2])
        # print(user_seq)
        for u in user_seq.values():
            seq = u
            local_seq = set()
            for i in range(0, len(seq)):
                for j in range(i + 1, len(seq)):
                    for k in range(j + 1, len(seq)):
                        local_seq.add(seq[i] + "." + seq[j] + "." + seq[k])
            for s in local_seq:
                count_dict[s] += 1

        mc = None
        ans = None
        # print(count_dict)
        for key in count_dict.keys():
            if ans == None:
                ans = key
                mc = count_dict[key]
            else:
                if mc < count_dict[key]:
                    ans = key
                    mc = count_dict[key]
                elif mc == count_dict[key]:
                    if ans > key:
                        ans = key
        return ans.split(".")
