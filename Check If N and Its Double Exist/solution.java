class Solution {
    public boolean checkIfExist(int[] arr) {
        Map<Integer,Boolean> map = new HashMap();
        for(int i=0;i<arr.length;i++)
        {

            int find = arr[i] * 2;
            if(map.get(find) != null)
            {
                return true;
            }
            if(arr[i] % 2 ==0)
            {
                if(map.get(arr[i] / 2) != null)
                {
                    return true;
                }
            }
            map.put(arr[i],true);
        }
        return false;
    }
}