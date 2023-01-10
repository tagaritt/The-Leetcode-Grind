import java.util.HashMap;

class Solution {
    public int[] twoSum(int[] nums, int target) {    
        
        // Declares a new HashMap to be used, allowing the use of ***KEY-VALUE PAIRS***.
        HashMap<Integer, Integer> numbers = new HashMap<Integer, Integer>();
        
        // Create a loop to evaluate all possible key-value pairs.
        for(int i = 0; i < nums.length; i++){   
            
            // Determine the value to check for given the current index's value.
            int difference = target - nums[i]; 
            
            // If a pair is found that equals the target value, return the pair.
            if (numbers.containsKey(difference)){
                return new int[] {numbers.get(difference), i};
            }
            
            // Adds the most-recently evaluated pair to the HashMap.
            numbers.put(nums[i], i);
        }
    
    // If no pair is found after complete evaluation, tell the user that no pair was found.
    throw new IllegalArgumentException("No pair was found.");
    }
}
