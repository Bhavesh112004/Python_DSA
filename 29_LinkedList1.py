class Node:
    def __init__(self, new_node):
        self.data = new_node
        self.next = None

def traverse_list(head):
        curr = head
        while curr is not None:
            print(curr.data, end = "")
            if curr.next is not None:
                print("->", end = "")
            curr =  curr.next

        print()

if __name__ == "__main__":
    head = Node(10)
    head.next = Node(20)
    head.next.next = Node(30)
    head.next.next.next = Node(40)

    traverse_list(head)