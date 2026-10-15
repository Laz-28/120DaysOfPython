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

#Password signal strength
password = input("Enter a password: ")

has_upper = False
has_lower = False
has_digit = False
has_symbol = False

for ch in password:
    if ch.isupper():
        has_upper = True
    elif ch.islower():
        has_lower = True
    elif ch.isdigit():
        has_digit = True
    else:
        has_symbol = True

score = 0
if len(password) >= 8:
    score += 1
if has_upper:
    score += 1
if has_lower:
    score += 1
if has_digit:
    score += 1
if has_symbol:
    score += 1

print(f"\nScore: {score}/5")

if score <= 2:
    print("Strength: Weak")
elif score <= 4:
    print("Strength: Medium")
else:
    print("Strength: Strong")

if len(password) < 8:
    print("Tip: use at least 8 characters")
if not has_symbol:
    print("Tip: add a symbol like ! @ # $")

##Slicing strings[start:stop:step]
word = "python"
print(word[0:3])
print(word[0::2])
print(word[::-1])

##Useful operations

print(len("Python"))
print("th" in "Python")

##String methods
s = "hello World"
s.upper()        # "HELLO WORLD"
s.lower()        # "hello world"
s.title()        # "Hello World"
s.capitalize()   # "Hello world"
s.swapcase()     # "HELLO wORLD"

##Cleaning and search
" hi ".strip()
"hello".replace("l", "L")
"hello".find("l")
"hello".count("l")
"hello".startswith("he")
"hello".endswith("lo")

##Splitting and joining

"a,b,c".split(",")            # ["a", "b", "c"]
"one two three".split()       # ["one", "two", "three"]
"-".join(["a", "b", "c"])     # "a-b-c"

##f-string formating
price = 1234.5678
print(f"{price:.2f}")        # 1234.57 (2 decimals)
print(f"{price:,.2f}")       # 1,234.57 (thousands separator)
print(f"{'Hi':>10}")         # right-align in 10 spaces
print(f"{'Hi':<10}|")        # left-align
print(f"{'Hi':^10}|")        # center

##Checking what's inside
"abc".isalpha()       # True (letters only)
"123".isdigit()       # True (digits only)
"abc123".isalnum()    # True (letters or digits)
"   ".isspace()       # True
"abc".islower()       # True
"ABC".isupper()       # True

