class Solution {
    public boolean check(String s)
    {
        return s.equals(new StringBuilder(s).reverse().toString());
    }
    public boolean check(String a,String b)
    {
        int i=0;
        int j=b.length() - 1;
        while(i < j && a.charAt(i) == b.charAt(j))
        {
            i++;
            j--;
        }
        String pre = a.substring(0,i);
        String post = b.substring(i);
        String pre1 = a.substring(0,a.length() - i);
        String post1 = b.substring(a.length() - i);
        return check(pre + post) || check(pre1 + post1);

    }
    public boolean checkPalindromeFormation(String a, String b) {
        return check(a) || check(b) || check(a,b) || check(b,a);
    }
}