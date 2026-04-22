class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        Map<Integer, Integer> freq = new HashMap<>();
        
        // Create n buckets
        List<List<Integer>> bucket = new ArrayList<>();

        for(int i=0; i<nums.length+1; i++){
            bucket.add(new ArrayList<>());
        }
        
        // Loop the nums and update freq 
        for(int num : nums){
            freq.put(num,freq.getOrDefault(num,0)+1);
        }

        // According to the freq, put every element into bucket
        for (Map.Entry<Integer, Integer> entry : freq.entrySet()){
            bucket.get(entry.getValue()).add(entry.getKey());
        }

        // Find the k freq
        int[] res = new int[k];
        int index =0;
        for(int i = bucket.size()-1; i>0 && index<k; i--){
            for(int n:bucket.get(i)){
                res[index] = n;
                index++;
                if(index == k){
                    return res;
                }
                
            }
        }
        return res;
    }
}
