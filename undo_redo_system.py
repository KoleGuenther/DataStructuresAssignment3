# Import the Node class you created in node.py
from node import Node

# Implement your Stack class here
class Stack:
    def __init__(self):
        self.top = None

    def is_empty(self):
        return self.top is None

    # Push implementation, adds a new value to the top of the stack
    def push(self, value):
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node

    # Pop implementation, removes top value and returns it
    def pop(self):
        if self.is_empty():
            return None
        popped_value = self.top.value
        self.top = self.top.next
        return popped_value

    # Peek implementation, returns the top value without removing it
    def peek(self):
        if self.is_empty():
            return None
        return self.top.value

    # Print stack implementation, prints all values in the stack
    def print_stack(self):
        current = self.top
        while current:
            print(current.value)
            current = current.next

def run_undo_redo():
    # Create instances of the Stack class for undo and redo
    
    undo_stack = Stack()
    redo_stack = Stack()

    while True:
        print("\n--- Undo/Redo Manager ---")
        print("1. Perform action")
        print("2. Undo")
        print("3. Redo")
        print("4. View Undo Stack")
        print("5. View Redo Stack")
        print("6. Exit")
        choice = input("Select an option: ")

        if choice == "1":
            action = input("Describe the action (e.g., Insert 'a'): ")
            undo_stack.push(action) # Push action onto undo stack
            redo_stack = Stack()  # Clear the redo stack

            print(f"Action performed: {action}")
        elif choice == "2":
            if undo_stack.is_empty(): # Added so redo/undo doesn't keep stacking the same action if its undone/redone multiple times
                print("No actions to undo.")
            else: 
                undo_stack.pop() # Pop action from undo stack
                redo_stack.push(action) # Push the action onto redo stack
                print(f"Action undone: {action}")

        elif choice == "3":
            if redo_stack.is_empty(): # Added so redo/undo doesn't keep stacking the same action if its undone/redone multiple times
                print("No actions to redo.")
            else:
                redo_stack.pop() # Pop action from redo stack
                undo_stack.push(action) # Push the action onto undo stack
                print(f"Action redone: {action}")

        elif choice == "4":
            print("\nUndo Stack:")
            undo_stack.print_stack() # Print the undo stack
            

        elif choice == "5":
            print("\nRedo Stack:")
            redo_stack.print_stack() # Print the redo stack
            
            
        elif choice == "6":
            print("Exiting Undo/Redo Manager.")
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    run_undo_redo()