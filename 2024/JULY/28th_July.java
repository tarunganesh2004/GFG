class removeDuplicates {
    public static String removeDups(String s) {
        int n = s.length();
        int[] f = new int[26];
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < n; i++) {
            if (f[s.charAt(i) - 'a'] == 0) {
                sb.append(s.charAt(i));
                f[s.charAt(i) - 'a']++;
            }
        }
        return sb.toString();
    }
}