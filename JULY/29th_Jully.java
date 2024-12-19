class rowWithMaxOnes {
    public int maxOnes(int[][] m) {
        int max = Integer.MIN_VALUE;
        int row = -1;
        for (int i = 0; i < m.length; i++) {
            int c = 0;
            for (int j = 0; j < m[0].length; i++) {
                if (m[i][j] == 1) {
                    c++;
                }
            }
            if (c > max) {
                max = c;
                row = i;
            }
        }
        return row;
    }
}