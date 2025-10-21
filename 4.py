class Node:
    def __init__(self, value, next_it):
        self.value = value
        self.next_it = next_it

class Stack:
    def __init__(self):
        self.top = None
        self.count = 0

    def push(self, value):
        if self.top is None:
            self.top = Node(value, None)
            self.count += 1
            return
        self.top = Node(value, self.top)
        self.count += 1

    def pop(self):
        if self.top is None:
            raise IndexError("Stack is empty")
        top = self.top
        self.top = top.next_it
        self.count -= 1
        return top.value

    def peek(self):
        if self.top is None:
            raise IndexError("Stack is empty")
        return self.top.value

    def is_empty(self):
        if self.count == 0:
            return True
        return False

if __name__ == "__main__":
    stack = Stack()
    print(f"is_empty: '{stack.is_empty()}'")
    stack.push(Node(1, "a"))
    print(f"is_empty: '{stack.is_empty()}'")
    stack.push(Node(2, "b"))
    print(f"peek: '{stack.peek().next_it}'")
    print(f"is_empty: '{stack.is_empty()}'")
    print(f"pop: '{stack.pop().next_it}'")
    print(f"is_empty: '{stack.is_empty()}'")
    print(f"pop: '{stack.pop().next_it}'")
    print(f"is_empty: '{stack.is_empty()}'")