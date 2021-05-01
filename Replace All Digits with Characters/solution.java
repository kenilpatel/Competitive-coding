class Solution {
    public String replaceDigits(String s) {
        String ans = "";
        int prev = 0;
        for(int i=0;i<s.length();i++)
        {
            char c = s.charAt(i);
            if(Character.isDigit(c))
            {
                int x = Integer.parseInt(String.valueOf(c));
                int nw = prev + x;
                char new_c = (char)nw;
                ans += new_c;
            }
            else
            {
                prev = c;
                ans += c;
            }
        }
        return ans;
    }
}