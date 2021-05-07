class Solution {
    public String shiftingLetters(String S, int[] shifts) {
        int n = shifts.length;
        StringBuilder ans = new StringBuilder();
        shifts[n - 1] %= 26;
        for(int i=n-2;i>=0;i--)
        {
            shifts[i] += shifts[i + 1] % 26;
        }
        for(int i=0;i<n;i++)
        {
            int pos = (int)S.charAt(i) - 97;
            int next = (pos + shifts[i]) % 26 + 97;
            ans.append((char)next);
        }
        return ans.toString();
    }
}