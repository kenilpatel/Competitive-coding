class Solution {
    public int findKthLargest(int[] nums, int k) {
        PriorityQueue<Integer> pQueue =
             new PriorityQueue<Integer>(Collections.reverseOrder());
        for(int i=0;i<nums.length;i++)
        {
            pQueue.add(nums[i]);
        }
        int top = -1;
        while(k!=0)
        {
            top = pQueue.poll();
            k = k -1;
        }
        return top;
    }
}