// https://www.geeksforgeeks.org/problems/validate-an-ip-address-1587115621/1
class ValidateIpAddress {
    public boolean isValid(String s) {
        String[] arr = s.split("\\.", -1);
        for (String s1 : arr) {
            if (s1.length() <= 0 || s1.length() > 3) {
                return false;
            }

            int n = Integer.parseInt(s);
            if (n > 255 || (n > 0 && s1.charAt(0) == '0')) {
                return false;
            }
        }
        return true;
    }
}