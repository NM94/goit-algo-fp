class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    def get_middle(self, head):
        if head is None:
            return head
        slow = head
        fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def sorted_merge(self, left, right):
        if not left:
            return right
        if not right:
            return left
        if left.data <= right.data:
            result = left
            result.next = self.sorted_merge(left.next, right)
        else:
            result = right
            result.next = self.sorted_merge(left, right.next)
        return result

    def merge_sort(self, head=None):
        if head is None:
            head = self.head
        if head is None or head.next is None:
            return head

        middle = self.get_middle(head)
        next_to_middle = middle.next
        middle.next = None

        left = self.merge_sort(head)
        right = self.merge_sort(next_to_middle)

        sorted_list = self.sorted_merge(left, right)
        self.head = sorted_list
        return sorted_list

    def merge_sorted_lists(self, list1, list2):
        dummy = Node(0)
        tail = dummy

        a = list1.head
        b = list2.head

        while a and b:
            if a.data <= b.data:
                tail.next = a
                a = a.next
            else:
                tail.next = b
                b = b.next
            tail = tail.next

        tail.next = a if a else b
        self.head = dummy.next



lst = LinkedList()
for x in [5, 1, 4, 2, 3]:
    lst.append(x)
lst.print_list()


lst.reverse()
lst.print_list()


lst.merge_sort()
lst.print_list()


lst1 = LinkedList()
lst2 = LinkedList()
for x in [10, 35, 51]:
    lst1.append(x)
for x in [20, 45, 61]:
    lst2.append(x)

merged = LinkedList()
merged.merge_sorted_lists(lst1, lst2)
merged.print_list()
