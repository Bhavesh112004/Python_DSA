class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

def reverse_list(head):
    prev = None
    curr = head
    while curr:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next
    return prev

def ModifyList(head):
    if head is None or head.next is None:
        return head

    slow = head
    fast = head
    while fast.next is not None and fast.next.next is not None:
        slow = slow.next
        fast = fast.next.next

    second_half = slow.next
    slow.next = None

    second_half = reverse_list(second_half)

    first = head
    second = second_half

    while second is not None:
        value = first.data
        first.data = second.data - value
        second.data = value

        first = first.next
        second = second.next

    # Restore the original structure
    slow.next = reverse(second_half)

    return head


def display_list(head):
    curr = head
    while curr is not None:
        print(curr.data, end = ' ')
        if curr.next is not None:
            print("->", end = ' ')

        curr = curr.next
    print()

def main():
    head = Node(2)
    head.next = Node(9)
    head.next.next = Node(8)
    head.next.next.next = Node(12)
    head.next.next.next.next = Node(7)
    head.next.next.next.next.next = Node(10)

    head = ModifyList(head)
    display_list(head)

if __name__ == '__main__':
     main()