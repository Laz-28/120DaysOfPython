price = 1234.5678
print(f"{price:.2f}")        # 1234.57 (2 decimals)
print(f"{price:,.2f}")       # 1,234.57 (thousands separator)
print(f"{'Hi':>10}")         # right-align in 10 spaces
print(f"{'Hi':<10}|")        # left-align
print(f"{'Hi':^10}|")        # center


##Project
text = input("Enter a word or phrase: ")

# Clean it: lowercase, keep only letters and digits
cleaned = ""
for ch in text.lower():
    if ch.isalnum():
        cleaned += ch

if cleaned == cleaned[::-1]:
    print(f'"{text}" is a palindrome')
else:
    print(f'"{text}" is not a palindrome')