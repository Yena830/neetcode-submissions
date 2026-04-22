class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
       //Initialize new map
        Map<String, List<String>> anagrams = new HashMap<>();
        // Loop for each word
        for(int i=0;i<strs.length;i++){
            // To turn all chars in word to array
            char[] chars = strs[i].toCharArray();
            // sort
            Arrays.sort(chars);
            // Store the sorted word
            String sortedword = new String(chars);
            // If the sorted word is not in map
            if(!anagrams.containsKey(sortedword)){
                anagrams.put(sortedword,new ArrayList<>());
            }
            // Add the current word into the map
            anagrams.get(sortedword).add(strs[i]);
        }
        // Return the list
        return new ArrayList<>(anagrams.values()); 
    }
}
