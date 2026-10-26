class Solution {
    public int[] dailyTemperatures(int[] temperatures) {
        Stack <Integer> helperstack = new Stack<>();
        int n = temperatures.length;
        int [] res = new int[n];
        for(int idx = n-1;idx>=0;idx--){
            while(!helperstack.isEmpty() && temperatures[idx] >= temperatures[helperstack.peek()]){
                helperstack.pop();
            }
            if (!helperstack.isEmpty()){
                res[idx] = helperstack.peek()-idx;
            }
            helperstack.push(idx);
        }
    return res;
    }
}