class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

def SizeOfList(head):
    size = 0
    curr = head
    while curr is not None:
        curr = curr.next
        size += 1

    return size

def print_list(head):
    curr =  head
    while  curr is not None:
        print(curr.data, end = ' ')
        if curr.next is not None:
            print('<->', end =' ')
        curr = curr.next
    print()

def main():
    head = Node(1)
    head.next = Node(2)
    head.next.prev = head
    head.next.next = Node(3)
    head.next.next.prev = head.next
    head.next.next.next = Node(4)
    head.next.next.next.prev = head.next.next

    print_list(head)
    print('Size of list: ',SizeOfList(head))
    

if __name__ == "__main__":
    main()