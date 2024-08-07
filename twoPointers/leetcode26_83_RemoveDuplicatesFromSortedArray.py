"""
Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same. Then return the number of unique elements in nums.

Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:

Change the array nums such that the first k elements of nums contain the unique elements in the order they were present in nums initially. The remaining elements of nums are not important as well as the size of nums.
Return k.
Custom Judge:

The judge will test your solution with the following code:

int[] nums = [...]; // Input array
int[] expectedNums = [...]; // The expected answer with correct length

int k = removeDuplicates(nums); // Calls your implementation

assert k == expectedNums.length;
for (int i = 0; i < k; i++) {
    assert nums[i] == expectedNums[i];
}
If all assertions pass, then your solution will be accepted.

 

Example 1:

Input: nums = [1,1,2]
Output: 2, nums = [1,2,_]
Explanation: Your function should return k = 2, with the first two elements of nums being 1 and 2 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).
Example 2:

Input: nums = [0,0,1,1,1,2,2,3,3,4]
Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
Explanation: Your function should return k = 5, with the first five elements of nums being 0, 1, 2, 3, and 4 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).
 

Constraints:

1 <= nums.length <= 3 * 10**4
-100 <= nums[i] <= 100
nums is sorted in non-decreasing order.

"""
# O(n) time
# O(1) space
def removeDuplicates(nums: list[int]):
    i, j = 0, 1 # design two pointers, one slow -- i, one fast -- j
    while j < len(nums): # only need to check the fast pointer
        # when duplicated, moving fast, until find not duplicated in else condition
        if nums[i] == nums[j]:
            j += 1
        # when encounter the first difference, swap the i + 1 (which is the first duplciates) with current j
        else:
            nums[i+1], nums[j] = nums[j], nums[i+1]
            # i+1 is the new non-duplicate index
            i += 1
            # j+1 to start the check
            j += 1
    # because i starts from 0, the final non-duplicated should be k+1
    return i+1
nums = [1,1,2]
print(removeDuplicates(nums))

nums2 = [0,0,1,1,1,2,2,3,3,4]
print(removeDuplicates(nums2))




"""
leetcode 83 Remove duplicates from sorted list

Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.

 

Example 1:


Input: head = [1,1,2]
Output: [1,2]
Example 2:


Input: head = [1,1,2,3,3]
Output: [1,2,3]
 

Constraints:

The number of nodes in the list is in the range [0, 300].
-100 <= Node.val <= 100
The list is guaranteed to be sorted in ascending order.

"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head:ListNode):
        if not head: return None
        f, s = head, head
        while f:
            if f.val == s.val:
                f = f.next
            # when f.val is not the same as s.val, means the duplicate is over. Need the slow to point the current f
            else:
                s.next = f 
                # do not forget to update slow, otherwise, slow never changed 
                s = s.next
        s.next = None 
        return head 
    
# nonDuplicate = Solution()
# nonDuplicate.deleteDuplicates()
            

   