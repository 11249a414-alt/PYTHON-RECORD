# Input from user
num = input("Enter a number: ")

# Check for palindrome
if num == num[::-1]:
    print(f"{num} is a palindrome.")
else:
    print(f"{num} is not a palindrome.")

# Count occurrences of each digit
digit_count = {}  # dictionary to store counts

for digit in num:
    if digit.isdigit():  # ensure only digits are counted
        if digit in digit_count:
            digit_count[digit] += 1
        else:
            digit_count[digit] = 1

print("\nDigit Occurrences:")
for digit, count in sorted(digit_count.items()):
    print(f"Digit {digit} occurs {count} time(s).")
