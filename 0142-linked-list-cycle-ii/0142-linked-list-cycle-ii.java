/**
 * Definition for singly-linked list.
 * class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */
public class Solution {
    public ListNode detectCycle(ListNode head) {
        if (head == null || head.next == null) {
            return null;
        }
        boolean hascycle = false;
        ListNode slow = head;
        ListNode fast = head;
        if(slow == null && slow.next== null){
            return null ;
        }
        while(fast.next!=null && fast.next.next!=null){
            slow = slow.next;
            fast = fast.next.next;
            if(slow == fast){
               hascycle = true;
               break;
            }}
            if(!hascycle){
                return null;
            }
        slow = head;
        while(slow!=fast){
            slow = slow.next;
            fast = fast.next;
        }
        
        
        return slow;
    }
}