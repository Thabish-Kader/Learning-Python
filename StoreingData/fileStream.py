todos = open('todo.txt', 'a')
print('Buy apples', file=todos)
print('Buy kiwis', file=todos)
print('Buy blackberries', file=todos)

todos.close()

# Reading a file
tasks = open('todo.txt')  # default mode of open is to read

for fruits in tasks:
    print(fruits, end='')  # end is used to suppress the new line

tasks.close()

# Understanding the with statement

with open('todos.txt') as tasks:
    for fruits in tasks:
        print(fruits, end='')
