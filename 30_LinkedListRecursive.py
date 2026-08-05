class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def recursive_LL_traverse(head):
    if head is None:
        print()
        return

    print(head.data, end= "")

    if head.next is not None:
        print("->", end = "")

    recursive_LL_traverse(head.next)

if __name__ == "__main__":

    head = Node(10)
    head.next = Node(20)
    head.next.next = Node(30)
    head.next.next.next = Node(40)

    recursive_LL_traverse(head)