class Node:
    def __init__(self, data):
        self.data = data 
        self.next = None

def CountOccurence(head, key):
    if head is None:
        return 0

    curr = head
    count = 0
    while curr is not None:
        if curr.data == key:
            count += 1

        curr = curr.next

    return count

def print_list(head):
    curr = head
    while curr is not None:
        print(curr.data, end=" ")
        curr = curr.next
    print()
    

def main():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(1)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(1)
    head.next.next.next.next.next = Node(1)

    key = 1
    count = CountOccurence(head, key)
    print(count)

if __name__ == "__main__":
    main()