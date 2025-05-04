num = int(input("Enter a number to reverse: "))
rev = 0 #rev will store the reversed number, initially set to 0

while num != 0:  #Keep running the loop as long as num is not zero
    rem = num % 10 #Gets the last digit of num. 1234 % 10 = 9
    rev = rev * 10 + rem #Appends the digit to the reversed number. rev = 0, then rev = 0 * 10 + 9 = 9
    num = num // 10 #Removes the last digit of num 6789 // 10 = 678 (integer division)

print("Reverse number is:", rev)

#---------------------------------
#Method 2

num = "12345"
reverse = int(str(num)[::-1])
print(reverse)
