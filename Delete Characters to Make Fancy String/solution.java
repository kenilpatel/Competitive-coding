class Solution {
    public String makeFancyString(String s) {
        StringBuilder ans = new StringBuilder();
        int len = 0;
        for(int i=0;i<s.length();i++){
            char ch = s.charAt(i);
            if(len >= 2){
                if(!(ch == ans.charAt(len - 1) & ch == ans.charAt(len - 2))){
                    ans.append(ch);
                    len += 1;
                }
            }
            else{
                ans.append(ch);
                len += 1;
            }
        }
        return ans.toString();
    }
}