from typing import Optional, List

class ListNode:
    def __init__(self, val=0, next=None) -> None:
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None and list2 is None:
            return None
        elif list1 is None:
            return list2
        elif list2 is None:
            return list1
        
        l1 = extractLinkedList(list1)
        l2 = extractLinkedList(list2)
        return listToLinkedList(sorted(l1 + l2))


def extractLinkedList(l: Optional[ListNode], result=None):
    # create intermediate list
    if result == None:
        result = []

    if l.next == None:
      result.append(l.val)
    else:
        result.append(l.val)
        return extractLinkedList(l.next, result)
    return result


def listToLinkedList(l: List[int]) -> Optional[ListNode]:
    cur = dummy = ListNode(0)
    for e in l:
        cur.next = ListNode(e)
        cur = cur.next
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