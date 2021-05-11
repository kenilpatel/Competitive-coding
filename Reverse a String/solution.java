class Reverse
{
    // Complete the function
    // str: input string
    public static String reverseWord(String str)
    {
        char[] c = str.toCharArray();
        int i=0;
        int j=c.length - 1;
        while(i < j)
        {
            char temp = c[i];
            c[i] = c[j];
            c[j] = temp;
            i++;
            j--;
        }
        return new String(c);
    }
}