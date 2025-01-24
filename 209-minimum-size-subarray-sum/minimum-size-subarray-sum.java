class Solution {
    public int minSubArrayLen(int target, int[] nums) {
        int val = 0; // Current sum of the window
        int r = nums.length + 1; // Initialize to a value greater than the max possible length
        int i = 0; // Left pointer
        int j = 0; // Right pointer

        while (j < nums.length) {
            // Add nums[j] to the current sum
            val += nums[j];
            j++;

            // Shrink the window from the left while the condition is met
            while (val >= target) {
                r = Math.min(r, j - i); // Update the minimum length
                val -= nums[i];
                i++;
            }
        }

        // If no valid subarray was found, return 0
        return r == nums.length + 1 ? 0 : r;
    }
}
