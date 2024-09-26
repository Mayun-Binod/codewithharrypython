# Question 1: How do you open a file in Python for reading?
file = open('example.txt', 'r')
content = file.read()
file.close()
print(content)

# Question 2: How do you write to a file in Python?

file = open('example.txt', 'w')
file.write('Hello, World!')
file.close()
# Question 3: What happens if you try to open a file that doesn't exist in read mode?
try:
    file = open('non_existent_file.txt', 'r')
except FileNotFoundError:
    print('File not found.')