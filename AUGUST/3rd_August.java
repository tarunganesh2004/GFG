import java.util.Stack;

class celebrityProblem {
    public static int celebrity(int[][] a) {
        Stack<Integer> st = new Stack<>();
        for (int i = 0; i < a.length; i++) {
            st.push(i);
        }
        while (st.size() >= 2) {
            int i = st.pop();
            int j = st.pop();
            if (a[i][j] == 1) {
                st.push(j);
            } else {
                st.push(i);
            }
        }
        int pot = st.pop();
        for (int i = 0; i < a.length; i++) {
            if (i != pot) {
                if (a[i][pot] == 0 || a[pot][i] == 1) {
                    return -1;
                }
            }
        }
        return pot;
    }
}