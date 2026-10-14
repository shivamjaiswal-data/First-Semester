# Question 10

s = input("Enter the main string:\n")
sub = input("Enter the substring you want to find:\n")

count = 0

for i in range(len(s)):

    if s[i:i + len(sub)] == sub:
        count = count + 1

print("Substring is present", count, "times")