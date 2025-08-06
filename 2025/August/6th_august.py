
s="IX"

def romanToDecimal(s):
    map={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}

    res=0
    i=0
    while i<len(s):
        if i+1<len(s) and map[s[i]]<map[s[i+1]]:
            res+=map[s[i+1]]-map[s[i]]
            i+=2 # Skip both
        else:
            res+=map[s[i]]
        i+=1
    return res

print(romanToDecimal(s))

"""
Java Snippet:
public static int romanToInt(String s){
        Map<Character, Integer> map = new HashMap<>();
        map.put('I', 1);
        map.put('V', 5);
        map.put('X', 10);
        map.put('L', 50);
        map.put('C', 100);
        map.put('D', 500);
        int i = 0;
        int res = 0;
        while (i < s.length()) {
            if (i + 1 < s.length() && map.get(s.charAt(i)) < map.get(s.charAt(i + 1))) {
                res += map.get(s.charAt(i + 1)) - map.get(s.charAt(i));
                i++;
            } else {
                res += map.get(s.charAt(i));
                i++;
            }

        }
        return res;
    }
"""