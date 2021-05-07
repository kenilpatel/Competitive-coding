class Solution {
    public int getX(String s)
    {
        if(s.equals("x"))
        {
            return 1;
        }
        else
        {
            int n = s.length();
            String num = s.substring(0,n - 1);
            return Integer.parseInt(num);
        }
    }
    public int getN(String s)
    {
        try
        {
            return Integer.parseInt(s);
        }
        catch(Exception e)
        {
            return 0;
        }

    }
    public String solveEquation(String equation) {
        String[] eq = equation.split("=");
        String[] plus = eq[0].split("\\+");
        int s1 = 0;
        int s2 = 0;
        int num;
        for(int i=0;i<plus.length;i++)
        {
            String[] all = plus[i].split("\\-");
            if(all[0].contains("x"))
            {
                num = getX(all[0]);
                s1 +=  num;
            }
            else
            {
                num = getN(all[0]);
                s2 -= num;
            }
            // System.out.println(num);
            for(int j=1;j<all.length;j++)
            {
                if(all[j].contains("x"))
                {
                   num = getX(all[j]) * -1;
                    s1 += num;
                }
                else
                {
                    num = getN(all[j]) * - 1;
                    s2 -= num;
                }
            }
        }
        String[] plus1 = eq[1].split("\\+");
        for(int i=0;i<plus1.length;i++)
        {
            String[] all = plus1[i].split("\\-");
            if(all[0].contains("x"))
            {
                num = getX(all[0]);
                s1 -= num;
            }
            else
            {
                num = getN(all[0]);
                s2 += num;
            }
            for(int j=1;j<all.length;j++)
            {
                if(all[j].contains("x"))
                {
                    num = getX(all[j]) * -1;
                    s1 -= num;
                }
                else
                {
                    num = getN(all[j]) * - 1;
                    s2 += num;
                }
            }
        }
        if(s1 == 0 && s2 == 0)
        {
            return "Infinite solutions";
        }
        else if(s1 == 0 && s2 != 0)
        {
            return "No solution";
        }
        else
        {
            int ans = s2 / s1;
            return "x="+ans;
        }
    }
}