class Solution {
    public boolean isAnagram(String s, String t) {
        char[] sArray = s.toCharArray();
        char[] tArray = t.toCharArray();
        int[] alpha = new int[26];
        for(char x : sArray){
            alpha[x-'a']++;
        }
        for(char y: tArray){
            alpha[y-'a']--;
        }
        for(int i:alpha){
            if(i!=0){
                return false;
            }
        }
        return true;
    }
}
