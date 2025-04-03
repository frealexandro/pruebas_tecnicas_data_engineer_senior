# /*
# * Write a program that prints the first 50 numbers of the Fibonacci sequence
# * starting at 0.
# * - The Fibonacci series consists of a sequence of numbers in which
# * the next one is always the sum of the two previous ones.
# * 0, 1, 1, 2, 3, 5, 8, 13...
# */


def fibonacci(n):

    a,b = 0,1

    for _ in range (n):

        yield a

        a,b = b, a + b


print(list(fibonacci(50))) 

# i get some errors in the code ths dicipline is the best way to learn now i have a alarm of 30 min in the day