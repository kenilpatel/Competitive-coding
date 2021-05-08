class Solution {
    public int minSteps(String s, String t) {
        int steps = 0;
        int n = s.length();
        Map<Character,Integer> map = new HashMap();
        for(int i=0;i<n;i++)
        {
            char c = s.charAt(i);
            map.put(c,map.getOrDefault(c,0) + 1);
        }
        for(int i=0;i<n;i++)
        {
            char c = t.charAt(i);
            map.put(c,map.getOrDefault(c,0) - 1);
        }
        for(Character key:map.keySet())
        {
            int count = map.get(key);
            if(count >= 0)
            {
                steps += count;
            }
        }
        return steps;
    }
}