# This is an implementation of a stack using Python's List data type.
# A Stack is a Last In, First Out type of data structure. 
# In this case, the maximum index will be considered the top of the stack, in order to prevent having to reindex the items frequently.

class Stack:

    stack = []
    
    def __init__(self):
        self.stack = []

    # Push (add) an item to the top of the stack.
    def push(self, item):
        self.stack.append(item)
    
    # Pop (remove) an item from the top of the stack.
    def pop(self):
        try:
            return self.stack.remove(len(self.stack)-1)
        except IndexError:
            print("IndexError: Index outside of Stack.")
        except ValueError:
            print("ValueError: Stack empty.")
              
    # Peek (return, without removing) at the item on top of the stack.
    def peek(self):
        try:
            return self.stack[len(self.stack)-1]
        except IndexError:
            print("IndexError: Index outside of Stack.")
        except ValueError:
            print("ValueError: Stack empty.")
        
    
    # String representation of the data
    def __str__(self):
        try:
            return f"{self.stack}, Top: {self.stack[len(self.stack)-1]}"
        except IndexError:
            return f"{self.stack}"