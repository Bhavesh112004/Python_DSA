class Node:
    def __init__ (self, data):
        self.data = data
        self.next = None

def detectLoop(head):
    curr = head
    slow = head
    fast = head
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return True 

    return False

def main():
    head = Node(1)
    head.next = Node(3)
    head.next.next = Node(4)

    head.next.next.next = head.next

    if detectLoop(head):
        print("True")
    else:
        print("False")
if __name__ == "__main__":
    main()