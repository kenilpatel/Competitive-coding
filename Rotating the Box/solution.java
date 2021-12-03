class Solution {
    public char[][] rotateTheBox(char[][] box) {
        int m = box.length;
        int n = box[0].length;
        int m1 = n;
        int n1 = m;
        char[][] rotatedBox = new char[m1][n1];
        int i1 = -1;
        int j1 = 0;
        Map<Integer, List<Integer>> stoneMap = new HashMap();

        for(int j=0;j<n;j++) {
            j1 = 0;
            i1++;
            for(int i=m-1;i>=0;i--) {
                rotatedBox[i1][j1] = box[i][j];
                if (box[i][j] == '#') {
                    List<Integer> listY = stoneMap.getOrDefault(i1,
                                                               new ArrayList());
                    listY.add(j1);
                    rotatedBox[i1][j1] = '.';
                    stoneMap.put(i1,listY);
                }
                j1++;
            }
        }

        debug(stoneMap);

        for(int i=m1-1;i>=0;i--) {
            debug("I",i);
            for(Integer y:stoneMap.getOrDefault(i, new ArrayList<Integer>())) {
                int maxI = i;
                for(int possibleI=i+1;possibleI<m1;possibleI++) {
                    debug(possibleI,"possiblei");
                    if (rotatedBox[possibleI][y] != '.') {
                        break;
                    }
                    maxI = possibleI;
                }
                debug(maxI,y);
                rotatedBox[maxI][y] = '#';
            }

        }

        return rotatedBox;
    }

    void debug(Object ...args) {
            String printf = "";
            for(int i=0;i<args.length;i++) {
                printf = printf + " " + args[i];
            }
            // System.out.println(printf);
        }
}