class Node:
  	
  	# Constructor to initialize the node
    def __init__(self, data):
        self.data = data
        self.next = None

def insert_before(head, key, new_data):
    if head is None:
        return head

    if head.data == key:
        new_node = Node(new_data)
        new_node.next = head
        return new_node

    prev = None
    curr = head
    while curr is not None:
        if curr.data == key:
            new_node = Node(new_data)
            prev.next = new_node
            new_node.next = curr
            return head
        prev = curr
        curr = curr.next


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
    key = 2
    new_data = 4

    # Insert a new node with data 4 after the node having
    # data 3
    head = insert_before(head, key, new_data)
    if not head:
        print("Not Found")
    else:
        print("Linked List before insertion: ", end="")
        print_list(head)