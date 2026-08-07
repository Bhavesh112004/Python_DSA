class Node: 
    def __init__(self, data):
        self.data = data
        self.next = None

def DeleteFront(head):
    if head is None:
        return None

    temp = head

    head = head.next

    temp = None

    return head

def display_list(head):
    curr = head
    while curr is not None:
        print(curr.data, end = "")
        if curr.next is not None:
            print("->", end= '')
        curr = curr.next

def main():
    head = Node(10)
    head.next = Node(20)
    head.next.next = Node(30)
    head.next.next.next = Node(40)

    head = DeleteFront(head)
    display_list(head)

if __name__ == "__main__":
    main()