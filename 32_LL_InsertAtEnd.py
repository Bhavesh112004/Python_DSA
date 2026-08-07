class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def InsertAtLast(head, x):
    new_node = Node(x)

    if head is None:
        return new_node
    
    last = head

    while last.next is not None:
        last = last.next

    last.next = new_node

    return head

def display_list(node):
    while node is not None:
        print(node.data, end = "")
        if node.next is not None:
            print("->", end = "")
        node = node.next
    print()

def main():
    head = Node(10)
    head.next = Node(20)
    head.next.next = Node(30)
    head.next.next.next = Node(40)

    x = 50
    head = InsertAtLast(head,x)

    display_list(head)

if __name__ == "__main__":
    main()