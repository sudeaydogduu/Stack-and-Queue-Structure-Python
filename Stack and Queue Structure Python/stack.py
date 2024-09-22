def stack():
    global stack_list
    stack_list = list()

def push(input):
    global top_list
    global stack_list

    if top_list >= s_size:
        print("Stack is Full")
    else:
        top_list += 1
        stack_list.append(input)

def pop():
    global top_list
    if top_list <= -1:
        print("Stack is Empty")
    else:
        stack_list.pop()
        top_list = top_list -1

def empty():
    global top_list
    if top_list <= -1:
        return True
    else:
        return False

def top():
    global stack_list
    global top_list
    return stack_list[top_list]

def size():
    global stack_list
    return len(stack_list)

s_size = int(input("Enter the Size of the Stack Structure : "))
if s_size<=0 :
    print("Size is 0, No Action.")
    quit()

top_list = -1  #Because the List Structure Starts from Index 0

stack()
push(26)
push(6)
push(14)
pop()
push(18)
push(2)
pop()
push(17)
push(29)
push(30)
pop()

print("\n\nChecking Queue is Empty :", empty()) #If its empty True, else False
print("Stack Top Element :", top())
print("Stack Size : ", size())
print("Stack Latest Status : ",stack_list)