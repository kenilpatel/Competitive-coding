class Solution {
    public int dayOfYear(String date) {
        Map<Integer,Integer> days = new HashMap();
        days.put(0,0);
        days.put(1,31);
        days.put(3,31);
        days.put(4,30);
        days.put(5,31);
        days.put(6,30);
        days.put(7,31);
        days.put(8,31);
        days.put(9,30);
        days.put(10,31);
        days.put(11,30);
        days.put(12,31);
        String[] dateBreak = date.split("-");
        int day = new Integer(dateBreak[2]);
        int month = new Integer(dateBreak[1]);
        int year = new Integer(dateBreak[0]);
        days.put(2,year % 4 == 0?29:28);
        int ans = day;
        for(int i=0;i<month;i++){
            ans += days.get(i);
        }
        return ans;
    }
}