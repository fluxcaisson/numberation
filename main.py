numbers = []
count = int(input("Enter the number of elements: "))  # Prompt the user to enter the number of elements

for i in range(count):
    num = float(input("Enter number {}: ".format(i+1)))  # Prompt the user to enter each number
    numbers.append(num)  # Add the number to the list

max_num = max(numbers)  # Find the maximum number
min_num = min(numbers)  # Find the minimum number

print("Maximum number:", max_num)
print("Minimum number:", min_num)
