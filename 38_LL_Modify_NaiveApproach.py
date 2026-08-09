class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

def ModifyList(head):
    values = []

    curr = head

    while curr is not None:
        values.append(curr.data)
        curr = curr.next

    left = 0
    right = len(values)-1

    while left < right:
        value = values[left]
        values[left] = values[right]- value
        values[right] = value

        left +=1
        right -= 1

    curr = head
    for value in values:
        curr.data = value
        curr = curr.next

    return head

def display_list(head):
    curr = head
    while curr is not None:
        print(curr.data, end = ' ')
        if curr.next is not None:
            print("->", end = ' ')

        curr = curr.next
    print()

def main():
    head = Node(2)
    head.next = Node(9)
    head.next.next = Node(8)
    head.next.next.next = Node(12)
    head.next.next.next.next = Node(7)
    head.next.next.next.next.next = Node(10)

    head = ModifyList(head)
    display_list(head)

if __name__ == '__main__':
     main()