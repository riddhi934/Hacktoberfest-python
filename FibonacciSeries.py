# Sample Input/Output:
# Enter the value of n: 6
# Fibonacci Series upto n is:
# 0 1 1 2 3 5

# Defination of class,
# which contain method to get the fibonacci series upto n terms.
class Fibonacci:
    # Defination of constructor.
    def __init__(self):
        self.firstNum = 0
        self.secondNum = 1
    # Defination of getFibonacci() method.
    def getFibinacci(self, n):
        if(n >= 1):
            print(self.firstNum, end = " ")
        if(n >= 2):
            print(self.secondNum, end = " ")
        i = 2
        while (i < n):
            nextTerm = int(self.firstNum)+int(self.secondNum)
            print(nextTerm, end= " ")
            self.firstNum = int(self.secondNum)
            self.secondNum = int(nextTerm)
            i += 1

# main() function or the driver function.
if __name__ == "__main__":
    # Instantiating Fibonacci class.
    fib = Fibonacci()
    # Taking input from the user for n.
    n = int(input("Enter the value of n: "))
    print("\nFibonacci Series upto n is: ")
    # Computing and printing the fibonacci series,
    # upto n terms.
    fib.getFibinacci(n)