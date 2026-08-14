class Node:
    def __init__(self, data):
        self.data = data 
        self.next =  None

def countNodes(start):
    count = 1
    curr = start
    while curr.next != start:
        count += 1
        curr = curr.next

    return count

def lengthOfLoop(head):

    slow = head
    fast = head
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return countNodes(slow)

    return 0

def main():
    head = Node(25)
    head.next = Node(14)
    head.next.next = Node(19)
    head.next.next.next = Node(35)
    head.next.next.next.next = Node(10)

    head.next.next.next.next.next = head.next.next

    print(lengthOfLoop(head))

if __name__ == "__main__":
    main()