# /*
# * Write a program that prints the first 50 numbers of the Fibonacci sequence
# * starting at 0.
# * - The Fibonacci series consists of a sequence of numbers in which
# * the next one is always the sum of the two previous ones.
# * 0, 1, 1, 2, 3, 5, 8, 13...
# */

# Define a function that generates the first 'n' numbers of the Fibonacci sequence
def fibonacci(n):  
    # Initialize the list with the first two numbers of the sequence
    fib_sequence = [0, 1]  
    
    # Use a loop to generate the next Fibonacci numbers
    # Since we already have two numbers in the list, we only need to add (n - 2) more
    for _ in range(n - 2):  
        # Calculate the next number by adding the last two numbers in the list
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    
    # Return the complete Fibonacci sequence
    return fib_sequence  

# Call the function to get the first 50 Fibonacci numbers
fib_50 = fibonacci(50)  

# Convert the numbers to strings and join them with commas to print them as a list
print(", ".join(map(str, fib_50)))  

#all: it was my fist attempt i use chat gpt to solve a part