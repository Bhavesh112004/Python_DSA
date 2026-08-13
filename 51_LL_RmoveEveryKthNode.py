class Node:
    def __init__(self, data):
        self.data = data 
        self.next = None

def removeKth(head,k):
    if head is None or k<=0:
        return None

    count = 1
    prev = None
    curr = head
    while curr is not None:
        if count % k == 0:
            prev.next = curr.next
        else:
            prev = curr
        curr = curr.next
        count += 1

    return head

def print_list(head):
    curr = head
    while curr is not None:
        print(curr.data, end=" ")
        curr = curr.next
    print()
    

def main():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = Node(6)

    k = 3
    head = removeKth(head, k)
    print_list(head)

if __name__ == "__main__":
    main()