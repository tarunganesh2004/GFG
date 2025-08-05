# Palindrome Sentence


s="Too hot to hoot"

def isPalinSent(self,s):
    s=s.lower()
    s=s.replace(" ","")
    res=""
    for ch in s:
        if ch.isalnum():
            res+=ch
    return res==res[::-1]

print(isPalinSent(0,s))

"""
Java Snippet:
public static boolean isPalindromeSentence(String s) {
    s = s.toLowerCase().replace(" ", "");
    StringBuilder res = new StringBuilder();
    for (char ch : s.toCharArray()) {
        if (Character.isLetterOrDigit(ch)) {
            res.append(ch);
        }
    }
    String cleaned = res.toString();
    return cleaned.equals(new StringBuilder(cleaned).reverse().toString());
}
"""