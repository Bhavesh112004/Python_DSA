class Node:
    def __init__ (self, data):
        self.data = data
        self.next = None

def detectLoop(head):
    st = set()
    curr = head
    while curr is not None:
        if curr in st:
            return True
        st.add(curr)
        curr = curr.next

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