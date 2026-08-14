class Node:
    def __init__(self, data):
        self.data = data 
        self.next = None

def pairwise_swap(head):
    if head is None or head.next is None:
        return head

    prev = head
    curr = head.next

    head = curr
    while True:
        next_node = curr.next
        curr.next = prev
        
        if next_node is None or next_node.next is None:
            
            # connect remaining node (if exists)
            prev.next = next_node
            break

        prev.next = next_node.next

        prev = next_node
        curr = prev.next

    return head

def print_list(head):
    curr = head
    while curr is not None:
        print(curr.data, end=" ")
        curr = curr.next
    print()
    

def main():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = Node(6)
    #head.next.next.next.next.next.next = Node(7)

    head = pairwise_swap(head)
    print_list(head)

if __name__ == "__main__":
    main()