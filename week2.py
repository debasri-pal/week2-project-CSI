class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add_node(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    def print_list(self):
        if not self.head:
            print("List is empty.")
            return
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")

    def delete_nth_node(self, n):
        if not self.head:
            raise Exception("Cannot delete from an empty list.")

        if n <= 0:
            raise IndexError("Index must be a positive integer.")

        if n == 1:
            self.head = self.head.next
            return

        temp = self.head
        count = 1
        while temp and count < n - 1:
            temp = temp.next
            count += 1

        if not temp or not temp.next:
            raise IndexError("Index out of range.")

        temp.next = temp.next.next

# Sample Test
if __name__ == "__main__":
    ll = LinkedList()
    ll.add_node(10)
    ll.add_node(20)
    ll.add_node(30)
    ll.add_node(40)

    print("Initial Linked List:")
    ll.print_list()

    try:
        ll.delete_nth_node(2)
        print("\nAfter deleting 2nd node:")
        ll.print_list()
    except Exception as e:
        print("Error:", e)

    try:
        ll.delete_nth_node(10)  # This will raise an exception
    except Exception as e:
        print("Error:", e)

    try:
        empty_list = LinkedList()
        empty_list.delete_nth_node(1)
    except Exception as e:
        print("Error:", e)
