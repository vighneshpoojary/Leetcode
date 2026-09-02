class Solution {
    public boolean isAnagram(String s, String t) {
      
        int [] pcount = new int[26];
        int [] scount = new int[26];
        if(s.length()!=t.length())return false;
        for(char c:t.toCharArray()){
            pcount[c-'a']++;
        }
        for(int i=0;i<s.length();i++){
            scount[s.charAt(i)-'a']++;
            if(i>=t.length()){
                scount[s.charAt(i-t.length())-'a']--;
            }
            if(i>=t.length()-1&&Arrays.equals(pcount,scount)){
                return true;
               
            }
            
        
       }  
    return false;}
}