class Solution {
    public int findKthLargest(int[] nums, int k) {
        PriorityQueue<Integer> maxheap = new PriorityQueue<>(Collections.reverseOrder());
        for(int i =0;i<nums.length-k+1;i++){
            maxheap.add(nums[i]);

        }
        for(int i =nums.length-k+1;i<nums.length;i++){
                if(nums[i]<maxheap.peek()){
                    maxheap.poll();
                    maxheap.add(nums[i]);

                }
        }

        return maxheap.peek();
    }
}