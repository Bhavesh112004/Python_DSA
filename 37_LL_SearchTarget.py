class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def SearchTarget(head, target):
    curr = head
    if curr.data == target:
        return True

    return SearchTarget(head.next,target)
        
def main():
    head = Node(10)
    head.next = Node(20)
    head.next.next = Node(30)
    head.next.next.next = Node(40)

    x = 40
    result = SearchTarget(head,x)
    if result == True:
        print('True')
    else:
        print('False')
    

if __name__ == "__main__":
    main()