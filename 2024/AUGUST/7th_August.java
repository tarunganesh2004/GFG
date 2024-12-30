class kthElementOfTwoArrays {
    public long kthElement(int k, int[] a1, int[] a2) {
        int i = 0, j = 0, ans = 0;
        while (k > 0) {
            if (i >= a1.length) {
                ans = a2[j];
                j++;
            } else if (j >= a2.length) {
                ans = a1[i];
                i++;
            } else if (a1[i] < a2[i]) {
                ans = a1[i];
                i++;
            } else {
                ans = a2[j];
                j++;
            }
            k--;
        }
        return ans;
    }
}