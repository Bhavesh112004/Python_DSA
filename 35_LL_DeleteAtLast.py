class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
def DeleteAtLast(head):
    if head is None:
        return None

    if head.next is None:
        return None

    second_last = head
    while second_last.next.next is not None:
        second_last = second_last.next

    second_last.next = None

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
    head.next.next = Node(40)
    head.next.next.next = Node(50)

    head = DeleteAtLast(head)
    display_list(head)


if __name__ == "__main__":
    main()