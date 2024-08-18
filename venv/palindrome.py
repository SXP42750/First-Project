s = "Hello"

for i in range(len(s) // 2):
    if s[i] != s[len(s) - 1 - i]:
        print("Not a palindrome")
        break
else:
    print("Palindrome")