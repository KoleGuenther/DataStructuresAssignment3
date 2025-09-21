# Import the Node class you created in node.py
from node import Node

# Implement your Queue class here
class Queue:
    # Delete the following line and implement your Queue class
    def __init__(self):
        self.front = None
        self.rear = None

    def is_empty(self):
        return self.front is None
    
    # Enqueue implementation, adds a new value to the end of the queue
    def enqueue(self, value):
        new_node = Node(value)
        if self.rear:
            self.rear.next = new_node
        self.rear = new_node
        if not self.front:
            self.front = new_node

    # Dequeue implementation, removes front value and returns it
    def dequeue(self):
        if self.is_empty():
            return None
        dequeued_value = self.front.value
        self.front = self.front.next
        if not self.front:
            self.rear = None
        return dequeued_value

    # Peek implementation, returns the front value without removing it
    def peek(self):
        if self.is_empty():
            return None
        return self.front.value
    
    # Print queue implementation, prints all values in the queue
    def print_queue(self):
        current = self.front
        while current:
            print(current.value)
            current = current.next


def run_help_desk():
    # Create an instance of the Queue class
    help_desk_queue = Queue()

    while True:
        print("\n--- Help Desk Ticketing System ---")
        print("1. Add customer")
        print("2. Help next customer")
        print("3. View next customer")
        print("4. View all waiting customers")
        print("5. Exit")
        choice = input("Select an option: ")

        if choice == "1":
            name = input("Enter customer name: ")
            # Add the customer to the queue
            help_desk_queue.enqueue(name)
            
            print(f"{name} added to the queue.")
        elif choice == "2":
            # Help the next customer in the queue and return message that they were helped
            helped_customer = help_desk_queue.dequeue()
            if helped_customer:
                print(f"Helped customer: {helped_customer}")
            else:
                print("No customers in the queue.")


        elif choice == "3":
            # Peek at the next customer in the queue and return their name
            help_desk_queue.peek()
            if help_desk_queue.peek():
                print(f"Next customer to be helped: {help_desk_queue.peek()}")


        elif choice == "4":
            # Print all customers in the queue
            print("\nWaiting customers:")
            help_desk_queue.print_queue()

        elif choice == "5":
            print("Exiting Help Desk System.")
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    run_help_desk()
