class Solution {
    public String decodeString(String s) {
        Stack<Character> stack = new Stack<Character>();

        for(int i=0;i<s.length();i++)
        {
            if(s.charAt(i) == ']')
            {

                String temp = "";
                while(true)
                {
                    if(stack.peek() == '[')
                    {
                        stack.pop();
                        break;
                    }
                    temp = stack.pop() + temp;
                }
                String num = "";
                while(true)
                {
                    if(stack.size() == 0)
                    {
                        break;
                    }
                    if(Character.isDigit(stack.peek()) == false)
                    {
                        break;
                    }
                    num = stack.pop() + num;
                }
                // System.out.println(temp+","+num);
                if (temp != "" && num != "")
                {
                    String ans = "";
                    ans = ans + temp.repeat(Integer.parseInt(num));
                    // System.out.println(ans);
                    for(int j=0;j<ans.length();j++)
                    {
                        stack.add(ans.charAt(j));
                    }
                }

            }
            else
            {
                stack.push(s.charAt(i));
            }
        }
        String fans = "";
        while(stack.size() != 0)
        {
            fans = stack.pop() + fans;
        }
        return fans;
    }
}