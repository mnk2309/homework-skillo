queue = []


def enqueue(element):
    queue.append(element)

def dequeue():
    if not queue:
        print("Queue is empty.")
        return None
    else:
        return queue.pop(-1)


enqueue(1)
enqueue(2)
enqueue(3)

print("Test:", queue)

removed_element = dequeue()

print("After removal", queue)