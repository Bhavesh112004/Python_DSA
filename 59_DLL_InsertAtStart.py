class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

def InsertAtStart(head, new_data):
    new_node = Node(new_data)

    new_node.next = head
    if head is not None:
        head.prev = new_node

    return new_node

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
    head = InsertAtStart(head, x)
    print_list(head)

if __name__ == "__main__":
    main()