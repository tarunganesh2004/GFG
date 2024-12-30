// https://www.geeksforgeeks.org/problems/k-pangrams0909/1

class kPangrams {
    public static boolean kPangram(String str, int k) {
        str = str.replaceAll("\\s", "");
        int n = str.length();
        if (n < 26)
            return false;
        if (n >= 26 && k == 25)
            return true;
        
        int[] f = new int[26];
        int m = 0;
        for (char c : str.toCharArray()) {
            if (Character.isLowerCase(c)) {
                f[c - 'a']++;
            }
        }
        for (int i = 0; i < 26; i++) {
            if (f[i] == 0)
                m++;
        }
        return m <= k;
    }
}