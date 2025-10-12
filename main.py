# This main file is where the code examples are run, using the implementations in this repo.
from datastructures import stack



def main():
    
    
    # Stack example
    print("=== Stack Example ===")
    newstack = stack.Stack()
    print("Popping item.")
    newstack.pop()
    print(f"Stack: {newstack}")
    print("Pushing item.")
    newstack.push(10)
    newstack.push(11)
    print(f"Stack: {newstack}")
    print(newstack.peek())



if __name__ == "__main__":
    main()