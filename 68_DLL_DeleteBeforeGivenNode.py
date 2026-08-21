class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

def DeleteBeforeGivenNode(head, key):
    curr = head

    while curr is not None:
        if curr.data == key:
            break
        curr = curr.next

    if curr is None or curr.prev is None:
        return head

    node_to_delete = curr.prev
    curr.prev = node_to_delete.prev

    if node_to_delete.prev is not None:
        node_to_delete.prev.next = curr
    else:
        head = curr
    
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
    key = 1
    head = DeleteBeforeGivenNode(head, key)
    print_list(head)
    

if __name__ == "__main__":
    main()