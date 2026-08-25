class Solution {
    public int mySqrt(int x) {
        long low = 1;
        long high = x/2;
        int count = 0 ;
        if (x<2) return x;
        while(low <= high){
           long mid = (low+high)/2;
           long square = mid*mid; 
           if (square == x){
            return (int)mid;
           }
           else if(square<x){
            count = (int)mid;
            low = mid+1;
           }
           else{
            high = mid-1;
           }

        }return count;
 
    }

}