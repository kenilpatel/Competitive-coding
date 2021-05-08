class Solution {
    public int clumsy(int N) {
        Deque<String> stack = new ArrayDeque();
        Deque<Integer> ans_stack = new ArrayDeque();
        char[] sign = {'*','/','+','-'};
        int len = 4;
        int idx = 0;
        for(int i=N;i>=2;i--)
        {
            stack.addLast(i + "");
            stack.addLast(sign[idx] + "");
            idx++;
            idx %= len;
        }
        stack.add(1 + "");
        int ans = 0;
        while(stack.isEmpty() == false)
        {
            String s = stack.pollFirst();
            try
            {
                int op1 = Integer.parseInt(s);
                ans_stack.addLast(op1);
            }
            catch(Exception e)
            {
                if(s.contains("+"))
                {
                    String nums = stack.pollFirst();
                    ans_stack.addLast(Integer.parseInt(nums));
                }
                else if(s.contains("-"))
                {
                    String nums = stack.pollFirst();
                    ans_stack.addLast(-1 * Integer.parseInt(nums));
                }
                else if(s.contains("*"))
                {
                    String nums = stack.pollFirst();
                    int op2 = Integer.parseInt(nums);
                    int op1 = ans_stack.pollLast();
                    ans_stack.addLast(op1 * op2);
                }
                else if(s.contains("/"))
                {
                    String nums = stack.pollFirst();
                    int op2 = Integer.parseInt(nums);
                    int op1 = ans_stack.pollLast();
                    ans_stack.addLast((int)Math.floor(op1 / op2));
                }
            }
        }
        for(Integer i:ans_stack)
        {
            ans += i;
        }
        return ans;
    }
}