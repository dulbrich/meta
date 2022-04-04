from heapq import heapify, heappush, heappop

class ListNode:
	def __init__(self, val, next):
		self.val = val
		self.next = next

def mergeklists(lists):
	minheap = []
	heapify(minheap)
	for i in range(lists):
		if lists[i] is not None:
			heappush(minheap, (lists[i].val, lists[i]))
	head = ListNode("sentinal", None)
	tail = head
	while minheap:
		val, p = heappop(minheap)
		tail.next = p
		tail = p
		p = p.next
		tail.next = None
		if p is not None:
			heappush(minheap, (p.val, p))
	return head.next
