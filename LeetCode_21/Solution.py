from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None) -> None:
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy

        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next
        
        if list1:
            tail.next = list1
        elif list2:
            tail.next = list2

        return dummy.next

    
def main():
  l2 = ListNode(4)
  l1 = ListNode(2, l2)
  l = ListNode(1, l1)

  t2 = ListNode(4)
  t1 = ListNode(3, t2)
  t = ListNode(1, t1)

  s = Solution()
  test = s.mergeTwoLists(l, t)
  print(test)


if __name__ == '__main__':
  main()