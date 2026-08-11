class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

def count_nodes(head):
    curr = head
    count = 0
    while curr is not None:
        count += 1
        curr = curr.next

    return count

def main():
    head = Node(2)
    head.next = Node(9)
    head.next.next = Node(8)
    head.next.next.next = Node(12)
    head.next.next.next.next = Node(7)
    # head.next.next.next.next.next = Node(10)

    head = count_nodes(head)
    print(f"The Count of Nodes is {head}")

if __name__ == '__main__':
     main()