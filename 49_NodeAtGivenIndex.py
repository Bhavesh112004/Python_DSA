class Node:
  	
  	# Constructor to initialize the node
    def __init__(self, data):
        self.data = data
        self.next = None

def get_node(head, k):
    pos = 1
    curr = head
    while curr is not None:
        if pos == k:
            return curr.data
        curr = curr.next
        pos += 1

    return -1


def print_list(node):
    while node is not None:
        print(node.data, end=" ")
        node = node.next
    print()

if __name__ == "__main__":
  	
    # Create a hard-coded linked list:
    # 2 -> 3 -> 5 -> 6
    head = Node(2)
    head.next = Node(3)
    head.next.next = Node(5)
    head.next.next.next = Node(6)

    print("Original Linked List: ", end="")
    print_list(head)

    # Key: Insert node after key
    position = 0


    # Insert a new node with data 4 after the node having
    # data 3
    head = get_node(head, position)
    print(head)