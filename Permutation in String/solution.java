class Solution {
    public boolean check(int[] arr1,int[] arr2)
    {
        for(int i=0;i<26;i++)
        {
            if(arr1[i] != arr2[i])
            {
                return false;
            }
        }
        return true;
    }
    public boolean checkInclusion(String s1, String s2) {
        int i = 0;
        int j = s1.length();
        int count1[] = new int[26];
        int count2[] = new int[26];
        if(s1.length() > s2.length())
        {
            return false;
        }
        for(int ix=0;ix<s1.length();ix++)
        {
            int pos = s1.charAt(ix) - 97;
            count1[pos] += 1;
        }
        for(int ix=0;ix<s1.length();ix++)
        {
            int pos = s2.charAt(ix) - 97;
            count2[pos] += 1;
        }
        if(check(count1,count2))
        {
            return true;
        }
        while(j < s2.length())
        {
            int pos1 = s2.charAt(i) - 97;
            int pos2 = s2.charAt(j) - 97;
            count2[pos1]--;
            count2[pos2]++;
            if(check(count1,count2))
            {
                return true;
            }
            i++;
            j++;
        }
        return false;
    }
}