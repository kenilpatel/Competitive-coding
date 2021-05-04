class Solution {
    public int longestSubsequence(int[] arr, int difference) {
        int len[] = new int[arr.length];
        Map<Integer,Integer> map = new HashMap();
        for(int i=0;i<arr.length;i++)
        {
            len[i] = 1;
        }
        for(int i=0;i<arr.length;i++)
        {

            int idx = map.getOrDefault(arr[i] - difference,-1);
            if(idx != -1)
            {
                len[i] = len[idx] + 1;
            }
            map.put(arr[i],i);
        }
        int max = 0;
        for(int i=0;i<arr.length;i++)
        {
            max = Math.max(max,len[i]);
        }
        return max;
    }
}