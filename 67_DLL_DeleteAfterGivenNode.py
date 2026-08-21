class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

def DeleteAfterGivenNode(head, key):
    curr = head

    while curr is not None:
        if curr.data == key:
            break
        curr = curr.next

    if curr is None or curr.next is None:
        return head

    node_delete = curr.next

    curr.next = node_delete.next
    if node_delete.next is not None:
        node_delete.next.prev = curr

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
    head = Node(1)
    head.next = Node(2)
    head.next.prev = head
    head.next.next = Node(3)
    head.next.next.prev = head.next
    head.next.next.next = Node(4)
    head.next.next.next.prev = head.next.next

    print_list(head)
    key = 2
    head = DeleteAfterGivenNode(head, key)
    print_list(head)
    

if __name__ == "__main__":
    main()