class FindContentChildren {
    public static int findContentChildren(int[] g, int[] s) {
        Arrays.sort(g);
        Arrays.sort(s);
        int count = 0;
        int cookieNum = 0;
        for (int i = 0; i < g.length; i++) {
            while (cookieNum < s.length && g[i] > s[cookieNum]) {
                    cookieNum++;
            }
            if (cookieNum == s.length) {
                break;
            }
            count++;
            cookieNum++;
        }
        return count;
    }
}