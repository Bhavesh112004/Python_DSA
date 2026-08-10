class Node:
    def __init__(self, data):
        self.data =  data
        self.next = None

def MiddleNode(head):
    curr = head
    slow = head
    fast = head
    while fast is not None and fast.next is not None:
        slow= slow.next
        fast = fast.next.next

    return slow
        
    
    
    
# def display_list(head):
#     curr = head
#     while curr is not None:
#         print(f"{curr.data}", end="")
#         if curr.next is not None:
#             print('->', end = '')
#         curr = curr.next
#     print()

def main():
    head = Node(10)
    head.next = Node(20)
    head.next.next= Node(30)
    head.next.next.next = Node(40)
    head.next.next.next.next = Node(50)
    # head.next.next.next.next.next = Node(60)

    head = MiddleNode(head)
    print(head.data)

if __name__ == "__main__":
    main()