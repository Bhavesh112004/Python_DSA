class Node:
    def __init__(self, data):
        self.data = data 
        self.prev = None
        self.next = None

def InsertAtPos(head, p, x):
    if p < 0:
        print( "Invalid Position")
        return
    nodes = []
    curr = head
    while curr is not None:
        nodes.append(curr)
        curr = curr.next

    new_node = Node(x)

    pNode = nodes[p]

    new_node.next = pNode.next
    new_node.prev = pNode

    if pNode.next is not None:
        pNode.next.prev = new_node

    pNode.next = new_node

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

    position = -1
    new_data = 6

    head = InsertAtPos(head, position, new_data)
    print_list(head)

if __name__ == "__main__":
    main()