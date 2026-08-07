class Node:
    def __init__(self, data):
        self.data = data 
        self.next = None

def InsertAtPos(head, pos, val):
    if pos < 1:
        return head

    if pos == 1:
        new_node = Node(val)
        new_node.next = head
        return new_node
    
    curr = head

    for i in range(1, pos -1):
        if curr is None:
            return head
        curr = curr.next

    if curr is None:
        return head

    new_node = Node(val)

    new_node.next = curr.next
    curr.next = new_node

    return head
def display_list(head):
    curr = head
    while curr is not None:
        print(curr.data, end="")
        if curr.next is not None:
            print('->', end= '')

        curr = curr.next

    print()

def main():
    head = Node(10)
    head.next = Node(20)
    head.next.next = Node(40)
    head.next.next.next = Node(50)

    head = InsertAtPos(head, 3, 30)
    display_list(head)

if __name__ == "__main__":
    main()