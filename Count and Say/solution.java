class Solution {
    public String say(String s)
    {
        int len = s.length();
        char prev = s.charAt(0);
        int count = 1;
        String ans = "";
        for(int i=1;i<len;i++)
        {
            if(prev == s.charAt(i))
            {
                count++;
            }
            else
            {
                ans += String.valueOf(count) + String.valueOf(prev);
                prev = s.charAt(i);
                count = 1;
            }
        }

        ans += String.valueOf(count) + String.valueOf(prev);
        return ans;
    }
    public String countAndSay(int n) {
        if(n == 1)
        {
            return "1";
        }
        else
        {
            return say(countAndSay(n - 1));
        }
    }

}