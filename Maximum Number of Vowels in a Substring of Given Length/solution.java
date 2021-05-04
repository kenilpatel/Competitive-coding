class Solution {
    public int maxVowels(String s, int k) {
        Deque<Integer> dque = new ArrayDeque();
        int n = 0;
        int ans = 0;
        for(int i=0;i<s.length();i++)
        {
            if(s.charAt(i) == 'a' ||
              s.charAt(i) == 'e' ||
              s.charAt(i) == 'i' ||
              s.charAt(i) == 'o' ||
              s.charAt(i) == 'u')
            {
                while(n > 0 && i - dque.peekFirst() >= k)
                {
                    dque.pollFirst();
                    n--;
                }
                dque.addLast(i);
                n++;
                ans = Math.max(ans,n);
            }
        }
        return ans;
    }
}