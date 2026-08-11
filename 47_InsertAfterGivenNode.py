class Node:
  	
  	# Constructor to initialize the node
    def __init__(self, data):
        self.data = data
        self.next = None

def insert_after(head, key, new_data):
    curr = head

    while curr is not None:
        if curr.data == key:
            break
        curr = curr.next

    if curr is None:
        print('Not found')

        return head

    new_node = Node(new_data)

    new_node.next = curr.next
    curr.next = new_node

    return head

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
    key = 3
    new_data = 4

    # Insert a new node with data 4 after the node having
    # data 3
    head = insert_after(head, key, new_data)

    print("Linked List after insertion: ", end="")
    print_list(head)