class Solution {
    public boolean hasDuplicate(int[] nums) {
        Set<Integer> letter = new HashSet<>();
        int res = 0;
        for(int i = 0; i<nums.length; i++){
            if(letter.contains(nums[i])){
                return true;
            }
            letter.add(nums[i]);
        }
        return false;
    }
}
