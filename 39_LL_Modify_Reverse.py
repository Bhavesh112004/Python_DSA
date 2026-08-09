class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

def reverse_list(head):
    prev = None
    curr = head
    while curr:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next
    return prev


def display_list(head):
    curr = head
    while curr is not None:
        print(curr.data, end = ' ')
        if curr.next is not None:
            print("->", end = ' ')

        curr = curr.next
    print()

def main():
    head = Node(2)
    head.next = Node(9)
    head.next.next = Node(8)
    head.next.next.next = Node(12)
    head.next.next.next.next = Node(7)
    head.next.next.next.next.next = Node(10)

    head = reverse_list(head)
    display_list(head)

if __name__ == '__main__':
     main()