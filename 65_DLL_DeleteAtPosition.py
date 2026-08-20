class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

def DeleteAtEnd(head, p):
    if head is None:
        return None

    curr = head
    for _ in range(p):
        if curr is None:
            return head
        curr = curr.next

    if curr is None:
        return head

    if curr.prev is not None:
        curr.prev.next = curr.next

    if curr.next is not None:
        curr.next.prev = curr.prev

    if head == curr:
        head = curr.next

    del curr
    return head

def print_list(head):
    curr =  head
    while  curr is not None:
        print(curr.data, end = ' ')
        if curr.next is not None:
            print('<->', end =' ')
        curr = curr.next
    print()

def main():
    head = Node(2)
    head.next = Node(4)
    head.next.prev = head
    head.next.next = Node(5)
    head.next.next.prev = head.next
    print("Before Deletion: ")
    print_list(head)

    pos = 1

    head = DeleteAtEnd(head, pos)
    print("After Deletion: ")
    print_list(head)

if __name__ == "__main__":
    main()