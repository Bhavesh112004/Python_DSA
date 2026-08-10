class Node:
    def __init__(self, data):
        self.data =  data
        self.next = None

def ReverseUsingStack(head):
    stack = []
    temp = head

    while temp.next is not None:
        stack.append(temp)
        temp = temp.next

    head = temp
    while stack:
        temp.next = stack.pop()
        temp = temp.next

    temp.next = None

    return head
    
def display_list(head):
    curr = head
    while curr is not None:
        print(f"{curr.data}", end="")
        if curr.next is not None:
            print('->', end = '')
        curr = curr.next
    print()

def main():
    head = Node(10)
    head.next = Node(20)
    head.next.next= Node(30)
    head.next.next.next = Node(40)
    head.next.next.next.next = Node(50)

    head = ReverseUsingStack(head)
    display_list(head)

if __name__ == "__main__":
    main()