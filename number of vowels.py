# Program to count vowels in given letters

# Input number of letters
n = int(input("Number of letters: "))
letters = []

for i in range(n):
    while True:
        ch = input(f"Letter {i+1}: ").lower()
        if ch.isalpha() and len(ch) == 1:  # ensure it's a single letter
            letters.append(ch)
            break
        else:
            print("Invalid input! Please enter a single letter.")

# Define vowels
vowels = "aeiou"

# Count vowels
count = 0
for ch in letters:
    if ch in vowels:
        count += 1

# Output
print("Number of vowels in the puzzle:", count)
