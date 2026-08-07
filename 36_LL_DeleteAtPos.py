class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
def DeleteAtLast(head, pos):
    temp = head

    if pos == 1:
        head = temp.next
        return head
    
    prev = temp
    for i in range(1, pos -1):
        prev = prev.next

    prev.next = prev.next.next

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

    head = DeleteAtLast(head,3)
    display_list(head)

if __name__ == "__main__":
    main()