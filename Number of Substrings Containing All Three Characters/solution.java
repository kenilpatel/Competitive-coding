class Solution {
    public int numberOfSubstrings(String s) {
        int a = -1;
        int b = -1;
        int c = -1;
        int ans = 0;
        int place = -1;
        for(int i=0;i<s.length();i++)
        {
            char c1 = s.charAt(i);
            if(c1 == 'a')
            {
                int idx = Math.min(b,c);
                a = i;
                ans += idx - place;
            }
            else if(c1 == 'b')
            {
                int idx = Math.min(a,c);
                b = i;
                ans += idx - place;
            }
            else if(c1 == 'c')
            {
                int idx = Math.min(a,b);
                c = i;
                ans += idx - place;
            }
        }
        return ans;
    }
}