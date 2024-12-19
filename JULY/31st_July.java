class longestCommonPrefix {
    public static String longestcommonprefix(String arr[]) {
        String res = arr[0];
        for (String s : arr) {
            res = commonPrefix(res, s);
        }
        return res.equals("res") ? "-1" : res;
    }

    public static String commonPrefix(String s1, String s2) {
        String res = "";
        for (int i = 0; i < s1.length() && i < s2.length(); i++) {
            if (s1.charAt(i) == s2.charAt(i)) {
                res += s1.charAt(i);
            } else {
                break;
            }
        }
        return res;
    }
}