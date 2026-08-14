class Node:
    def __init__(self, data):
        self.data = data
        self.next =  None

def lengthOfLoop(head):
    visited = set()
    curr = head 
    count = 0

    while curr is not None:
        if curr in visited:
            startofLoop = curr
            while True:
                count += 1
                curr = curr.next
                if curr == startofLoop:
                    break

            return count
        visited.add(curr)
        curr = curr.next

    return 0


def main():
    head = Node(25)
    head.next = Node(14)
    head.next.next = Node(19)
    head.next.next.next = Node(35)
    head.next.next.next.next = Node(10)

    head.next.next.next.next.next = head.next.next

    print(lengthOfLoop(head))

if __name__ =="__main__":
    main()