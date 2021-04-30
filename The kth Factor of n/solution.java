class Solution {
    public int kthFactor(int n, int k) {
        List<Integer> arr = new ArrayList<Integer>();
        int idx = 1;
        for(int i=1;i<=n;i++)
        {
            if(n % i == 0)
            {
                if(idx == k)
                {
                    return i;
                }
                arr.add(i);
                idx += 1;
            }
        }
        return -1;

    }
}