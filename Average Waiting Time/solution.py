class Solution(object):
    def averageWaitingTime(self, customers):
        """
        :type customers: List[List[int]]
        :rtype: float
        """
        time = [customers[0][0] + customers[0][1]]
        arrival = [customers[0][0]]
        wait_sum = 0
        for i in range(1,len(customers)):
            top = time[-1]
            if top > customers[i][0]:
                time.append(top + customers[i][1])
            else:
                time.append(customers[i][0] + customers[i][1])
            arrival.append(customers[i][0])
        difference = []
        zip_object = zip(time, arrival)
        for list1_i, list2_i in zip_object:
            difference.append(list1_i-list2_i)
        return float(float(sum(difference))/float(len(customers)))

