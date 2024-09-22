def queue():
    global queue_list
    queue_list = list()


def enqueue(input):
    global rear_list
    global queue_list

    if rear_list >= q_size:
        print("Queue is Full")
    else:
        rear_list += 1
        queue_list.insert(rear_list,input)

def dequeue():
    global rear_list
    global front_list
    global queue_list

    if rear_list == front_list:
        print("Queue is Empty")
    else:
        front_list += 1
        queue_list.pop(0)

def is_empty():
    global rear_list
    global front_list
    if rear_list == front_list:
        return True
    else:
        return False

def front():
    global front_list
    return queue_list[0]

def rear():
    global front_list
    return queue_list[-1]

def size():
    global queue_list
    return len(queue_list)


q_size = int(input("Enter the Size of the Queue Structure: "))
if q_size<=0 :
    print("Size is 0, No Action.")
    quit()

rear_list = -1  #Because the List Structure Starts from Index 0
front_list = -1

queue()
enqueue(26)
enqueue(6)
enqueue(14)
dequeue()
enqueue(18)
enqueue(2)
dequeue()
enqueue(17)
enqueue(29)
enqueue(30)
dequeue()

print("\n\nQueue Front Value :",front())
print("Queue Rear Value :",rear())
print("Checking Queue is Empty :", is_empty())
print("Queue Size :", size())
print("Queue Latest Status :",queue_list)