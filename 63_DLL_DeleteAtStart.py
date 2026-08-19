class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

def DeleteAtStart(head):
    if head is None:
        return None

    temp = head
    head = head.next

    if head is not None:
        head.prev = None

    temp.next = None

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
    print("Before Deletion: ")
    print_list(head)
    head = DeleteAtStart(head)
    print("After Deletion: ")
    print_list(head)

if __name__ == "__main__":
    main()