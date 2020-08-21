queries = int(input())
queue = []

first_element_index = 0

for query in range(0, queries):
    element = input().split()
    if len(element) == 2:
        command = int(element[0])
        number = int(element[1])

    else:
        command = int(element[0])

    if command == 1:
        queue.append(number)
        continue
    elif command == 2:
        queue.pop(first_element_index)
        continue
    elif command == 3:
        print(queue[0])
