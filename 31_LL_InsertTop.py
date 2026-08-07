class Node:
    def __init__(self, data):
        self.data = data 
        self.next = None

def display_list(head):
    curr = head
    while curr is not None:
        print(curr.data, end = "")

        if curr.next is not None:
            print("->", end = "")
        curr = curr.next

    print()

def Insert_Front(head,x):
    new_node = Node(x)
    new_node.next = head
    return new_node
    

if __name__ == "__main__":
    head = Node(20)
    head.next = Node(30)
    head.next.next= Node(40)

    x = 10
    head = Insert_Front(head,x)

    display_list(head)