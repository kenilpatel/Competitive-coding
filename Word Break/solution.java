class Solution {
    public Map<String,Integer> dict;
    public Map<String,Boolean> memo;
    Solution()
    {
        this.dict = new HashMap<String,Integer>();
        this.memo = new HashMap<String, Boolean>();
    }
    public boolean wordBreak(String s, List<String> wordDict) {
        for(int i=0;i<wordDict.size();i++)
        {
            this.dict.put(wordDict.get(i), 1);
        }
        System.out.println(this.dict);
        return DP(s);
    }
    public boolean DP(String s)
    {
        // System.out.println("called for"+","+s);
        if(s.isEmpty())
        {
            return true;
        }
        if(s.length() == 1)
        {
            if(this.dict.containsKey(s))
            {
                this.memo.put(s,true);
                return true;
            }
            else
            {
                this.memo.put(s,false);
                return false;
            }

        }
        if(this.dict.containsKey(s))
        {
            this.memo.put(s,true);
            return true;
        }
        if(this.memo.containsKey(s))
        {
            return memo.get(s);
        }
        else
        {
            for(int i=1;i<s.length();i++)
            {
                boolean left = DP(s.substring(0,i));
                if(left==true)
                {
                    boolean right = DP(s.substring(i));
                    if(right==true)
                    {
                        this.memo.put(s,true);
                        return true;
                    }
                }
            }
            this.memo.put(s,false);
            return false;
        }
    }
}