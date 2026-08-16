class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

def InsertAtEnd(head,tail, new_data):
    new_node = Node(new_data)

    if head is None:
        tail = new_node
        head = new_node
    else: 
        tail.next = new_node
        new_node.prev = tail

        tail = new_node

    return head, tail


def print_list(head):
    curr = head
    while curr is not None:
        print(curr.data, end="")
        if curr.next is not None:
            print(" <-> ", end="")
        curr = curr.next
    print()

def main():
    head = Node(1)
    second = Node(2)
    third = Node(3)
    fourth = Node(4)

    head.next = second
    second.prev = head
    second.next = third
    third.prev = second
    third.next = fourth
    fourth.prev = third

    x = 0
    head, tail = InsertAtEnd(head,fourth, x)
    print_list(head)

if __name__ == "__main__":
    main()