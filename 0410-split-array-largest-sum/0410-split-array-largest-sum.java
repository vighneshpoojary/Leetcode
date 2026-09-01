class Solution {
    boolean isValid(int[] nums, int n, int k, int maxAllowed) {
        int stu = 1;
        int pages = 0;
        for (int i = 0; i < n; i++) {
            if (nums[i] > maxAllowed) return false; 
            if (pages + nums[i] <= maxAllowed) {
                pages += nums[i];
            } else {
                stu++;
                pages = nums[i];
            }
        }
        return stu <= k;
    }

    public int splitArray(int[] nums, int k) {
        int n = nums.length;
        if (k > n) return -1;

        int sum = 0, max = 0;
        for (int num : nums) {
            sum += num;
            max = Math.max(max, num);
        }

        int st = max;
        int end = sum;

        while (st <= end) {
            int mid = st + (end - st) / 2;
            if (isValid(nums, n, k, mid)) {
                end = mid - 1;
            } else {
                st = mid + 1;
            }
        }
        return st;  
    }
}
