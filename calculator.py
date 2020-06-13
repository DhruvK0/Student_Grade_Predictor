#Get the input numbers and operator
num1 = int(input("Enter the first number then hit enter: "))
op = input("Choose an operator for the numbers, 'A' for addition, 'S' for subtraction, 'M' for multiplication, and 'D' for division: ")
num2 = int(input("Enter the second number then hit enter: "))

#calculate the answer based on the numbers and operator
if op == 'A':
    final = num1 + num2
elif op == 'S':
    final = num1-num2
elif op == 'M':
    final = num1*num2
elif op == 'D':
        final = num1/num2

#print final answer
print(final) 
